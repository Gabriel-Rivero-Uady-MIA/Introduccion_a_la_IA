# Evidencia de Retrieval — LoL Knowledge & Patch Assistant

## 1. Configuración validada

- **Modelo de embedding:** `gemini-embedding-2`
- **Dimensión:** `768`
- **Vector store:** ChromaDB persistente
- **Colección:** `lol_corpus_26_19`
- **Registros:** `1400`
- **Métrica observada en la colección:** `L2`
- **Interpretación:** menor `distance` = vecino más cercano
- **Chunking vigente:** `300` palabras con `60` de overlap
- **Flujo de consulta:**

```text
pregunta
↓
Mi_embed.embed()
↓
embedding 768D
↓
Mi_store.query()
↓
ChromaDB
↓
Mi_retrieve.retrieve()
↓
list[Retrieved]
```

No se reingirió ni se volvió a embeber el corpus durante estas pruebas.

---

## 2. Primera consulta controlada — habilidad de campeón

**Pregunta:**

```text
¿Qué hace la Q de Annie?
```

**Top-3:**

```text
[1] champion_abilities_26.19.md::chunk_57 | distance ≈ 0.4579
[2] champion_abilities_26.19.md::chunk_56 | distance ≈ 0.4960
[3] champion_abilities_26.19.md::chunk_55 | distance ≈ 0.5572
```

La evidencia específica de `Q — Disintegrate` aparece dentro del top-3. La consulta identifica correctamente la zona semántica de Annie, aunque el rank 1 contiene principalmente contexto de otras habilidades.

**Resultado:** retrieval correcto para habilidad de campeón.

---

## 3. Estadística de campeón

### Consulta en español

```text
¿Cuál es la vida base de Annie?
```

El chunk correcto fue localizado previamente como:

```text
champion_stats_26.19.md::chunk_3
```

y contiene:

```text
Champion: Annie
Health: 560 (+96 per level)
```

En retrieval quedó en:

```text
rank 4
distance ≈ 0.6937
```

### Consulta en inglés

```text
What is Annie's base health?
```

El mismo chunk correcto quedó en:

```text
rank 4
distance ≈ 0.5377
```

**Observación:** el inglés produjo una distancia menor, pero el rank fue el mismo.

**Conclusión:** `top_k=3` pierde esta evidencia; `top_k=5` sí la recupera.

---

## 4. Objetos — Zhonya's Hourglass

Chunks identificados:

```text
items_26.19.md::chunk_81
items_26.19.md::chunk_82
```

El `chunk_82` contiene suficiente información para responder preguntas comunes sobre Zhonya: nombre, precio, estadísticas, activo `Time Stop`, duración de estasis y aliases.

### Alias presentes en el corpus

```text
zonyas
zhonyas
```

### Pruebas

```text
que hace el zonyas
→ chunk_82 rank 1

que hace el zhonyas
→ chunk_82 rank 1
```

Con typo no incluido explícitamente:

```text
que hace el zonias
→ chunk_82 rank 24
→ distance ≈ 1.0590
```

**Conclusión:** los aliases presentes en el corpus funcionan muy bien, pero un typo no representado degrada fuertemente el retrieval.

Posible mejora futura: normalización/corrección de consulta antes del embedding.

---

## 5. Mecánicas generales — Tenacity

Ground truth identificado en:

```text
game_mechanics.md::chunk_5
game_mechanics.md::chunk_6
```

### Formulación 1

```text
que hace la tenacidad
```

El contenido de `game_mechanics.md` cayó aproximadamente en:

```text
rank 31
```

### Formulación 2

```text
como funciona la tenacidad
```

Resultado:

```text
[1] champion_abilities_26.19.md::chunk_687 | distance ≈ 0.9945
[2] game_mechanics.md::chunk_6              | distance ≈ 0.9992
[3] champion_abilities_26.19.md::chunk_866 | distance ≈ 1.0141
```

**Conclusión:** el retrieval es sensible a la formulación de la consulta. Una paráfrasis semánticamente equivalente puede cambiar mucho el ranking.

Posible mejora futura: query rewriting / query normalization.

---

## 6. Patch notes

### Consulta general

```text
que cambio en el parche 26.19
```

Resultado:

```text
[1] patch_notes.md::chunk_2
[2] patch_notes.md::chunk_0
[3] patch_notes.md::chunk_3
```

### Consulta específica sobre objetos

```text
cambio algun item en el parche 26.19
```

Resultado:

```text
[1] patch_notes.md::chunk_0
[2] patch_notes.md::chunk_2
[3] patch_notes.md::chunk_1
```

### Referencia temporal coloquial

```text
que trae el nuevo parche
```

Resultado:

```text
[1] patch_notes.md::chunk_0 | distance ≈ 0.8328
[2] patch_notes.md::chunk_3 | distance ≈ 0.8433
[3] patch_notes.md::chunk_2 | distance ≈ 0.8575
```

**Conclusión:** `patch_notes.md` queda muy bien discriminado incluso cuando el usuario no menciona explícitamente `26.19`.

---

## 7. Comparación de `top_k`

Se compararon:

```text
top_k = 2
top_k = 3
top_k = 5
```

usando una sola recuperación `top_k=5` por pregunta y observando los primeros 2, 3 y 5 resultados.

### Hallazgos

- **Annie Q:** `k=2` ya contiene evidencia útil.
- **Annie vida base:** el chunk correcto aparece en `rank 4`; `k=2` y `k=3` fallan, `k=5` lo recupera.
- **Zhonya:** el chunk correcto aparece en `rank 1`.
- **Tenacity:** con la formulación `"como funciona la tenacidad"`, el chunk correcto aparece en `rank 2`.
- **Nuevo parche:** `k=2` ya devuelve evidencia correcta; `k=5` empieza a introducir ruido adicional.

### Decisión provisional

```text
top_k provisional = 5
```

No porque siempre produzca mejores resultados, sino porque es el menor valor probado que no pierde el caso de Annie stats.

Este valor queda sujeto a revisión cuando se integre la generación con Gemini.

---

## 8. Consulta fuera de dominio

**Pregunta:**

```text
como hago una pizza napolitana
```

Resultado:

```text
[1] champion_abilities_26.19.md::chunk_670  | distance ≈ 1.1124
[2] champion_abilities_26.19.md::chunk_1174 | distance ≈ 1.1365
[3] champion_abilities_26.19.md::chunk_643  | distance ≈ 1.1412
```

Chroma devuelve vecinos incluso cuando la pregunta no pertenece al dominio.

**Conclusión:** el vector store por sí solo no sabe abstenerse.

Las distancias fuera de dominio fueron mayores que en muchas consultas válidas, pero existe solapamiento con consultas válidas como Tenacity (~0.999), por lo que no se define todavía un umbral de abstención.

---

## 9. Conclusiones de V3

Quedó validado:

```text
✓ colección persistente reutilizada
✓ no se reingirió el corpus
✓ embed(question) funcionando
✓ embeddings de 768 dimensiones
✓ query por embedding explícito
✓ top-k funcionando
✓ documents recuperados
✓ metadata recuperada
✓ distances entendidas como L2
✓ formato Retrieved funcionando
✓ consultas de distintas fuentes probadas
✓ comparación top_k = 2 / 3 / 5
✓ consulta fuera de dominio observada
```

Hallazgos importantes:

```text
1. top_k=5 es el mejor default provisional entre los valores probados.
2. El retrieval funciona bien con aliases presentes en el corpus.
3. Typos no contemplados pueden degradar fuertemente el ranking.
4. La formulación de la pregunta puede cambiar significativamente el resultado.
5. Chroma siempre devuelve vecinos, incluso fuera de dominio.
6. No se implementa todavía abstención ni min_score.
7. No hay evidencia suficiente para modificar el chunking 300/60.
```

El núcleo de retrieval del RAG queda funcional y listo para continuar hacia la etapa de generación grounded con Gemini.
