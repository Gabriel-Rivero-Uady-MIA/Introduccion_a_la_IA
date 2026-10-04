# Evidencia — 04 V1 ChromaDB

## Objetivo

Comprobar el funcionamiento básico de **ChromaDB con persistencia en disco**, utilizando embeddings generados externamente por `Mi_embed.py` y chunks reales del corpus de **LoL Knowledge & Patch Assistant**.

En esta etapa no se realiza todavía la ingestión completa de los 1400 chunks ni retrieval semántico.

---

## 1. Instalación y verificación de ChromaDB

Se instaló ChromaDB dentro del entorno virtual del proyecto:

```powershell
pip install chromadb
```

Versión verificada:

```text
chromadb 1.5.9
```

---

## 2. PersistentClient y colección de prueba

Se creó un cliente persistente utilizando:

```python
client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)
```

La base quedó almacenada en:

```text
chroma_db/
```

Se creó inicialmente una colección de prueba:

```text
lol_test
```

y se verificó su existencia mediante:

```python
client.list_collections()
```

Resultado inicial:

```text
Colecciones: [Collection(name=lol_test)]
Registros: 0
```

---

## 3. Primer registro con embedding real

Se utilizó `Mi_embed.py` para generar externamente un embedding real de Google AI a partir del texto:

```text
Annie lanza una bola de fuego con su habilidad Q.
```

Resultado:

```text
Dimensión del embedding: 768
Registros: 1
```

El registro se almacenó explícitamente en Chroma mediante:

- `id`
- `document`
- `embedding`
- `metadata`

Datos recuperados:

```text
ID: test_1
Documento: Annie lanza una bola de fuego con su habilidad Q.
Metadata: {'source': 'prueba_controlada', 'doc_title': 'Annie', 'index': 0}
Dimensión guardada: 768
```

Esto confirmó que ChromaDB recibió el vector ya generado y no calculó el embedding automáticamente.

---

## 4. Prueba de persistencia

Se cerró el proceso de escritura y posteriormente se ejecutó un segundo script dedicado únicamente a lectura.

El nuevo proceso abrió:

```python
client = chromadb.PersistentClient(
    path=str(CHROMA_PATH)
)

collection = client.get_collection(
    name="lol_test"
)
```

El registro continuó disponible:

```text
Registros: 1
ID: test_1
Dimensión guardada: 768
```

Por lo tanto, se confirmó que los datos permanecen almacenados después de finalizar el proceso original.

---

## 5. Integración con chunks reales del corpus

Se utilizó el pipeline actual del proyecto:

```text
data/*.md
↓
data.py
↓
Corpus
↓
chunk.py
↓
1400 chunks
```

Configuración de chunking:

```text
chunk_size = 300
overlap = 60
```

Resultado:

```text
Documentos: 5
Chunks totales: 1400
```

Para la prueba controlada se seleccionó un chunk real por cada documento del corpus:

| Chunk ID | Documento |
|---:|---|
| 0 | `champion_abilities_26.19.md` |
| 1227 | `champion_stats_26.19.md` |
| 1302 | `game_mechanics.md` |
| 1313 | `items_26.19.md` |
| 1396 | `patch_notes.md` |

Cada chunk conservó:

```text
id
doc_title
source
index
text
```

---

## 6. Embeddings de los chunks reales

Los cinco textos se enviaron a:

```python
embed_many(texts)
```

Resultado:

```text
Embeddings generados: 5
Dimensión: 768
```

El flujo probado fue:

```text
Chunk.text
↓
Mi_embed.py
↓
Google AI
↓
embedding 768D
↓
ChromaDB
```

---

## 7. Inserción de los chunks reales

Se creó una colección independiente para esta prueba:

```text
lol_real_chunks_test
```

Los cinco registros se guardaron en ChromaDB con:

```text
id
document
embedding
metadata
```

Metadata utilizada:

```text
doc_title
source
index
```

Resultado:

```text
Registros guardados: 5
```

---

## 8. Persistencia con chunks reales

Se ejecutó posteriormente un script separado de lectura que no generó nuevos embeddings ni realizó inserciones.

Resultado:

```text
Registros: 5
```

Se recuperaron correctamente los IDs:

```text
0
1227
1302
1313
1396
```

Para cada registro se comprobó la presencia de:

```text
document
metadata
embedding 768D
```

Esto confirmó que los chunks reales y sus embeddings permanecieron almacenados después de cerrar el proceso que realizó la inserción.

---

## 9. Conclusión de 04 V1

Se confirmó que **ChromaDB puede almacenar de forma persistente los embeddings generados externamente por Google AI junto con el texto y metadata de cada chunk**.

La arquitectura validada es:

```text
Corpus Markdown
↓
data.py
↓
chunk.py
↓
Chunk
↓
Mi_embed.py
↓
embedding Google AI 768D
↓
ChromaDB persistente
```

ChromaDB no genera los embeddings en esta implementación. Los vectores son creados por `Mi_embed.py` y entregados explícitamente a Chroma mediante `embeddings=`.

---

## Checkpoint final

> ChromaDB almacena nuestros embeddings de Google junto con el texto del chunk y su metadata. Utilizamos una colección persistente en disco. Insertamos manualmente algunos chunks reales, cerramos el proceso, volvimos a abrir Chroma y verificamos que los registros continuaban presentes. Chroma no calculó los embeddings; los recibió de nuestro `Mi_embed.py`.

### Estado de V1

- [x] ChromaDB instalado.
- [x] `PersistentClient` funcionando.
- [x] Colección creada y recuperada.
- [x] Embedding real de Google almacenado.
- [x] 5 chunks reales guardados.
- [x] Metadata almacenada.
- [x] IDs definidos.
- [x] Embeddings de 768 dimensiones comprobados.
- [x] Persistencia en disco comprobada.
- [x] Evidencia de V1 generada.

---

## Siguiente bloque

El siguiente chat será:

```text
RAG_LoL_04_V2_Ingest
```

Objetivo:

```text
5 documentos
↓
1400 chunks
↓
embed_many()
↓
ingestión automática en ChromaDB
```

El diseño de `store.py` se mantendrá evolutivo durante V1, V2 y V3. Al finalizar esos bloques se realizará una revisión final para decidir si la versión acumulada debe consolidarse o refactorizarse en una versión definitiva.
