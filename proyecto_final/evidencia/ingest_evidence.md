# Evidencia — 04 V2 Ingest

## Proyecto

**LoL Knowledge & Patch Assistant**

Bloque:

**04 V2 — Ingest**

---

## Objetivo

Automatizar la ingestión completa del corpus RAG:

```text
5 documentos Markdown
↓
data.py
↓
Corpus
↓
chunk.py
↓
1400 chunks
↓
Mi_embed.embed_many()
↓
1400 embeddings de 768 dimensiones
↓
Mi_store.py
↓
ChromaDB persistente
```

---

## Corpus

Documentos utilizados:

```text
champion_abilities_26.19.md
champion_stats_26.19.md
game_mechanics.md
items_26.19.md
patch_notes.md
```

Resultado:

```text
Documentos: 5
Chunks: 1400
```

Configuración de chunking ya congelada desde 03 V1:

```text
chunk_size = 300
overlap = 60
```

---

## Embeddings

Archivo:

```text
Mi_embed.py
```

Modelo:

```text
gemini-embedding-2
```

Dimensión solicitada:

```text
768
```

Función principal utilizada durante ingestión:

```python
embed_many(texts)
```

Validaciones realizadas durante ingestión:

```text
cantidad de embeddings == cantidad de textos
dimensión de cada embedding == 768
```

Resultado final:

```text
Embeddings: 1400
Dimensión: 768
```

---

## ChromaDB

Archivo:

```text
Mi_store.py
```

Persistencia local:

```text
chroma_db/
```

Colección utilizada para el corpus completo:

```text
lol_corpus_26_19
```

Cada registro almacena:

```text
id
document
embedding
metadata:
    doc_title
    source
    index
```

Resultado final:

```text
Registros en Chroma: 1400
```

---

## Diseño de Mi_store.py

Se implementó una clase:

```python
ChromaStore
```

Responsabilidad:

```text
Mi_store.py
↓
encapsular únicamente operaciones con ChromaDB
```

Métodos implementados en V2:

```text
__init__()
reset_collection()
add()
count()
get()
```

`Mi_store.py` no conoce directamente:

```text
Chunk
Corpus
Mi_embed.py
Google AI
batching
```

La preparación de datos permanece en `Mi_ingest.py`.

---

## Diseño de Mi_ingest.py

Responsabilidad:

```text
cargar corpus
↓
generar chunks
↓
preparar IDs, documents y metadatas
↓
controlar batching
↓
solicitar embeddings
↓
guardar batches mediante Mi_store.py
```

Esto adopta la filosofía del `pipeline.py` del profesor:

```text
orquestar componentes
sin implementar internamente sus responsabilidades especializadas
```

---

## IDs

Se descartó utilizar únicamente:

```text
str(chunk.id)
```

como ID definitivo.

Formato seleccionado:

```text
{source}::chunk_{index}
```

Ejemplos:

```text
champion_abilities_26.19.md::chunk_0
champion_abilities_26.19.md::chunk_700
patch_notes.md::chunk_3
```

Criterios cumplidos:

```text
únicos
reproducibles
comprensibles
trazables al documento y posición
```

Validación:

```text
IDs: 1400
IDs únicos: True
```

---

## Metadata

Metadata definitiva de V2:

```python
{
    "doc_title": chunk.doc_title,
    "source": chunk.source,
    "index": chunk.index,
}
```

El texto completo del chunk se almacena como:

```text
document
```

No se añadió metadata específica de campeones, habilidades u objetos.

---

## Política de colección

Para desarrollo se planteó inicialmente una reconstrucción completa mediante:

```text
reset_collection()
```

Durante la ingestión completa aparecieron límites de cuota de Google AI.

Para evitar perder embeddings ya generados y persistidos, `Mi_ingest.py` fue adaptado para:

```text
leer store.count()
↓
validar los IDs ya existentes
↓
reanudar desde el siguiente chunk
```

Esto permitió continuar una ingestión interrumpida sin recalcular los registros ya persistidos.

No se implementó reindexado incremental sofisticado.

---

## Batching

Prueba inicial:

```text
10 chunks
↓
10 embeddings
↓
10 registros en Chroma
```

Prueba multi-batch:

```text
25 chunks

Batch 1 → 10
Batch 2 → 10
Batch 3 → 5
```

Resultado:

```text
Registros finales en Chroma: 25
```

Para la ingestión completa se utilizó:

```text
BATCH_SIZE = 25
```

Con 1400 chunks:

```text
56 batches
```

---

## Manejo de límites de Google AI

Durante la ingestión se observaron errores:

```text
429 RESOURCE_EXHAUSTED
```

Primero por:

```text
TPM
```

y posteriormente por:

```text
RPD del Free Tier
```

Los registros ya persistidos en Chroma se conservaron.

Se verificó que la ingestión podía reanudarse desde el número de registros existentes.

Después de habilitar billing, el límite mostrado para Gemini Embedding 2 pasó a:

```text
RPM: 3000
TPM: 1M
RPD: ilimitado
```

La ingestión continuó desde los registros ya almacenados hasta completar los 1400.

---

## Validación administrativa final

Se ejecutó una inspección desde un proceso independiente.

Resultado:

```text
Registros en Chroma: 1400
Chunks esperados: 1400
```

Se inspeccionaron:

```text
primer registro
registro intermedio
último registro
```

y se verificó en cada caso:

```text
ID
document
metadata
source
index
```

Ejemplos observados:

```text
champion_abilities_26.19.md::chunk_0
champion_abilities_26.19.md::chunk_700
patch_notes.md::chunk_3
```

---

## Persistencia

La ingestión completa terminó en un proceso.

Posteriormente se abrió ChromaDB desde otro proceso mediante:

```text
python -m Test.check_full_ingest
```

y se obtuvo:

```text
Registros en Chroma: 1400
```

Además, los registros pudieron recuperarse mediante `get()`.

Conclusión:

```text
Persistencia completa validada.
```

---

## Resultado final

```text
Documentos: 5
Chunks: 1400
Embeddings: 1400
Dimensión: 768
Registros en Chroma: 1400
Persistencia: validada
```

---

## Checkpoint 04 V2

La ingestión toma los cinco documentos, genera los 1400 chunks ya definidos, obtiene sus embeddings de Google AI en lotes y almacena cada chunk en ChromaDB junto con su texto y metadata.

Se definieron IDs reproducibles, una política clara de almacenamiento y una estrategia de reanudación ante interrupciones.

Al finalizar se verificó:

```text
✓ corpus carga correctamente
✓ 5 documentos
✓ 1400 chunks
✓ IDs estables y únicos
✓ metadata definida
✓ batching funcionando
✓ prueba automática pequeña
✓ prueba multi-batch
✓ ingestión completa
✓ 1400 embeddings
✓ todos 768D
✓ 1400 registros en Chroma
✓ inspección administrativa
✓ persistencia completa validada
```

---

## Siguiente bloque

```text
RAG_LoL_04_V3_Retrieval
```

Ahí se incorporará por primera vez:

```text
pregunta
↓
Mi_embed.embed()
↓
embedding 768D
↓
ChromaDB query
↓
top-k
↓
chunks + distances/scores
```
