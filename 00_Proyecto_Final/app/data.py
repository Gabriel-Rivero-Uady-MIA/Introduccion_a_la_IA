"""Load the League of Legends corpus from Markdown files."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Document:
    title: str
    source: str
    text: str


@dataclass(frozen=True)
class Corpus:
    name: str
    documents: tuple[Document, ...]


def load_corpus(data_dir: str | Path) -> Corpus:
    data_dir = Path(data_dir)

    documents: list[Document] = []

    for file_path in sorted(data_dir.glob("*.md")):
        text = file_path.read_text(encoding="utf-8").strip()

        if not text:
            raise ValueError(f"{file_path.name} is empty")

        documents.append(
            Document(
                title=file_path.stem,
                source=file_path.name,
                text=text,
            )
        )

    if not documents:
        raise ValueError("No Markdown files found")

    return Corpus(
        name="LoL Knowledge & Patch Assistant",
        documents=tuple(documents),
    )