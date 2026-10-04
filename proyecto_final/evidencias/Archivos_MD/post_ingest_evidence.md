# Evidencia — `06 V2 — POST /ingest`

## Objetivo

Validar que FastAPI pueda exponer la ingestión real del proyecto mediante `POST /ingest`, reutilizando el pipeline existente de:

```text
Document / Corpus
↓
chunking
↓
Google AI embeddings
↓
ChromaDB
```

sin duplicar lógica y sin poner en riesgo la colección productiva.

---

## Estado inicial

Configuración heredada:

```text
chunk_size = 300
overlap = 60

embedding model = gemini-embedding-2
embedding_dim = 768

collection = lol_corpus_26_19
records = 1400
```

FastAPI ya exponía:

```text
GET /health
```

con respuesta:

```json
{
  "status": "ok"
}
```

---

## Auditoría del backend

Se revisaron:

```text
app/main.py
app/ingest.py
app/data.py
app/chunk.py
app/embed.py
app/store.py
requirements.txt
```

Conclusiones principales:

- `app/data.py` define `Document`, `Corpus` y `load_corpus(...)`.
- `app/chunk.py` recibe un `Corpus` y genera chunks sin depender de Chroma ni Google AI.
- `app/embed.py` expone `embed_many(...)` con `gemini-embedding-2` y dimensión 768.
- `app/store.py` expone `ChromaStore(path, collection_name)`, lo que permite usar una colección de prueba aislada.
- `app/ingest.py` contenía la lógica real de ingestión, pero estaba concentrada en `main()`.
- `app/main.py` inicialmente solo exponía `GET /health`.

---

## Refactor mínimo de ingestión

Se separó la lógica reutilizable de `app/ingest.py`.

Se creó:

```python
ingest_corpus(corpus: Corpus, store: ChromaStore) -> dict[str, int]
```

El flujo quedó:

```text
main()
    ↓
ingest_corpus(...)

POST /ingest
    ↓
ingest_corpus(...)
```

Por lo tanto, CLI y FastAPI reutilizan el mismo pipeline.

También se mantuvieron:

```text
chunk_size = 300
overlap = 60
batch_size = 25
```

y los IDs estables:

```text
{source}::chunk_{index}
```

---

## Política ante duplicados

La función reutilizable consulta los IDs ya existentes en Chroma y procesa únicamente los faltantes.

Comportamiento observado:

```text
primer ingest
→ chunk inexistente
→ embedding
→ add a Chroma

segundo ingest del mismo documento
→ ID ya existente
→ no se genera embedding
→ no se duplica el registro
```

No se implementó actualización o reindexado automático de documentos existentes.

Ese problema continúa fuera de scope.

---

## Contrato de `POST /ingest`

Se eligió:

```text
multipart/form-data
```

con uno o varios archivos.

Formatos soportados:

```text
.md
.txt
```

FastAPI transforma los archivos recibidos en:

```text
Document[]
↓
Corpus
↓
ingest_corpus(...)
```

La respuesta devuelve:

```json
{
  "documents": 1,
  "chunks": 1,
  "chunks_indexed": 1,
  "total_records": 1
}
```

---

## Dependencia añadida

Se añadió a `requirements.txt`:

```text
python-multipart==0.0.32
```

para permitir recepción de archivos mediante `multipart/form-data`.

---

## Estrategia de prueba aislada

Para no tocar producción se utilizaron:

```text
tests/data/ingest_test.md
```

y una base Chroma separada:

```text
tests/chroma_ingest_test
collection = ingest_test_collection
```

Para las pruebas HTTP se utilizó otra colección aislada:

```text
tests/chroma_ingest_api_test
collection = ingest_api_test_collection
```

La colección productiva permaneció separada:

```text
chroma_db
collection = lol_corpus_26_19
```

---

## Prueba directa de la función de ingestión

Comando:

```text
python -m tests.test_ingest_service
```

### Primera ejecución

Resultado:

```text
Documentos: 1
Chunks: 1
Chunks ya existentes: 0
Chunks pendientes: 1

Batch 1/1
Embeddings recibidos: 1
Chunks indexados en esta ejecución: 1
Registros en Chroma: 1
```

Resultado estructurado:

```python
{
    'documents': 1,
    'chunks': 1,
    'chunks_indexed': 1,
    'total_records': 1
}
```

Persistencia verificada:

```text
Registros persistidos: 1
```

---

## Prueba de duplicado / idempotencia

Se ejecutó nuevamente el mismo test sin borrar la colección.

Resultado:

```text
Documentos: 1
Chunks: 1
Chunks ya existentes: 1
Chunks pendientes: 0
Todos los chunks ya existen en Chroma.
```

Resultado estructurado:

```python
{
    'documents': 1,
    'chunks': 1,
    'chunks_indexed': 0,
    'total_records': 1
}
```

Conclusión:

```text
el mismo documento no se duplica
```

---

## Validación de FastAPI

Se confirmó que `app.main` expone:

```text
/health
/ingest
```

además de las rutas automáticas de FastAPI:

```text
/openapi.json
/docs
/docs/oauth2-redirect
/redoc
```

---

## Prueba HTTP real de `POST /ingest`

FastAPI se levantó con variables temporales:

```text
CHROMA_PATH=tests/chroma_ingest_api_test
COLLECTION_NAME=ingest_api_test_collection
```

Comando de servidor:

```text
python -m uvicorn app.main:app --reload
```

La petición HTTP real se ejecutó con:

```text
curl.exe -X POST "http://127.0.0.1:8000/ingest"   -F "files=@tests/data/ingest_test.md"
```

### Primera ejecución HTTP

Resultado del backend:

```text
Documentos: 1
Chunks: 1
Chunks ya existentes: 0
Chunks pendientes: 1

Batch 1/1
Embeddings recibidos: 1
Chunks indexados en esta ejecución: 1
Registros en Chroma: 1
```

FastAPI respondió:

```text
POST /ingest → 200 OK
```

---

## Segunda ejecución HTTP

Se repitió exactamente la misma petición.

Resultado:

```text
Chunks ya existentes: 1
Chunks pendientes: 0
Todos los chunks ya existen en Chroma.
```

FastAPI respondió nuevamente:

```text
POST /ingest → 200 OK
```

Conclusión:

```text
POST /ingest es idempotente para el mismo documento
```

---

## Validación de entrada inválida

Se probó:

```text
tests/data/invalid.csv
```

Respuesta:

```json
{
  "detail": "Tipo de archivo no soportado: invalid.csv"
}
```

Estado HTTP:

```text
400 Bad Request
```

---

## Validación de `/health`

Se volvió a ejecutar:

```text
GET /health
```

Resultado:

```text
200 OK
```

Respuesta:

```json
{
  "status": "ok"
}
```

Por lo tanto, la implementación de `/ingest` no rompió el endpoint heredado de V1.

---

## Swagger / OpenAPI

`/docs` muestra:

```text
GET /health
POST /ingest
```

Se observó un problema de renderizado en Swagger UI para el selector de múltiples archivos: el esquema OpenAPI generado representa los archivos como strings con `contentMediaType`, y Swagger UI los muestra como campos de texto en vez de selector de archivos.

Por esta razón, la validación funcional real de `POST /ingest` se realizó con `curl.exe`.

El endpoint HTTP sí funcionó correctamente.

---

## Verificación de producción

Después de todas las pruebas se verificó explícitamente:

```text
collection = lol_corpus_26_19
```

Resultado:

```text
Producción: 1400
```

Conclusión:

```text
la colección productiva no fue alterada
```

---

## Checkpoint final

Quedó validado:

```text
✓ app/ingest.py revisado
✓ app/store.py revisado
✓ contrato de entrada decidido
✓ lógica de ingestión reutilizable
✓ no existe un segundo pipeline duplicado
✓ POST /ingest implementado
✓ respuesta estructurada
✓ validación de entrada
✓ test de ingestión aislado
✓ persistencia Chroma verificada
✓ comportamiento ante duplicados conocido
✓ colección lol_corpus_26_19 preservada
✓ GET /health sigue funcionando
✓ /docs muestra POST /ingest
✓ post_ingest_evidence.md generado
```

---

## Conclusión

`06 V2` demuestra que FastAPI puede ejecutar de forma segura y reproducible la ingestión real del proyecto.

El flujo final validado es:

```text
cliente HTTP
↓
POST /ingest
↓
FastAPI valida archivos
↓
Document / Corpus
↓
ingest_corpus(...)
↓
chunk_corpus(...)
↓
embed_many(...)
↓
ChromaStore.add(...)
↓
ChromaDB persistente
↓
respuesta JSON
```

La lógica se probó con una colección aislada, se verificó la persistencia, se validó el comportamiento ante duplicados y se confirmó que la colección productiva `lol_corpus_26_19` conserva sus 1400 registros.

Con esto, `06 V2 — POST /ingest` queda cerrado exitosamente.
