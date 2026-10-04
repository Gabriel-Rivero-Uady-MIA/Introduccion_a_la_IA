# Evidencia — Grounded Generation + Citations

## Proyecto

**LoL Knowledge & Patch Assistant**

Bloque:

```text
05 V2 — Grounded Generation + Citations
```

## Objetivo

Validar el flujo completo:

```text
pregunta
↓
Mi_retrieve.retrieve(top_k=5)
↓
list[Retrieved]
↓
contexto numerado
↓
prompt grounded
↓
Mi_generate.generate()
↓
respuesta en español con citas [n]
```

El criterio principal de éxito fue comprobar que Gemini puede responder usando únicamente la evidencia recuperada y que cada cita `[n]` sea rastreable al chunk correspondiente.

---

## Configuración utilizada

### Retrieval

```text
collection = lol_corpus_26_19
registros = 1400
embedding model = gemini-embedding-2
embedding_dim = 768
space = l2
top_k = 5
```

La colección persistente ya estaba ingerida. Durante estas pruebas no se re-embebió ni se reingestó el corpus.

### Generación

```text
modelo = gemini-3.8-flash
```

Interfaz utilizada:

```python
generate(prompt: str) -> str
```

---

## Arquitectura implementada

Se mantuvieron separadas las responsabilidades existentes:

```text
Mi_retrieve.py
→ recupera evidencia

Mi_generate.py
→ envía un prompt a Gemini y devuelve texto
```

Se añadió:

```text
Mi_rag.py
```

como capa de orquestación entre retrieval y generación.

Flujo:

```text
question
↓
Retrieved[]
↓
build_context()
↓
build_prompt()
↓
generate()
↓
answer
```

---

## Contexto numerado

`build_context()` transforma `list[Retrieved]` en un bloque de evidencia con números correspondientes directamente a `Retrieved.rank`.

Formato:

```text
[1]
Fuente: ...
Texto: ...

[2]
Fuente: ...
Texto: ...
```

Esto permite rastrear una cita como `[2]` directamente al resultado de retrieval con `rank = 2`.

No se envían a Gemini campos como `distance`, `id` o `index`, ya que son útiles para inspección y validación del sistema, pero no forman parte del conocimiento necesario para responder.

---

## Reglas principales del grounded prompt

El prompt final pide a Gemini:

```text
- responder en español;
- usar únicamente la información del contexto;
- no añadir conocimiento externo;
- citar afirmaciones relevantes usando [n];
- usar únicamente números de fuente existentes en el contexto;
- indicar cuando el contexto no contiene evidencia suficiente;
- redactar de forma natural, fluida y explicativa;
- no copiar la estructura del contexto como ficha o diccionario;
- priorizar párrafos en prosa continua;
- evitar listas, viñetas, tablas o secciones salvo que sean necesarias;
- integrar los datos relevantes en una explicación coherente manteniendo las citas.
```

La instrucción de evidencia insuficiente se utiliza en V2 únicamente como regla básica de grounding. La abstención definitiva se evaluará en `05 V3`.

---

## Prueba inicial controlada con evidencia ficticia

Pregunta:

```text
¿Qué hace la Q de Annie?
```

Se construyeron dos `Retrieved` ficticios que indicaban que Annie lanza una bola de fuego y que Desintegración recupera maná al matar, pero no indicaban explícitamente que Desintegración fuera la Q.

Gemini respondió que el contexto no era suficiente para establecer esa relación.

Observación:

```text
✓ no completó el hueco usando conocimiento externo
✓ utilizó únicamente las fuentes disponibles
✓ generó citas válidas
```

Este comportamiento confirmó que el grounded prompt estaba siendo respetado antes de conectar retrieval real.

---

# Pruebas end-to-end con retrieval real

## 1. Habilidad de campeón

Pregunta:

```text
¿Qué hace la Q de Annie?
```

Resultado observado:

- Retrieval recuperó chunks de `champion_abilities_26.19.md`.
- Los chunks `[2]` y `[3]` contenían información de Annie, `Ability Slot: Q` y `Ability Name: Disintegrate`.
- Gemini identificó correctamente la habilidad y explicó su daño, coste, cooldown y comportamiento al eliminar al objetivo.
- La respuesta utilizó citas `[2]` y `[3]`.

Verificación manual:

```text
✓ cita [2] → chunk con Q de Annie / Disintegrate
✓ cita [3] → chunk complementario con Q y pasiva de Annie
✓ no se usaron chunks irrelevantes de Brand o Zilean
```

Observación de estilo:

La primera versión fue demasiado cercana a una ficha técnica. Posteriormente se añadieron instrucciones de redacción natural y prosa continua.

---

## 2. Estadística de campeón

Pregunta:

```text
¿Cuál es la vida base de Annie?
```

Resultado observado:

- Retrieval recuperó `champion_stats_26.19.md`.
- El dato relevante apareció en `[4]`.
- El chunk contenía:

```text
Health: 560 (+96 per level)
```

Respuesta de Gemini:

```text
La vida base de Annie es de 560 (+96 por nivel) [4].
```

Verificación manual:

```text
✓ cita [4] → chunk correcto de estadísticas de Annie
✓ respuesta breve y apropiada para una pregunta factual
```

---

## 3. Objeto

Pregunta:

```text
¿Qué hace el Zhonyas?
```

Resultado observado:

- Retrieval recuperó `items_26.19.md` en `[1]` y `[5]`.
- Los chunks contenían la entrada de `Zhonya's Hourglass`.
- Gemini explicó el activo `Time Stop`, la estasis de 2.5 segundos, la imposibilidad de realizar acciones durante ese tiempo, el cooldown de 120 segundos y las estadísticas del objeto.
- La respuesta utilizó `[1]` y `[5]`.

Verificación manual:

```text
✓ citas [1] y [5] → chunks reales del objeto
✓ chunks de campeones presentes en el top-k fueron ignorados
```

---

## 4. Mecánica general

Pregunta:

```text
¿Cómo funciona la tenacidad?
```

Resultado observado:

- Retrieval recuperó `game_mechanics.md` en `[1]` y `[5]`.
- También aparecieron chunks complementarios de habilidades en `[2]`, `[3]` y `[4]`.
- Gemini explicó que la tenacidad reduce la duración de efectos de control elegibles, que no afecta de igual forma a todos los desplazamientos y que existen reglas específicas de acumulación/interacción.
- Las citas usadas correspondían a chunks que contenían esas afirmaciones.

Verificación manual:

```text
✓ game_mechanics.md presente en posiciones relevantes
✓ citas rastreables a evidencia real
✓ chunks secundarios solo se usaron cuando contenían información pertinente
```

Después del ajuste de estilo, la respuesta se produjo en prosa continua y resultó más natural sin perder las citas.

---

## 5. Patch notes

Pregunta:

```text
¿Qué cambió en el parche 26.19?
```

Resultado observado:

- `patch_notes.md` apareció en `[1]`, `[2]`, `[3]` y `[4]`.
- `[5]` correspondió a `champion_stats_26.19.md` y fue ruido.
- Gemini sintetizó cambios de múltiples campeones, objetos y sistemas.
- La respuesta utilizó citas `[1]`, `[2]`, `[3]` y `[4]`.
- El chunk irrelevante `[5]` no fue utilizado.

Verificación manual:

```text
✓ alta cobertura del documento patch_notes.md
✓ síntesis de varios chunks del mismo documento
✓ cita → chunk rastreable
✓ ruido del top-k ignorado
```

---

# Observaciones sobre `top_k = 5`

Durante estas pruebas `top_k = 5` permitió recuperar evidencia complementaria suficiente para preguntas que requerían más de un chunk.

También introdujo ruido en algunos casos:

```text
Annie Q
→ aparecieron chunks de Brand y Zilean

Zhonya
→ aparecieron chunks de campeones

Patch 26.19
→ apareció un chunk de champion_stats
```

Aun así, Gemini generalmente ignoró los chunks no relacionados y utilizó las fuentes pertinentes.

Conclusión provisional:

```text
top_k = 5 funciona adecuadamente para grounded generation,
pero su valor definitivo se evaluará en 05 V3 junto con abstention y validation.
```

---

# Ajuste de estilo del prompt

Durante las primeras pruebas, las respuestas eran correctas y grounded, pero tendían a reproducir la estructura técnica del corpus en forma de ficha o listado.

Se añadieron reglas para:

```text
redactar de forma natural y explicativa
priorizar prosa continua
evitar listas innecesarias
integrar los datos en una explicación coherente
```

Después del ajuste, la prueba:

```text
¿Cómo funciona la tenacidad?
```

produjo una respuesta continua en párrafos, manteniendo las mismas citas y el mismo grounding.

Resultado:

```text
✓ mejor estilo de redacción
✓ grounding preservado
✓ citas preservadas
✓ sin cambios en retrieval, ChromaDB ni Mi_generate.py
```

---

# Checkpoint final de V2

Quedó validado:

```text
✓ firmas reales de Mi_retrieve.py y Mi_generate.py revisadas
✓ material relevante del profesor revisado
✓ misma carpeta de trabajo reutilizada
✓ Mi_rag.py creado como capa de orquestación
✓ Retrieved[] → contexto numerado
✓ build_context() funcionando
✓ build_prompt() grounded funcionando
✓ retrieval + generation conectados
✓ respuesta en español
✓ citas [n] presentes
✓ citas existentes dentro del top-k
✓ verificación manual cita → evidencia
✓ pruebas sobre habilidad, estadística, objeto, mecánica y patch notes
✓ top_k=5 evaluado durante generación
✓ test_grounded_generation.py validado
✓ estilo de respuesta ajustado a prosa más natural
```

---

# Criterio de éxito

`05 V2` responde afirmativamente a:

> ¿Podemos transformar los chunks recuperados en evidencia numerada y hacer que Gemini produzca una respuesta grounded en español con citas rastreables?

Sí.

La siguiente etapa corresponde a:

```text
RAG_LoL_05_V3_Abstention_Validation
```

donde se evaluarán de forma específica:

```text
distancias L2
criterio de evidencia suficiente
abstención
validación de citas
preguntas fuera de dominio
top_k definitivo
```
