# LoL Knowledge & Patch Assistant

Proyecto final de la materia **Introducción a la Inteligencia Artificial**.

Sistema RAG sobre información de **League of Legends** usando **Streamlit, FastAPI, ChromaDB y Google AI**.

<a id="indice"></a>

## Índice

1. [Cómo ejecutar el proyecto desde cero](#1-como-ejecutar-el-proyecto-desde-cero)
2. [Overview del proyecto](#2-overview-del-proyecto)
3. [Stack](#3-stack)
4. [Corpus](#4-corpus)
5. [Chunking](#5-chunking)
6. [Embeddings, ChromaDB y retrieval](#6-embeddings-chromadb-y-retrieval)
7. [Generación, citas y abstención](#7-generacion-citas-y-abstencion)
8. [API](#8-api)
9. [Estados manejados y limitaciones](#9-estados-manejados-y-limitaciones)
10. [Nota académica](#10-nota-academica)

---

<a id="1-como-ejecutar-el-proyecto-desde-cero"></a>

# 1. Cómo ejecutar el proyecto desde cero

Los siguientes pasos están pensados para **Windows + PowerShell**.

## Paso 1 — Abrir la carpeta del proyecto

```powershell
cd 00_Proyecto_Final
```

## Paso 2 — Crear el entorno virtual

```powershell
python -m venv venv
```

## Paso 3 — Activar el entorno

```powershell
.\venv\Scripts\Activate.ps1
```

La terminal debería mostrar:

```text
(venv)
```

## Paso 4 — Instalar dependencias

```powershell
pip install -r requirements.txt
```

## Paso 5 — Crear `.env`

Copia el archivo de ejemplo:

```powershell
Copy-Item .env.example .env
```

La API key se obtiene desde Google AI Studio:

```text
https://aistudio.google.com/app/apikey
```

Después abre `.env` y agrega tu clave:

```env
GOOGLE_API_KEY=TU_API_KEY
API_BASE_URL=http://127.0.0.1:8000
```

Si `GOOGLE_API_KEY` no existe, FastAPI no podrá iniciar correctamente.

## Paso 6 — Levantar FastAPI

En la primera terminal:

```powershell
python -m uvicorn app.main:app --reload
```

FastAPI quedará normalmente en:

```text
http://127.0.0.1:8000
```

Swagger / OpenAPI:

```text
http://127.0.0.1:8000/docs
```

Deben aparecer:

```text
GET  /health
POST /ingest
POST /query
```

Mantén esta terminal abierta.

## Paso 7 — Levantar Streamlit

Abre una **segunda terminal** dentro de `00_Proyecto_Final`.

Activa nuevamente el entorno:

```powershell
.\venv\Scripts\Activate.ps1
```

Luego ejecuta:

```powershell
python -m streamlit run ui/streamlit_app.py
```

Streamlit quedará normalmente en:

```text
http://localhost:8501
```

La interfaz debe mostrar:

```text
API disponible.
```

## Paso 8 — Crear el índice ChromaDB

`chroma_db/` es persistencia local y está en `.gitignore`, por lo que una instalación nueva empieza sin índice.

En Streamlit entra a:

```text
Administración del corpus
```

y selecciona los cinco archivos de:

```text
data/
```

```text
champion_abilities_26.19.md
champion_stats_26.19.md
game_mechanics.md
items_26.19.md
patch_notes.md
```

Después presiona:

```text
Ingerir documentos
```

El flujo es:

```text
archivos
↓
POST /ingest
↓
chunking
↓
embeddings Google AI
↓
ChromaDB
```

La interfaz mostrará:

```text
Documentos procesados
Chunks detectados
Chunks nuevos indexados
Total en colección
```

### Nota sobre la cuota gratuita de Google AI

La ingestión completa genera muchas llamadas de embeddings.

Si se utiliza la cuota gratuita de Google AI, puede ser necesario dividir la carga entre más de un día por los límites vigentes de **RPD** y hacer pausas entre batches por los límites de **TPM**.

Durante el desarrollo, la ingestión se hizo por batches de 25 chunks y con una pausa entre batches. Si la cuota gratuita no permite terminar todo el corpus en una sola sesión, se puede continuar después: la ingestión es idempotente y no vuelve a indexar los chunks que ya existen.

Los límites de Google AI pueden cambiar, así que conviene revisar las cuotas disponibles de la cuenta antes de iniciar una indexación completa.

## Paso 9 — Hacer una consulta

En Streamlit abre:

```text
Consulta
```

Mantén:

```text
top_k = 5
```

Ejemplo:

```text
¿Qué hace la Q de Annie?
```

La interfaz mostrará:

```text
Respuesta
Citas utilizadas
Evidencia recuperada
```

Cada chunk recuperado incluye:

```text
source
distance
texto
doc_title
index
id
```

Otro ejemplo:

```text
¿Cómo funciona la tenacidad?
```

## Paso 10 — Probar abstención

Pregunta fuera del corpus:

```text
¿Cómo hago una pizza napolitana?
```

El sistema debe indicar que no hay evidencia suficiente y mostrar:

```text
Sin citas.
```

## Paso 11 — Detener el proyecto

En cada terminal:

```text
Ctrl + C
```

ChromaDB permanece guardado en disco y vuelve a estar disponible cuando se reinicia FastAPI.

[↑ Volver al índice](#indice)

---

<a id="2-overview-del-proyecto"></a>

# 2. Overview del proyecto

La arquitectura general es:

```text
Usuario
↓
Streamlit
↓ HTTP
FastAPI
↓
RAG
├── chunking
├── embeddings Google AI
├── ChromaDB
├── retrieval top-k
├── Gemini
├── citas [n]
└── abstención
```

Streamlit funciona únicamente como interfaz. No accede directamente a ChromaDB ni a Google AI.

El proyecto permite consultar el corpus, ver la respuesta con citas y evidencia recuperada, y agregar documentos desde la sección de administración.

[↑ Volver al índice](#indice)

---

<a id="3-stack"></a>

# 3. Stack

| Capa | Tecnología | Responsabilidad |
|---|---|---|
| UI | Streamlit | Consulta, carga de documentos, respuesta, citas y evidencia recuperada |
| API | FastAPI | `/health`, `/ingest` y `/query` |
| Base vectorial | ChromaDB | Persistencia de chunks, embeddings y búsqueda top-k |
| Embeddings | Google AI | Convierte documentos y preguntas en vectores |
| Generación | Gemini | Genera la respuesta final usando únicamente el contexto recuperado |

Dependencias principales:

```text
chromadb==1.5.9
fastapi==0.142.2
google-genai==2.25.0
python-dotenv==1.2.3
uvicorn==0.54.0
python-multipart==0.0.32
pytest==9.1.1
streamlit==1.64.0
requests==2.34.2
```

[↑ Volver al índice](#indice)

---

<a id="4-corpus"></a>

# 4. Corpus

El corpus corresponde a **League of Legends, parche 26.19**.

```text
data/
├── champion_abilities_26.19.md
├── champion_stats_26.19.md
├── game_mechanics.md
├── items_26.19.md
└── patch_notes.md
```

Tamaño aproximado:

```text
335,671 palabras
```

Los documentos cubren habilidades, estadísticas, objetos, mecánicas generales y notas del parche.

[↑ Volver al índice](#indice)

---

<a id="5-chunking"></a>

# 5. Chunking

La configuración final es:

```text
chunk_size = 300 palabras
overlap = 60 palabras
```

El ajuste se hizo en dos etapas.

Primero se compararon distintos tamaños de chunk para fijar un tamaño base adecuado. Después de elegir **300 palabras**, se mantuvo ese tamaño fijo y se probó el overlap:

```text
300 / 40
300 / 60
300 / 80
```

La configuración final utilizada fue:

```text
300 / 60
```

Cada chunk conserva:

```text
source
doc_title
index
```

[↑ Volver al índice](#indice)

---

<a id="6-embeddings-chromadb-y-retrieval"></a>

# 6. Embeddings, ChromaDB y retrieval

Modelo de embeddings:

```text
gemini-embedding-2
dimensión = 768
```

El mismo modelo se utiliza para documentos y preguntas.

ChromaDB almacena chunks, embeddings y metadatos, y recupera los vecinos más cercanos.

Valor por defecto:

```text
top_k = 5
```

La colección utilizada durante el desarrollo fue:

```text
lol_corpus_26_19
```

La persistencia local se guarda en:

```text
chroma_db/
```

y esa carpeta está incluida en `.gitignore`.

[↑ Volver al índice](#indice)

---

<a id="7-generacion-citas-y-abstencion"></a>

# 7. Generación, citas y abstención

Los chunks recuperados se numeran como:

```text
[1]
[2]
[3]
...
```

Gemini recibe esos chunks como contexto y debe:

- responder en español;
- usar únicamente la evidencia proporcionada;
- citar mediante `[n]`;
- no utilizar números de fuente inexistentes;
- abstenerse cuando la evidencia no sea suficiente.

Las citas se validan contra los ranks recuperados.

La abstención utiliza:

```text
ABSTAINED: true
```

cuando el contexto no permite responder.

En ese caso:

```text
abstained = true
citations = []
```

Si no existe ningún chunk indexado, el sistema detecta el corpus vacío antes de llamar a Gemini.

[↑ Volver al índice](#indice)

---

<a id="8-api"></a>

# 8. API

FastAPI expone:

```text
GET  /health
POST /ingest
POST /query
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## `GET /health`

```json
{
  "status": "ok"
}
```

## `POST /ingest`

Recibe uno o más archivos `.md` o `.txt`.

Respuesta:

```text
documents
chunks
chunks_indexed
total_records
```

## `POST /query`

Ejemplo:

```json
{
  "question": "¿Qué hace la Q de Annie?",
  "top_k": 5
}
```

Respuesta:

```text
answer
citations
abstained
retrieved
```

`retrieved` contiene:

```text
rank
id
source
doc_title
index
text
distance
```

[↑ Volver al índice](#indice)

---

<a id="9-estados-manejados-y-limitaciones"></a>

# 9. Estados manejados y limitaciones

La aplicación contempla de forma visible:

```text
pregunta vacía
API no disponible
GOOGLE_API_KEY ausente
corpus vacío
archivo vacío
tipo de archivo no soportado
```

Si falta la API key:

```text
No se encontró GOOGLE_API_KEY.
Configura la clave en el archivo .env antes de iniciar FastAPI.
```

El sistema responde únicamente con la información disponible en el corpus.

Si la evidencia recuperada no permite responder de forma suficiente, se abstiene.

[↑ Volver al índice](#indice)

---

<a id="10-nota-academica"></a>

# 10. Nota académica

Este proyecto fue desarrollado con fines académicos y no comerciales.

**League of Legends** y sus contenidos relacionados pertenecen a **Riot Games**. Este proyecto no está patrocinado, respaldado ni afiliado oficialmente con Riot Games.

[↑ Volver al índice](#indice)
