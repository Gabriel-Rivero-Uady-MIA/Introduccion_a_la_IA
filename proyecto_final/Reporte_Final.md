# Reporte final — LoL Knowledge & Patch Assistant

## 1. Dominio y tamaño del corpus

El proyecto es un sistema de RAG (*Retrieval-Augmented Generation*) enfocado en **League of Legends**, con el corpus congelado en el **parche 26.19**. Su objetivo es responder preguntas sobre campeones, habilidades, estadísticas, objetos, mecánicas generales y cambios del parche.

El corpus final está compuesto por **5 documentos Markdown**:

- `champion_abilities_26.19.md`
- `champion_stats_26.19.md`
- `game_mechanics.md`
- `items_26.19.md`
- `patch_notes.md`

En conjunto contienen **335,671 palabras**. Después del proceso de particionado se obtuvieron **1,400 chunks**, que fueron convertidos en embeddings mediante el modelo **`gemini-embedding-2`** de Google AI. Cada embedding tiene **768 dimensiones**.

La colección final se almacena de forma persistente en ChromaDB con el nombre `lol_corpus_26_19`, donde cada registro conserva el texto del chunk, su embedding y metadata que permite identificar su documento de origen y posición dentro del corpus.

## 2. Cómo se particionó el corpus y por qué

La configuración de chunking no se eligió de forma arbitraria. Primero se compararon tres configuraciones:

- **200 palabras / 40 de overlap**
- **300 palabras / 60 de overlap**
- **400 palabras / 80 de overlap**

La configuración **200/40** produjo **2,099 chunks**. Aunque generaba fragmentos más específicos, durante las pruebas se observó que podía dividir demasiado habilidades y descripciones complejas, distribuyendo información relacionada entre varios chunks.

La configuración **400/80** produjo **1,049 chunks**. Conservaba más contenido dentro de cada fragmento, pero aumentaba la probabilidad de mezclar habilidades, objetos o conceptos distintos dentro de una misma ventana.

La configuración **300/60** produjo **1,400 chunks** y mostró un mejor equilibrio entre ambos extremos: mantenía suficiente contexto para conservar información relacionada sin incorporar demasiado contenido ajeno al concepto principal.

Después se mantuvo fijo `chunk_size = 300` y se compararon overlaps de **40, 60 y 80 palabras**. Con 40 palabras existía menor redundancia, pero mayor riesgo de perder continuidad entre fragmentos consecutivos. Con 80 palabras aumentaba la continuidad, pero también la repetición de información. Por ello se seleccionó finalmente:

```text
chunk_size = 300
overlap = 60
```

Esta configuración ofreció un balance adecuado entre **contexto y redundancia**.

## 3. Cómo decide el sistema abstenerse

Una dificultad importante del sistema es que **ChromaDB siempre devuelve vecinos**, incluso cuando la pregunta no pertenece al dominio del corpus. Por lo tanto, recuperar resultados no significa necesariamente que exista evidencia suficiente para responder.

Inicialmente se evaluó utilizar un umbral fijo sobre la distancia L2 del mejor resultado. Sin embargo, las pruebas mostraron que esta estrategia no era confiable. Por ejemplo, la consulta **“¿Cómo funciona la tenacidad?”** obtuvo una distancia relativamente alta y aun así el conjunto recuperado contenía evidencia suficiente para responder correctamente. En cambio, **“¿Cuál es el mejor campeón del parche?”** obtuvo una distancia menor, pero el corpus no contenía evidencia para determinar objetivamente cuál campeón era “el mejor”.

La razón es que particularmente en el contexto de **"league of legends"** tanto en las descripciones de habilidades y objetos, se usan **key words** con significado único en el contexto del juego, el MD *"game_mechanics"* trata de resolver este problema como un diccionario para estas **key words**, en la evidencia recopilada se puede observar que palabras que se repiten mucho a lo largo de descripciones como **"Armadura"**, **"Resistencia mágica"**, **"Tenacidad"**, al momento de ser solicitados a descripción generan un valor l2 muy alto, sin embargo, son el sistema con K5 es capaz completamente de obtener el contexto adecuado y responder las preguntas sin problema. 

Para observar mejor como se comportan estas preguntas y porque son relevantes para responder y concluir el metodo que se utilizo de abstinencia, puede revisar el documento "abstention_validation_evidence.md" en la carpeta de evidencia. 

Por esta razón, la distancia L2 se conserva como una señal útil de similitud y para inspección, pero **no se utiliza como criterio definitivo de abstención**.

El flujo final es:

```text
pregunta
→ recuperación de top-5 chunks
→ Gemini recibe únicamente ese contexto
→ evalúa si la evidencia es suficiente
```

Si el contexto contiene evidencia suficiente:

```text
abstained = false
respuesta grounded
citas [n]
```

Si el contexto no contiene evidencia suficiente:

```text
abstained = true
citations = []
```

Esta política se validó con **6 preguntas**: dos válidas, dos fuera de dominio y dos relacionadas con League of Legends pero no respaldadas por el corpus. Los **6 casos fueron clasificados correctamente**.

## 4. Qué sale de Google AI y qué hace ChromaDB

Google AI cumple **dos funciones diferentes** dentro del sistema.

### Embeddings

Durante la ingestión, cada chunk del corpus se envía al modelo **`gemini-embedding-2`**, que produce un vector de **768 dimensiones**:

```text
texto del chunk
→ Google AI / gemini-embedding-2
→ embedding de 768 dimensiones
```

La misma operación se realiza con la pregunta del usuario. De esta forma, documentos y consultas quedan representados dentro del mismo espacio vectorial y pueden compararse semánticamente.

### Generación

Después del retrieval, los chunks recuperados se convierten en un contexto numerado y se envían al modelo **`gemini-3.8-flash`**. En esta etapa Gemini no busca directamente en la base de datos: recibe la pregunta y la evidencia que ya fue recuperada.

Su función es:

```text
pregunta + evidencia recuperada
→ Gemini
→ respuesta en español
→ citas [n]
→ decisión de abstención
```

El prompt obliga al modelo a utilizar únicamente el contexto proporcionado y a no completar información faltante con conocimiento externo.

### ChromaDB

**ChromaDB no genera embeddings en esta implementación.** Los vectores son creados previamente mediante Google AI y después se almacenan explícitamente en la base.

ChromaDB se utiliza para:

- almacenar de forma persistente los embeddings;
- conservar el texto y metadata de cada chunk;
- comparar el embedding de la consulta con los embeddings almacenados;
- devolver los **top-k chunks** más cercanos según distancia L2.

Por lo tanto, la separación principal del sistema puede resumirse así:

```text
Google AI / gemini-embedding-2
→ convierte texto en vectores

ChromaDB
→ almacena vectores y recupera los chunks más cercanos

Google AI / gemini-3.8-flash
→ utiliza los chunks recuperados para generar la respuesta
  y decidir si existe evidencia suficiente
```

Esta separación permite que la respuesta final no dependa únicamente del conocimiento interno del modelo, sino de evidencia recuperada desde el corpus específico del proyecto.
