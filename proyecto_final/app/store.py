import chromadb


class ChromaStore:
    def __init__(self, path: str, collection_name: str) -> None:
        self.path = path
        self.collection_name = collection_name

        self.client = chromadb.PersistentClient(path=self.path)

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )

    def reset_collection(self) -> None:
        try:
            self.client.delete_collection(
                name=self.collection_name
            )
        except Exception:
            pass

        self.collection = self.client.create_collection(
            name=self.collection_name
        )

    def add(
        self,
        ids: list[str],
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, str | int]],
    ) -> None:
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def count(self) -> int:
        return self.collection.count()

    def get(
        self,
        ids: list[str] | None = None,
    ) -> dict:
        return self.collection.get(
            ids=ids
        )

    def query(
        self,
        query_embedding: list[float],
        n_results: int,
    ) -> dict:
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
            include=["documents", "metadatas", "distances"],
        )

