import os

from dotenv import load_dotenv
from google import genai


MODEL = "gemini-3.8-flash"


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise RuntimeError(
        "No se encontró GOOGLE_API_KEY en el archivo .env"
    )

client = genai.Client(api_key=api_key)


def generate(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    text = response.text

    if not text:
        raise RuntimeError("Gemini devolvió una respuesta vacía.")

    return text