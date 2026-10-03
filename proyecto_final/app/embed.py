import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


MODEL = "gemini-embedding-2"
EMBEDDING_DIM = 768


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError(
        "No se encontró GOOGLE_API_KEY en el archivo .env"
    )

client = genai.Client(api_key=api_key)

def embed(text: str) -> list[float]:


    if not text.strip():
        raise ValueError("El texto no puede estar vacío.")

    response = client.models.embed_content(
        model=MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            output_dimensionality=EMBEDDING_DIM
        ),
    )

    vector = response.embeddings[0].values

    return list(vector)


def embed_many(texts: list[str]) -> list[list[float]]:
    if not texts:
        raise ValueError("La lista de textos no puede estar vacía.")

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=text)]
        )
        for text in texts
    ]

    response = client.models.embed_content(
        model=MODEL,
        contents=contents,
        config=types.EmbedContentConfig(
            output_dimensionality=EMBEDDING_DIM
        ),
    )

    vectors = [
        list(embedding.values)
        for embedding in response.embeddings
    ]

    return vectors