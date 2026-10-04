# Evidencia — Gemini API

## Proyecto

**LoL Knowledge & Patch Assistant**  
**Bloque:** `05 V1 — Gemini API`

## Objetivo

Validar que el proyecto puede enviar un prompt a un modelo Gemini mediante Google AI y recibir una respuesta de texto usando una interfaz simple y reutilizable.

Flujo validado:

```text
prompt
↓
Mi_generate.generate()
↓
Google AI / Gemini
↓
respuesta de texto
```

En este bloque todavía **no** se conecta retrieval, contexto recuperado, citas ni abstención.

---

## SDK utilizado

```text
google-genai
```

Import principal:

```python
from google import genai
```

El mismo SDK ya utilizado por `Mi_embed.py` se reutiliza para la capa de generación.

---

## Modelo de generación probado

```text
gemini-3.8-flash
```

Configuración utilizada en `Mi_generate.py`:

```python
MODEL = "gemini-3.8-flash"
```

---

## Configuración de API key

Se reutiliza la convención ya existente del proyecto:

```text
GOOGLE_API_KEY
```

La clave se carga desde `.env` mediante `python-dotenv`:

```python
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError(
        "No se encontró GOOGLE_API_KEY en el archivo .env"
    )
```

Cliente:

```python
client = genai.Client(api_key=api_key)
```

No se creó una segunda variable como `GEMINI_API_KEY`.

---

## Interfaz implementada

`Mi_generate.py` ofrece una función mínima:

```python
generate(prompt: str) -> str
```

Responsabilidad:

```text
entrada:
    prompt: str

salida:
    str
```

La función envía el prompt a Gemini mediante:

```python
response = client.models.generate_content(
    model=MODEL,
    contents=prompt,
)
```

y devuelve:

```python
response.text
```

También valida que la respuesta no esté vacía.

---

## Prueba 1 — generación simple

Comando ejecutado desde la raíz del proyecto:

```text
python -m Test.test_generate
```

Prompt:

```text
Explica qué es un RAG en una oración.
```

Respuesta obtenida:

```text
Un RAG (Generación Aumentada por Recuperación) es una técnica de inteligencia artificial que busca información relevante en fuentes de datos externas para que un modelo de lenguaje genere respuestas más precisas, actualizadas y confiables.
```

Validaciones:

```text
Modelo: gemini-3.8-flash
Tipo devuelto: str
Texto no vacío: True
```

Resultado:

```text
PASS
```

---

## Prueba 2 — seguimiento de instrucción simple

Prompt:

```text
Responde únicamente con la palabra OK.
```

Respuesta obtenida:

```text
OK
```

Validaciones:

```text
Tipo devuelto: str
Texto no vacío: True
```

Resultado:

```text
PASS
```

---

## Manejo básico de errores

Implementado en V1:

```text
✓ API key ausente
✓ respuesta vacía
✓ errores del SDK se propagan al llamador
```

No se implementaron todavía:

```text
retry complejo
fallback de modelos
sistema de colas
```

---

## Observación del SDK

Durante las pruebas apareció una advertencia relacionada con Automatic Function Calling (AFC).

La advertencia **no impidió la generación** y ambas pruebas finalizaron correctamente. En V1 no se utilizan tools ni function calling, por lo que no se modificó la arquitectura a partir de este warning.

---

## Resultado final

`Mi_generate.py` quedó validado como una capa de generación independiente:

```text
prompt
↓
Gemini
↓
str
```

Checkpoint de `05 V1`:

```text
✓ material del profesor revisado
✓ configuración de API key reutilizada
✓ Mi_generate.py creado
✓ generate(prompt) funcionando
✓ respuesta de texto válida
✓ Test/test_generate.py funcionando
✓ instrucción simple respetada
✓ manejo básico de errores
```

La siguiente etapa será:

```text
05 V2 — Grounded Generation + Citations
```

Ahí se conectará la salida de retrieval con Gemini mediante contexto numerado y citas `[n]`.
