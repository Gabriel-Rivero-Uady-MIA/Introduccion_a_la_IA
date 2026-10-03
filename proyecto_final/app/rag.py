from app.retrieve import Retrieved, retrieve
from app.store import ChromaStore
from app.generate import generate
import re
from dataclasses import dataclass

@dataclass(frozen=True)
class RAGAnswer:
    answer: str
    citations: list[int]
    abstained: bool
    retrieved: list[Retrieved]

def extract_citations(answer: str) -> list[int]:
    matches = re.findall(r"\[(\d+)\]", answer)
    return sorted({int(match) for match in matches})

def parse_model_response(response: str) -> tuple[bool, str]:
    lines = response.strip().splitlines()

    if len(lines) < 2:
        raise ValueError("Respuesta del modelo con formato inválido.")

    abstained_line = lines[0].strip()
    answer_line = lines[1].strip()

    if not abstained_line.startswith("ABSTAINED:"):
        raise ValueError("Falta el campo ABSTAINED.")

    if not answer_line.startswith("ANSWER:"):
        raise ValueError("Falta el campo ANSWER.")

    abstained_value = abstained_line.split(":", 1)[1].strip().lower()

    if abstained_value == "true":
        abstained = True
    elif abstained_value == "false":
        abstained = False
    else:
        raise ValueError("ABSTAINED debe ser true o false.")

    answer_parts = [
        answer_line.split(":", 1)[1].strip(),
        *lines[2:],
    ]

    answer = "\n".join(answer_parts).strip()

    return abstained, answer

def validate_citations(citations: list[int],retrieved: list[Retrieved],) -> bool:
    max_rank = len(retrieved)

    return all(
        1 <= citation <= max_rank
        for citation in citations
    )

def build_context(retrieved: list[Retrieved]) -> str:
    lines: list[str] = []

    for result in retrieved:
        lines.append(f"[{result.rank}]")
        lines.append(f"Fuente: {result.source}")
        lines.append(f"Texto: {result.text}")
        lines.append("")

    return "\n".join(lines).strip()


def build_prompt(question: str, context: str) -> str:
    return (
        "Sistema:\n"
        "Responde en español usando únicamente la información del contexto proporcionado.\n"
        "No añadas información externa ni conocimiento que no aparezca en el contexto.\n"
        "Cita cada afirmación relevante usando [n], donde n corresponde a una fuente del contexto.\n"
        "Usa únicamente números de fuente que existan en el contexto.\n"
        "Si el contexto no contiene evidencia suficiente para responder, indícalo claramente.\n"
        "Redacta la respuesta de forma natural, fluida y explicativa.\n"
        "No copies ni reproduzcas la estructura del contexto como una ficha o diccionario.\n"
        "Prioriza párrafos en prosa continua. Evita listas, viñetas, tablas o secciones salvo que sean necesarias para responder con claridad.\n"
        "Integra los datos relevantes en una explicación coherente, manteniendo las citas [n].\n"
        "Devuelve tu respuesta usando exactamente este formato:\n"
        "ABSTAINED: true o false\n"
        "ANSWER: texto de la respuesta\n"
        "Usa ABSTAINED: true únicamente si el contexto no contiene evidencia suficiente para responder.\n"
        "Si ABSTAINED: true, explica brevemente que no hay evidencia suficiente y no intentes completar la respuesta con conocimiento externo.\n"
        "Si ABSTAINED: false, responde normalmente y conserva las citas [n].\n\n"
        f"Contexto:\n{context}\n\n"
        f"Pregunta:\n{question}"
    )

def answer_question(question: str,retrieved: list[Retrieved],) -> RAGAnswer:
    if not retrieved:
        return RAGAnswer(
            answer=(
                "El corpus está vacío. No hay documentos indexados "
                "para responder consultas. Agrega documentos desde "
                "\"Administración del corpus\"."
            ),
            citations=[],
            abstained=True,
            retrieved=[],
        )
    context = build_context(retrieved)
    prompt = build_prompt(question, context)

    response = generate(prompt)

    abstained, answer = parse_model_response(response)

    citations = extract_citations(answer)

    if not validate_citations(citations, retrieved):
        raise ValueError("La respuesta contiene citas inexistentes.")

    if abstained:
        citations = []

    return RAGAnswer(
        answer=answer,
        citations=citations,
        abstained=abstained,
        retrieved=retrieved,
    )

def run_rag(question: str, store: ChromaStore, top_k: int = 5,) -> RAGAnswer:
    retrieved = retrieve(
        question=question,
        store=store,
        top_k=top_k,
    )

    return answer_question(
        question=question,
        retrieved=retrieved,
    )

