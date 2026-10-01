import os

from fastapi import FastAPI, HTTPException, UploadFile
from pydantic import BaseModel, Field

from app.data import Corpus, Document
from app.ingest import ingest_corpus
from app.rag import run_rag
from app.store import ChromaStore


CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    "chroma_db",
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "lol_corpus_26_19",
)


app = FastAPI()
app.openapi_version = "3.0.2"


class QueryRequest(BaseModel):
    question: str
    top_k: int = Field(default=5, ge=1)


query_store = ChromaStore(
    path=CHROMA_PATH,
    collection_name=COLLECTION_NAME,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/ingest")
async def ingest(
    files: list[UploadFile],
) -> dict[str, int]:
    if not files:
        raise HTTPException(
            status_code=400,
            detail="No se recibieron documentos.",
        )

    documents: list[Document] = []

    for file in files:
        filename = file.filename

        if not filename:
            raise HTTPException(
                status_code=400,
                detail="Se recibió un archivo sin nombre.",
            )

        extension = os.path.splitext(filename)[1].lower()

        if extension not in {".md", ".txt"}:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Tipo de archivo no soportado: "
                    f"{filename}"
                ),
            )

        content = await file.read()

        try:
            text = content.decode("utf-8").strip()

        except UnicodeDecodeError:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"El archivo {filename} "
                    "no es texto UTF-8 válido."
                ),
            )

        if not text:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"El archivo {filename} está vacío."
                ),
            )

        documents.append(
            Document(
                title=os.path.splitext(filename)[0],
                source=filename,
                text=text,
            )
        )

    corpus = Corpus(
        name="Uploaded corpus",
        documents=tuple(documents),
    )

    store = ChromaStore(
        path=CHROMA_PATH,
        collection_name=COLLECTION_NAME,
    )

    result = ingest_corpus(
        corpus=corpus,
        store=store,
    )

    return result


@app.post("/query")
def query(request: QueryRequest) -> dict:
    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="La pregunta no puede estar vacía.",
        )

    result = run_rag(
        question=question,
        store=query_store,
        top_k=request.top_k,
    )

    return {
        "answer": result.answer,
        "citations": result.citations,
        "abstained": result.abstained,
        "retrieved": [
            {
                "rank": item.rank,
                "id": item.id,
                "source": item.source,
                "doc_title": item.doc_title,
                "index": item.index,
                "text": item.text,
                "distance": item.distance,
            }
            for item in result.retrieved
        ],
    }