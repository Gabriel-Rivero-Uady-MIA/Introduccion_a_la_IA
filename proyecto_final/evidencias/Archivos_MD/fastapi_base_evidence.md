# Evidencia — 06 V1 Backend Audit + FastAPI Base

## Estructura final

```text
00_Proyecto_Final/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── data.py
│   ├── chunk.py
│   ├── embed.py
│   ├── store.py
│   ├── ingest.py
│   ├── retrieve.py
│   ├── generate.py
│   └── rag.py
├── data/
├── chroma_db/
├── tests/
├── evidencia/
├── ui/
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

## Backend de producción

- `app/data.py`
- `app/chunk.py`
- `app/embed.py`
- `app/store.py`
- `app/ingest.py`
- `app/retrieve.py`
- `app/generate.py`
- `app/rag.py`
- `app/main.py`

## Persistencia

Colección:

```text
lol_corpus_26_19
```

Registros validados:

```text
1400
```

No se realizó reingestión.

## Dependencias principales

```text
chromadb==1.5.9
fastapi==0.142.2
google-genai==2.25.0
python-dotenv==1.2.3
uvicorn==0.54.0
```

## FastAPI

Comando de arranque:

```text
uvicorn app.main:app --reload --port 8000
```

### GET /health

Respuesta validada:

```json
{
  "status": "ok"
}
```

### /docs

Swagger/OpenAPI cargó correctamente y mostró:

```text
GET /health
```

## Smoke tests

Migrados y ejecutados correctamente:

```text
test_generate.py              PASS
test_grounded_generation.py   PASS
test_abstention.py            PASS
test_citations.py             PASS
```

## Decisiones de arquitectura

- Se creó una nueva raíz limpia: `00_Proyecto_Final/`.
- `09_Proyecto_Final_Chunking/` se mantiene como entorno histórico/de desarrollo.
- El backend final vive en `app/`.
- Los módulos `Mi_*` fueron normalizados al migrarlos.
- El código pedagógico/histórico del profesor no se migró al backend final.
- `data/` y `chroma_db/` permanecen fuera de `app/`.
- Streamlit vivirá posteriormente en `ui/`.
- Todavía no se implementaron `POST /ingest` ni `POST /query`.

## Checkpoint final de 06 V1

- ✓ carpeta experimental auditada
- ✓ imports y dependencias revisados
- ✓ backend, tests, evidencia y material histórico clasificados
- ✓ estructura final del backend decidida
- ✓ nombres `Mi_*` normalizados
- ✓ `chroma_db` preservado y validado con 1400 registros
- ✓ `.env`, `.env.example` y `.gitignore` revisados
- ✓ `requirements.txt` generado con versiones funcionales
- ✓ FastAPI instalado y configurado
- ✓ `GET /health` funcionando
- ✓ `/docs` funcionando
- ✓ smoke tests del RAG siguen pasando

`06 V1` queda completado sin implementar todavía `/ingest` ni `/query`.
