# Evidencia — Streamlit Base + POST /query

## Objetivo

Validar que Streamlit funciona como cliente HTTP del backend FastAPI y permite consultar el RAG sin acceder directamente a ChromaDB, Gemini ni al pipeline interno.

## Arquitectura validada

```text
Streamlit
↓ HTTP
FastAPI
↓
Backend RAG
```

Streamlit utiliza exclusivamente los endpoints HTTP del backend.

## Dependencias añadidas

```text
streamlit==1.64.0
requests==2.34.2
```

`requests` fue elegido como cliente HTTP por simplicidad y porque la comunicación necesaria es síncrona.

## Ejecución

### Terminal 1 — FastAPI

```powershell
python -m uvicorn app.main:app --reload
```

### Terminal 2 — Streamlit

```powershell
python -m streamlit run ui/streamlit_app.py
```

## GET /health

La UI consulta:

```text
GET http://127.0.0.1:8000/health
```

### API disponible

Se validó visualmente:

```text
API disponible.
```

### API caída

Con FastAPI detenido se validó:

```text
No se pudo conectar con la API.
```

La UI no muestra stack traces al usuario.

## POST /query

Streamlit envía:

```json
{
  "question": "...",
  "top_k": 5
}
```

a:

```text
POST http://127.0.0.1:8000/query
```

La respuesta HTTP contiene:

```text
answer
citations
abstained
retrieved
```

## Caso válido

Pregunta utilizada:

```text
¿Qué hace la Q de Annie?
```

Resultado:

```text
HTTP 200
abstained = false
respuesta visible
citations visibles
retrieved visible
```

Las citas utilizadas se relacionan con los ranks correspondientes de `retrieved`.

Ejemplo validado:

```text
citations = [2, 3]

rank 2 → Citado
rank 3 → Citado
```

## Evidencia recuperada

Para cada resultado se muestran:

```text
rank
source
distance
text
```

Dentro de cada expander también se muestran:

```text
doc_title
index
id
```

Esto permite trazabilidad desde la respuesta hasta los chunks recuperados.

## top_k configurable

Se validó:

```text
top_k = 3
```

Resultado:

```text
3 chunks recuperados
```

Posteriormente se restauró:

```text
top_k = 5
```

Resultado:

```text
5 chunks recuperados
```

El valor default permanece en 5.

## Pregunta vacía

Se probó una pregunta vacía.

La UI mostró:

```text
La pregunta no puede estar vacía.
```

La consulta no fue enviada al backend.

## Caso fuera de dominio

Pregunta:

```text
¿Cómo hago una pizza napolitana?
```

Resultado:

```text
HTTP 200
abstained = true
citations = []
mensaje de abstención visible
chunks recuperados disponibles
```

La abstención se muestra como un resultado válido y no como un error HTTP.

## Caso relacionado pero no respaldado

Pregunta:

```text
¿Cuál es el mejor campeón del parche?
```

Resultado:

```text
HTTP 200
abstained = true
citations = []
Sin citas.
5 chunks recuperados visibles
```

Esto confirma que la UI conserva la política de abstención del backend.

## Manejo de errores

La UI distingue:

```text
pregunta vacía
HTTP 400
otros errores HTTP
timeout
fallo de conexión
```

No convierte una abstención válida en un error técnico.

## Resultado final

Se validó correctamente el flujo completo:

```text
usuario
↓
Streamlit
↓
POST /query
↓
FastAPI
↓
RAG
↓
answer + citations + abstained + retrieved
↓
Streamlit
```

Streamlit no importa ni utiliza directamente:

```text
app/rag.py
app/retrieve.py
app/store.py
ChromaDB
Google AI
Gemini
embeddings
```

Toda la comunicación entre frontend y backend ocurre mediante HTTP.

## Conclusión

`07 V1` cumple su criterio principal de éxito:

> Un usuario puede consultar el RAG completo desde Streamlit exclusivamente a través de FastAPI y visualizar una respuesta grounded junto con citas y evidencia recuperada trazable.
