# Evidencia — Embeddings Google AI

## 1. Configuración utilizada

Para esta etapa se utilizó Google AI como proveedor de embeddings.

- **Modelo:** `gemini-embedding-2`
- **Dimensión del vector:** `768`
- **SDK:** `google-genai`
- **Variable de entorno:** `GOOGLE_API_KEY`

El módulo de embeddings mantiene una única configuración de modelo y dimensión para evitar incompatibilidades posteriores entre los embeddings de los documentos y los embeddings de las preguntas.

---

## 2. Prueba controlada con textos

Se probaron los siguientes textos:

```text
A: Annie lanza una bola de fuego con su Q.
B: Desintegración es una habilidad de Annie.
C: Malphite obtiene armadura adicional.
```

Para cada texto se obtuvo:

- un objeto de tipo `list`;
- un vector de `768` dimensiones;
- valores numéricos válidos.

### Similitud coseno

Resultados obtenidos:

```text
cos(A, B) = 0.6729671589730889
cos(A, C) = 0.5740792305745596
```

Se observó que los textos A y B, relacionados con Annie y su habilidad, obtuvieron una similitud mayor que A y C.

Esto confirma el comportamiento semántico esperado del modelo de embeddings.

---

## 3. Prueba con chunks reales del corpus

Se cargó el corpus completo y se aplicó la configuración de chunking previamente seleccionada:

```text
Chunk size: 300 palabras
Overlap: 60 palabras
Chunks totales: 1400
```

Primero se probaron 10 chunks reales del corpus.

Todos los chunks evaluados produjeron correctamente:

```text
Chunk.text
    ↓
embed(...)
    ↓
list[float]
    ↓
768 dimensiones
```

No fue necesario modificar `data.py`, `chunk.py` ni la estructura de la clase `Chunk`.

---

## 4. Prueba representativa entre documentos

Se seleccionaron deliberadamente chunks provenientes de diferentes partes del corpus:

```text
Annie        -> champion_abilities_26.19.md
Mordekaiser  -> champion_abilities_26.19.md
Objeto       -> items_26.19.md
Mecánica     -> game_mechanics.md
Parche       -> patch_notes.md
```

Los cinco chunks generaron embeddings de `768` dimensiones.

Algunas similitudes obtenidas fueron:

```text
Annie vs Mordekaiser = 0.7017235665288527
Annie vs Objeto      = 0.6945368346952505
Objeto vs Mecánica   = 0.723936757770876
```

Los valores no se interpretan todavía como una evaluación completa del retrieval. Esta prueba únicamente confirma que chunks reales de distintas fuentes pueden ser transformados y comparados dentro del mismo espacio vectorial.

---

## 5. Prueba de múltiples embeddings

Además de la función:

```python
embed(text)
```

se implementó:

```python
embed_many(texts)
```

para permitir el procesamiento de varios textos en una misma operación, pensando en la futura fase de ingestión del corpus.

La prueba utilizó 3 textos y produjo:

```text
Cantidad de textos: 3
Cantidad de vectores: 3

Vector 1: list[float], dimensión 768
Vector 2: list[float], dimensión 768
Vector 3: list[float], dimensión 768
```

Esto confirma que cada texto produce su propio embedding independiente.

---

## 6. Compatibilidad entre `embed()` y `embed_many()`

Se utilizó exactamente el mismo texto mediante ambas funciones:

```text
Annie lanza una bola de fuego con su Q.
```

Resultados:

```text
Dimensión single: 768
Dimensión many:   768
Tipo single:      list
Tipo many:        list
Cosine:           0.9999999999999998
```

La similitud coseno es prácticamente `1.0`.

Por lo tanto, ambas funciones producen representaciones compatibles dentro del mismo espacio vectorial.

Esto permite utilizar posteriormente:

```text
/query
   ↓
embed(question)
```

y:

```text
/ingest
   ↓
embed_many(chunks)
```

manteniendo el mismo modelo y la misma dimensión.

---

## 7. Conclusión

La etapa de embeddings quedó validada correctamente.

Se comprobó que:

```text
✓ Google AI funciona desde el proyecto
✓ La API key se carga mediante .env
✓ El modelo de embeddings está definido
✓ embed(text) devuelve list[float]
✓ Los vectores tienen dimensión 768
✓ cosine similarity funciona
✓ Textos relacionados presentan mayor similitud semántica
✓ Los chunks reales del corpus pueden ser embebidos
✓ Diferentes documentos del corpus comparten el mismo espacio vectorial
✓ embed_many(texts) genera múltiples embeddings correctamente
✓ embed() y embed_many() producen vectores compatibles
```

La indexación completa de los `1400` chunks se realizará posteriormente junto con ChromaDB, para evitar generar todos los embeddings antes de contar con un mecanismo persistente para almacenarlos.
