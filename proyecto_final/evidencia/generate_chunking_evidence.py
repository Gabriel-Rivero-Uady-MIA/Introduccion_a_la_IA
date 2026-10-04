from data import load_corpus
from chunk import chunk_corpus
from pathlib import Path


OUTPUT_FILE = Path("chunking_evidence.md")


def find_chunk(chunks, search_text):
    for position, chunk in enumerate(chunks):
        if search_text.lower() in chunk.text.lower():
            return position
    return None


def write_chunk_context(lines, chunks, position):
    start = max(0, position - 1)
    end = min(len(chunks), position + 2)

    for i in range(start, end):
        chunk = chunks[i]

        marker = " **← ENCONTRADO**" if i == position else ""

        lines.append(
            f"### Chunk {chunk.id}{marker}\n"
        )
        lines.append(
            f"- Source: `{chunk.source}`\n"
            f"- Index: `{chunk.index}`\n"
            f"- Palabras: `{chunk.word_count}`\n"
        )

        lines.append("```text")
        lines.append(chunk.text)
        lines.append("```")
        lines.append("")


corpus = load_corpus("data")

lines = []

lines.append("# Evidencia de selección de configuración de Chunking")
lines.append("")
lines.append("## 1. Medición del corpus")
lines.append("")
lines.append(f"**Corpus:** {corpus.name}")
lines.append("")
lines.append(f"**Documentos:** {len(corpus.documents)}")
lines.append("")

total_words = 0

for document in corpus.documents:
    words = len(document.text.split())
    total_words += words

    lines.append(
        f"- `{document.source}`: **{words} palabras**"
    )

lines.append("")
lines.append(f"**TOTAL:** {total_words} palabras")
lines.append("")


# ---------------------------------------------------------
# Comparación inicial de tamaños
# ---------------------------------------------------------

lines.append("## 2. Comparación inicial de configuraciones")
lines.append("")

configurations = [
    (200, 40),
    (300, 60),
    (400, 80),
]

for size, overlap in configurations:

    chunks = chunk_corpus(
        corpus=corpus,
        size=size,
        overlap=overlap,
    )

    total_chunk_words = sum(
        chunk.word_count for chunk in chunks
    )

    average_words = total_chunk_words / len(chunks)

    lines.append(
        f"### Configuración {size}/{overlap}"
    )
    lines.append("")
    lines.append(
        f"- Chunks totales: **{len(chunks)}**"
    )
    lines.append(
        f"- Promedio de palabras por chunk: "
        f"**{average_words:.2f}**"
    )
    lines.append("")

    for document in corpus.documents:

        document_chunks = [
            chunk
            for chunk in chunks
            if chunk.source == document.source
        ]

        lines.append(
            f"- `{document.source}`: "
            f"{len(document_chunks)} chunks | "
            f"último chunk: "
            f"{document_chunks[-1].word_count} palabras"
        )

    lines.append("")


# ---------------------------------------------------------
# Pruebas cualitativas
# ---------------------------------------------------------

qualitative_tests = [
    (
        "3. Prueba cualitativa — Q de Annie",
        "### Q — Disintegrate",
    ),
    (
        "4. Prueba cualitativa — E de Thresh",
        "### E — Flay",
    ),
    (
        "5. Prueba cualitativa — Manamune",
        "**Item:** Manamune",
    ),
]

for section_title, search_text in qualitative_tests:

    lines.append(f"## {section_title}")
    lines.append("")
    lines.append(
        f"Texto utilizado para localizar el contenido: "
        f"`{search_text}`"
    )
    lines.append("")

    for size, overlap in configurations:

        chunks = chunk_corpus(
            corpus=corpus,
            size=size,
            overlap=overlap,
        )

        lines.append(
            f"### Configuración {size}/{overlap}"
        )
        lines.append("")

        position = find_chunk(
            chunks,
            search_text,
        )

        if position is None:
            lines.append(
                "**No se encontró el texto buscado.**"
            )
            lines.append("")
            continue

        write_chunk_context(
            lines,
            chunks,
            position,
        )


# ---------------------------------------------------------
# Comparación específica del overlap
# ---------------------------------------------------------

lines.append(
    "## 6. Comparación específica del overlap"
)
lines.append("")
lines.append(
    "Se mantuvo fijo `chunk_size = 300` y se modificó "
    "únicamente el overlap."
)
lines.append("")

overlap_configurations = [
    (300, 40),
    (300, 60),
    (300, 80),
]

search_text = "### E — Flay"

for size, overlap in overlap_configurations:

    chunks = chunk_corpus(
        corpus=corpus,
        size=size,
        overlap=overlap,
    )

    lines.append(
        f"### Configuración {size}/{overlap}"
    )
    lines.append("")

    position = find_chunk(
        chunks,
        search_text,
    )

    if position is None:
        lines.append(
            "**No se encontró el texto buscado.**"
        )
        lines.append("")
        continue

    write_chunk_context(
        lines,
        chunks,
        position,
    )


# ---------------------------------------------------------
# Resultado final
# ---------------------------------------------------------

final_chunks = chunk_corpus(
    corpus=corpus,
    size=300,
    overlap=60,
)

lines.append("## 7. Configuración seleccionada")
lines.append("")
lines.append("```text")
lines.append("chunk_size = 300")
lines.append("overlap = 60")
lines.append(f"chunks generados = {len(final_chunks)}")
lines.append("```")
lines.append("")

lines.append(
    "La configuración 300/60 fue seleccionada después de "
    "comparar distintos tamaños de chunk y distintos valores "
    "de overlap. Las pruebas incluyeron habilidades cortas, "
    "habilidades complejas, transiciones entre contenido y "
    "objetos del corpus."
)
lines.append("")
lines.append(
    "Esta configuración mostró un equilibrio adecuado entre "
    "preservación de contexto y fragmentación, evitando tanto "
    "chunks excesivamente pequeños como chunks que mezclaran "
    "demasiados conceptos diferentes."
)


OUTPUT_FILE.write_text(
    "\n".join(lines),
    encoding="utf-8",
)

print(
    f"Evidencia generada correctamente: {OUTPUT_FILE}"
)