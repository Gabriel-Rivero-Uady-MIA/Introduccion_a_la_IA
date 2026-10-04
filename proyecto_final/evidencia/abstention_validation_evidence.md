# Evidencia — Abstention Validation

## Proyecto

**LoL Knowledge & Patch Assistant**  
Bloque: **05 V3 — Abstention + Validation**

---

## Objetivo

Validar que el RAG pueda distinguir razonablemente entre:

- preguntas con evidencia suficiente en el corpus;
- preguntas fuera de dominio;
- preguntas relacionadas con League of Legends pero no respaldadas por el corpus.

El objetivo final es evitar que el sistema responda únicamente porque ChromaDB siempre devuelve vecinos.

---

## Configuración validada

```text
chunk_size = 300
overlap = 60

embedding_model = gemini-embedding-2
embedding_dim = 768

generation_model = gemini-3.8-flash

collection = lol_corpus_26_19
records = 1400
space = l2

top_k = 5
```

En distancia L2:

```text
menor distancia = mayor similitud
```

Sin embargo, la similitud no implica necesariamente que el contexto sea suficiente para responder.

---

## Arquitectura relevante

El flujo validado en V3 quedó conceptualmente así:

```text
pregunta
↓
retrieve(top_k=5)
↓
Retrieved[]
↓
build_context()
↓
build_prompt()
↓
Gemini evalúa si el contexto cubre la pregunta
↓
ABSTAINED: true / false
↓
parse_model_response()
↓
extract_citations()
↓
validate_citations()
↓
RAGAnswer
```

La responsabilidad de la abstención queda en la capa RAG, no dentro de ChromaDB ni dentro de `Mi_retrieve.py`.

---

## Estructura `RAGAnswer`

Se agregó una salida estructurada:

```python
@dataclass(frozen=True)
class RAGAnswer:
    answer: str
    citations: list[int]
    abstained: bool
    retrieved: list[Retrieved]
```

Esto permite distinguir programáticamente entre una respuesta normal y una abstención.

### Comportamiento esperado

Si existe evidencia suficiente:

```text
abstained = False
answer = respuesta grounded
citations = [n, ...]
retrieved = top-k recuperados
```

Si no existe evidencia suficiente:

```text
abstained = True
answer = mensaje explícito de abstención
citations = []
retrieved = top-k recuperados
```

Los resultados recuperados se conservan para debugging y futura integración con FastAPI.

---

## Estrategias evaluadas

### 1. Threshold L2 puro

Criterio conceptual:

```text
si best_distance > X
→ abstenerse
```

Se descartó como criterio principal.

La evidencia mostró que una distancia menor puede indicar similitud semántica sin demostrar que el contexto responda realmente la pregunta.

Dos casos fueron especialmente importantes:

```text
¿Cómo funciona la tenacidad?
best_distance = 0.9311
→ sí existe evidencia suficiente
→ abstained = False
```

mientras que:

```text
¿Cuál es el mejor campeón del parche?
best_distance = 0.7136
→ no existe evidencia suficiente para determinar "el mejor"
→ abstained = True
```

Por tanto:

> **La distancia L2 sirve como señal de similitud del retrieval, pero no como prueba de suficiencia de evidencia.**

---

### 2. Abstención basada en cobertura semántica del contexto

Se reforzó el prompt para exigir que Gemini:

```text
use únicamente el contexto;
no complete con conocimiento externo;
indique si existe evidencia suficiente;
devuelva ABSTAINED: true o false.
```

Formato solicitado:

```text
ABSTAINED: true o false
ANSWER: texto de la respuesta
```

Este enfoque fue validado con preguntas válidas, fuera de dominio y ambiguas.

---

## Hallazgo especial — mecánicas generales

Las consultas de mecánicas mostraron que la distancia absoluta puede ser difícil de interpretar.

Ejemplo:

```text
¿Cómo funciona la tenacidad?
Rank 1 = 0.9311
```

A pesar de esa distancia relativamente alta, el top-5 recuperó evidencia distribuida entre:

```text
game_mechanics
champion_abilities
```

Los chunks incluían:

- definición general de Tenacity;
- excepciones de crowd control;
- interacción con Brittle;
- ejemplos concretos de habilidades.

Gemini pudo sintetizar correctamente esa evidencia.

Esto muestra que la calidad del contexto puede depender del **conjunto top-k**, no únicamente del mejor vecino individual.

También ayuda a explicar por qué conceptos transversales como:

```text
tenacity
armor
magic resistance
```

pueden producir vecindarios más complejos: aparecen en mecánicas, habilidades, objetos y estadísticas.

---

## Dataset final de validación

Se usaron seis preguntas:

### Válidas

```text
¿Qué hace la Q de Annie?
¿Cómo funciona la tenacidad?
```

### Fuera de dominio

```text
¿Cómo hago una pizza napolitana?
¿Cuál es la capital de Japón?
```

### Ambiguas / relacionadas con LoL pero no soportadas

```text
¿Cuál es el mejor campeón del parche?
¿Cuál es la mejor build competitiva actual?
```

---

## Resultados finales

| Tipo | Pregunta | Best distance | Esperado | Resultado | Correcto |
|---|---|---:|---|---|---|
| Válida | ¿Qué hace la Q de Annie? | 0.4579 | responder | `abstained=False` | ✓ |
| Válida | ¿Cómo funciona la tenacidad? | 0.9311 | responder | `abstained=False` | ✓ |
| Fuera de dominio | ¿Cómo hago una pizza napolitana? | 1.0277 | abstenerse | `abstained=True` | ✓ |
| Fuera de dominio | ¿Cuál es la capital de Japón? | 1.0385 | abstenerse | `abstained=True` | ✓ |
| Ambigua | ¿Cuál es el mejor campeón del parche? | 0.7136 | abstenerse | `abstained=True` | ✓ |
| Ambigua | ¿Cuál es la mejor build competitiva actual? | 0.8344 | abstenerse | `abstained=True` | ✓ |

Resultado del test final:

```text
Resultados: 6/6 correctos
```

---

## Citas

Se añadieron:

```python
extract_citations()
validate_citations()
```

### Extracción

Ejemplo:

```text
"Annie causa daño [1] y recupera maná [3]."
```

produce:

```python
[1, 3]
```

### Validación

Con `top_k=5`:

```text
[1, 3] → válido
[1, 6] → inválido
```

El test específico verificó:

```text
Citas válidas encontradas: [1, 3]
Validación: True

Citas inválidas encontradas: [1, 6]
Validación: False
```

Si Gemini produce una cita inexistente, `Mi_rag.py` lanza un error.

---

## Citas durante abstención

Se decidió:

```text
abstained = True
→ citations = []
```

Aunque los chunks recuperados se conservan en `retrieved`, una abstención no expone citas como si respaldaran una respuesta factual.

En la validación final:

```text
Pizza → citations=[]
Capital de Japón → citations=[]
Mejor campeón → citations=[]
Mejor build → citations=[]
```

---

## `top_k` definitivo

Se conserva:

```text
top_k = 5
```

Razones:

1. Ya funcionó correctamente durante V2 y V3.
2. En consultas como Tenacity, varios chunks complementarios aportan evidencia distribuida.
3. Reducir a `k=3` podría eliminar contexto útil.
4. No apareció evidencia suficiente de que `k=5` perjudique la abstención.
5. Los seis casos finales se clasificaron correctamente con `k=5`.

---

## Criterio final de abstención

El criterio final elegido es:

```text
1. El sistema recupera top-5 chunks desde ChromaDB.

2. Las distancias L2 se conservan como señal de retrieval y debugging,
   pero NO se utilizan como threshold definitivo de abstención.

3. Gemini recibe únicamente el contexto recuperado y una instrucción explícita
   de no utilizar conocimiento externo.

4. Gemini debe declarar:

   ABSTAINED: false
   si el contexto contiene evidencia suficiente.

   ABSTAINED: true
   si el contexto no contiene evidencia suficiente.

5. Mi_rag.py parsea esa decisión.

6. Si abstained=False:
   - conserva la respuesta;
   - extrae las citas;
   - valida que las citas correspondan a ranks existentes.

7. Si abstained=True:
   - devuelve una abstención explícita;
   - citations=[];
   - conserva retrieved para debugging.
```

---

## Archivos finales relevantes

### Código productivo modificado

```text
Mi_rag.py
```

Ahora contiene:

```text
RAGAnswer
extract_citations()
validate_citations()
parse_model_response()
build_context()
build_prompt()
answer_question() -> RAGAnswer
```

### Tests conservados

```text
Test/test_abstention.py
Test/test_citations.py
```

### Scripts exploratorios eliminados después de cumplir su función

```text
Test/test_abstention_prompt.py
Test/test_abstention_distances.py
```

---

## Limitaciones conocidas

La validación realizada es deliberadamente pequeña y pedagógica.

No se implementaron:

```text
rerankers
cross-encoders
LLM-as-a-judge adicional
segundo clasificador
query rewriting
typo correction
query normalization
```

La decisión de abstención depende del comportamiento del modelo de generación y del prompt.

El test de citas valida que los números `[n]` existan dentro del top-k, pero no comprueba automáticamente que cada afirmación esté semánticamente respaldada por la cita correspondiente.

---

## Conclusión

V3 demuestra que el RAG puede distinguir razonablemente cuándo responder y cuándo abstenerse.

El sistema ya no responde automáticamente porque ChromaDB haya devuelto vecinos.

La decisión final queda basada en la suficiencia semántica del contexto:

```text
evidencia suficiente
→ respuesta grounded
→ citas válidas
→ abstained=False

evidencia insuficiente
→ abstención explícita
→ citations=[]
→ abstained=True
```

La validación final obtuvo:

```text
6/6 casos correctos
```

Por tanto, el objetivo de **05 V3 — Abstention + Validation** queda cumplido.
