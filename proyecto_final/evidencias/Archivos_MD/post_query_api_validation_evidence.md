# Evidencia — 06 V3 POST /query + API Validation

## Objetivo

Validar que FastAPI expone el RAG completo mediante `POST /query`, reutilizando el pipeline real del backend y devolviendo una respuesta JSON estable con:

- `answer`
- `citations`
- `abstained`
- `retrieved`

También se verificó que `GET /health` y `POST /ingest` continúan funcionando sin regresiones.

---

## Arquitectura validada

```text
cliente HTTP
↓
POST /query
↓
question + top_k
↓
app.main
↓
app.rag.run_rag(...)
↓
app.retrieve.retrieve(...)
↓
ChromaDB
↓
app.rag.answer_question(...)
↓
Gemini
↓
RAGAnswer
↓
serialización JSON
```

FastAPI no reimplementa retrieval, grounding, abstención ni citas.

---

## Adaptación realizada en `app/rag.py`

Se añadió una función de orquestación reutilizable:

```python
def run_rag(
    question: str,
    store: ChromaStore,
    top_k: int = 5,
) -> RAGAnswer:
    retrieved = retrieve(
        question=question,
        store=store,
        top_k=top_k,
    )

    return answer_question(
        question=question,
        retrieved=retrieved,
    )
```

La función existente `answer_question(...)` se conservó.

---

## Contrato de `POST /query`

### Request

```json
{
  "question": "¿Qué hace la Q de Annie?",
  "top_k": 5
}
```

- `question`: requerido.
- `top_k`: opcional.
- default de `top_k`: `5`.
- `top_k >= 1`.

Las preguntas vacías o formadas solo por espacios se rechazan antes de llamar embeddings o Gemini.

### Response

```json
{
  "answer": "...",
  "citations": [1, 2, 3],
  "abstained": false,
  "retrieved": [
    {
      "rank": 1,
      "id": "...",
      "source": "...",
      "doc_title": "...",
      "index": 57,
      "text": "...",
      "distance": 0.4578
    }
  ]
}
```

Cada elemento de `retrieved` serializa:

```text
rank
id
source
doc_title
index
text
distance
```

---

## Prueba directa del pipeline RAG

Se probó `run_rag()` antes de conectar HTTP.

Pregunta:

```text
¿Qué hace la Q de Annie?
```

Resultado:

```text
ABSTAINED: False
CITATIONS: [2, 3]
RETRIEVED: 5 resultados
```

Las citas correspondieron a ranks existentes dentro de `retrieved`.

---

## Validación manual por Swagger

Swagger mostró correctamente:

```text
GET  /health
POST /ingest
POST /query
```

### Caso válido

Request:

```json
{
  "question": "¿Qué hace la Q de Annie?",
  "top_k": 5
}
```

Resultado:

```text
HTTP 200
abstained = false
citations = [1, 2, 3]
retrieved = 5
```

Los chunks recuperados pertenecieron al corpus real, incluyendo:

```text
champion_abilities_26.19.md
```

### Fuera de dominio

Request:

```json
{
  "question": "¿Cómo hago una pizza napolitana?",
  "top_k": 5
}
```

Resultado:

```text
HTTP 200
abstained = true
citations = []
```

El sistema respondió explícitamente que no había evidencia suficiente.

### Pregunta relacionada pero no respaldada

Request:

```json
{
  "question": "¿Cuál es el mejor campeón del parche?",
  "top_k": 5
}
```

Resultado:

```text
HTTP 200
abstained = true
citations = []
```

El sistema no inventó una clasificación ni utilizó conocimiento externo.

### Pregunta vacía

Requests probados:

```json
{
  "question": "",
  "top_k": 5
}
```

y:

```json
{
  "question": "   ",
  "top_k": 5
}
```

Resultado en ambos casos:

```text
HTTP 400
detail = "La pregunta no puede estar vacía."
```

### `top_k = 3`

Request:

```json
{
  "question": "¿Qué hace la Q de Annie?",
  "top_k": 3
}
```

Resultado:

```text
HTTP 200
abstained = false
retrieved = 3
citations ⊆ {1, 2, 3}
```

Esto confirma que `top_k` viaja correctamente desde HTTP hasta retrieval.

---

## Corrección de configuración detectada durante V3

Durante la primera prueba de `/query`, FastAPI estaba leyendo variables de entorno heredadas de V2:

```text
CHROMA_PATH = tests/chroma_ingest_api_test
COLLECTION_NAME = ingest_api_test_collection
```

Por ello `/query` consultó accidentalmente la colección de prueba.

Se limpiaron las variables:

```powershell
Remove-Item Env:CHROMA_PATH -ErrorAction SilentlyContinue
Remove-Item Env:COLLECTION_NAME -ErrorAction SilentlyContinue
```

Luego se verificó:

```text
PATH: chroma_db
COLLECTION: lol_corpus_26_19
RECORDS: 1400
```

Tras reiniciar Uvicorn, `/query` recuperó correctamente chunks del corpus de producción.

---

## Tests automatizados

Archivo creado:

```text
tests/test_query_api.py
```

Se usó `FastAPI TestClient` y `monkeypatch` para aislar la capa HTTP sin consumir cuota de Google ni depender de Chroma real.

Casos automatizados:

```text
test_query_valid
test_query_out_of_domain
test_query_not_supported
test_query_empty
test_query_blank_spaces
test_query_top_k_3
```

Comando:

```powershell
python -m pytest tests/test_query_api.py -v
```

Resultado:

```text
6 passed
```

También se observaron 3 warnings de deprecación provenientes de dependencias externas. No afectaron los tests.

Se añadió `pytest==9.1.1` al entorno de desarrollo para hacer reproducibles las pruebas.

---

## Regression check — `GET /health`

Resultado:

```text
HTTP 200
{"status":"ok"}
```

`GET /health` sigue funcionando después de implementar `/query`.

---

## Regression check — `POST /ingest`

Para evitar modificar producción, se usó una colección aislada:

```text
CHROMA_PATH = tests/chroma_ingest_regression_v3
COLLECTION_NAME = ingest_regression_v3
```

La prueba se ejecutó mediante `curl.exe`, ya que Swagger no ofrece selector de archivos en este entorno.

Archivo:

```text
tests/data/ingest_test.md
```

Resultado observado:

```text
Documents: 1
Chunks: 1
Chunks ya existentes: 0
Chunks pendientes: 1

Batch 1/1
Embeddings recibidos: 1
Chunks indexados en esta ejecución: 1
Registros en Chroma: 1

POST /ingest HTTP/1.1 200 OK
```

Después de la prueba se limpiaron las variables de entorno para restaurar la configuración normal.

---

## Estado final de producción

Configuración final:

```text
CHROMA_PATH = chroma_db
COLLECTION_NAME = lol_corpus_26_19
RECORDS = 1400
top_k default = 5
```

La colección de producción se preservó.

---

## Archivos creados o modificados en V3

```text
app/rag.py
app/main.py
tests/test_run_rag.py
tests/test_query_api.py
requirements.txt
evidencia/post_query_api_validation_evidence.md
```

---

## Checkpoint final

Se validó:

```text
✓ firmas reales revisadas
✓ contrato QueryRequest definido
✓ pregunta vacía validada
✓ top_k opcional con default 5
✓ POST /query implementado
✓ app/rag.py reutilizado
✓ RAGAnswer serializado
✓ Retrieved serializado
✓ answer presente
✓ citations presentes
✓ abstained presente
✓ retrieved presente
✓ caso válido funciona
✓ fuera de dominio funciona
✓ caso no respaldado funciona
✓ pregunta vacía falla correctamente
✓ citas siguen apuntando al rank correcto
✓ /docs muestra los 3 endpoints
✓ tests/test_query_api.py — 6/6
✓ GET /health sigue funcionando
✓ POST /ingest sigue funcionando
✓ evidencia final creada
```

## Conclusión

`06 V3` queda completado exitosamente.

FastAPI expone el RAG completo mediante `POST /query`, delegando en el pipeline existente y devolviendo una respuesta JSON estable con respuesta, citas, abstención y evidencia recuperada. Las validaciones manuales y automatizadas confirmaron el comportamiento correcto para respuestas válidas, abstención, preguntas vacías y `top_k` configurable. Además, `GET /health` y `POST /ingest` continúan funcionando sin regresiones.
