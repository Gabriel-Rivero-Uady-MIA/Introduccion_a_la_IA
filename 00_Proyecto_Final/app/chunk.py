"""Split each document into overlapping chunks of whole words."""

from __future__ import annotations

from dataclasses import dataclass

from app.data import Corpus


@dataclass(frozen=True)
class Chunk:
    id: int
    doc_title: str
    source: str
    index: int
    text: str

    @property
    def word_count(self) -> int:
        return len(self.text.split())


def _windows(words: list[str], size: int, overlap: int) -> list[list[str]]:
    if size < 1:
        raise ValueError("size must be >= 1")

    if overlap < 0 or overlap >= size:
        raise ValueError("overlap must satisfy 0 <= overlap < size")

    if len(words) <= size:
        return [words]

    step = size - overlap
    windows: list[list[str]] = []
    i = 0

    while i < len(words):
        windows.append(words[i : i + size])

        if i + size >= len(words):
            break

        i += step

    return windows


def chunk_corpus(corpus: Corpus, size: int, overlap: int) -> list[Chunk]:
    chunks: list[Chunk] = []
    cid = 0

    for doc in corpus.documents:
        words = doc.text.split()

        for index, window in enumerate(_windows(words, size, overlap)):
            chunks.append(
                Chunk(
                    id=cid,
                    doc_title=doc.title,
                    source=doc.source,
                    index=index,
                    text=" ".join(window),
                )
            )

            cid += 1

    return chunks