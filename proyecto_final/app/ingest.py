import time

from app.data import Corpus
from app.chunk import chunk_corpus
from app.embed import embed_many, EMBEDDING_DIM
from app.store import ChromaStore


CHUNK_WORDS = 300
OVERLAP = 60

BATCH_SIZE = 25
BATCH_DELAY_SECONDS = 1


def prepare_chroma_data(corpus: Corpus,) -> tuple[list,list[str],list[str],list[dict[str, str | int]],]:
    chunks = chunk_corpus(corpus,size=CHUNK_WORDS,overlap=OVERLAP,)

    ids: list[str] = []
    documents: list[str] = []
    metadatas: list[dict[str, str | int]] = []

    for chunk in chunks:
        ids.append(
            f"{chunk.source}::chunk_{chunk.index}"
        )

        documents.append(
            chunk.text
        )

        metadatas.append(
            {
                "doc_title": chunk.doc_title,
                "source": chunk.source,
                "index": chunk.index,
            }
        )

    return chunks, ids, documents, metadatas


def ingest_corpus(corpus: Corpus, store: ChromaStore,) -> dict[str, int]:
    chunks, ids, documents, metadatas = prepare_chroma_data(
        corpus
    )

    total_chunks = len(chunks)

    if not (
        len(chunks)
        == len(ids)
        == len(documents)
        == len(metadatas)
    ):
        raise RuntimeError(
            "Las cantidades de chunks, IDs, documents "
            "y metadatas no coinciden."
        )

    if len(set(ids)) != len(ids):
        raise RuntimeError(
            "Se encontraron IDs duplicados."
        )

    existing_data = store.get(ids=ids)
    existing_ids = set(existing_data["ids"])

    missing_indexes = [
        index
        for index, chunk_id in enumerate(ids)
        if chunk_id not in existing_ids
    ]

    print("Documentos:", len(corpus.documents))
    print("Chunks:", total_chunks)
    print("Chunks ya existentes:", len(existing_ids))
    print("Chunks pendientes:", len(missing_indexes))

    if not missing_indexes:
        print("Todos los chunks ya existen en Chroma.")

        return {
            "documents": len(corpus.documents),
            "chunks": total_chunks,
            "chunks_indexed": 0,
            "total_records": store.count(),
        }

    total_batches = (
        len(missing_indexes) + BATCH_SIZE - 1
    ) // BATCH_SIZE

    indexed = 0

    for batch_start in range(
        0,
        len(missing_indexes),
        BATCH_SIZE,
    ):
        batch_indexes = missing_indexes[
            batch_start : batch_start + BATCH_SIZE
        ]

        batch_number = (
            batch_start // BATCH_SIZE
        ) + 1

        batch_ids = [
            ids[index]
            for index in batch_indexes
        ]

        batch_documents = [
            documents[index]
            for index in batch_indexes
        ]

        batch_metadatas = [
            metadatas[index]
            for index in batch_indexes
        ]

        print()
        print(
            f"Batch {batch_number}/{total_batches}"
        )

        try:
            batch_embeddings = embed_many(
                batch_documents
            )

        except Exception:
            print()
            print(
                f"Error generando embeddings "
                f"en batch {batch_number}."
            )
            print(
                "Los registros ya guardados en "
                "Chroma se conservan."
            )
            print(
                "Registros actualmente persistidos:",
                store.count(),
            )
            raise

        if len(batch_embeddings) != len(batch_documents):
            raise RuntimeError(
                f"Batch {batch_number}: "
                "la cantidad de embeddings no coincide "
                "con la cantidad de textos."
            )

        if any(
            len(vector) != EMBEDDING_DIM
            for vector in batch_embeddings
        ):
            raise RuntimeError(
                f"Batch {batch_number}: "
                "se encontró un embedding con dimensión "
                f"distinta de {EMBEDDING_DIM}."
            )

        try:
            store.add(
                ids=batch_ids,
                documents=batch_documents,
                embeddings=batch_embeddings,
                metadatas=batch_metadatas,
            )

        except Exception:
            print()
            print(
                f"Error guardando batch "
                f"{batch_number} en Chroma."
            )
            print(
                "Registros actualmente persistidos:",
                store.count(),
            )
            raise

        indexed += len(batch_documents)

        print(
            "Embeddings recibidos:",
            len(batch_embeddings),
        )

        print(
            "Chunks indexados en esta ejecución:",
            indexed,
        )

        print(
            "Registros en Chroma:",
            store.count(),
        )

        if batch_number < total_batches:
            print(
                f"Esperando {BATCH_DELAY_SECONDS} segundos "
                "para respetar TPM..."
            )

            time.sleep(
                BATCH_DELAY_SECONDS
            )

    return {
        "documents": len(corpus.documents),
        "chunks": total_chunks,
        "chunks_indexed": indexed,
        "total_records": store.count(),
    }
