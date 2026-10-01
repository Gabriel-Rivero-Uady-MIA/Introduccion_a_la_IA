from dataclasses import dataclass

from app.embed import embed
from app.store import ChromaStore


@dataclass(frozen=True)
class Retrieved:
    rank: int
    id: str
    source: str
    doc_title: str
    index: int
    text: str
    distance: float


def retrieve(
    question: str,
    store: ChromaStore,
    top_k: int,
) -> list[Retrieved]:
    query_embedding = embed(question)

    results = store.query(
        query_embedding=query_embedding,
        n_results=top_k,
    )

    retrieved: list[Retrieved] = []

    for i in range(len(results["ids"][0])):
        metadata = results["metadatas"][0][i]

        retrieved.append(
            Retrieved(
                rank=i + 1,
                id=results["ids"][0][i],
                source=metadata["source"],
                doc_title=metadata["doc_title"],
                index=metadata["index"],
                text=results["documents"][0][i],
                distance=results["distances"][0][i],
            )
        )

    return retrieved