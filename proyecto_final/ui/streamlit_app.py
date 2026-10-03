import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv( "API_BASE_URL", "http://127.0.0.1:8000",).rstrip("/")

st.title("LoL Knowledge & Patch Assistant")

st.write(
    "Consulta información del corpus de League of Legends "
    "a través del backend FastAPI."
)


def check_api_health() -> bool:
    try:
        response = requests.get(
            f"{API_BASE_URL}/health",
            timeout=5,
        )

        return response.status_code == 200

    except requests.RequestException:
        return False

def ingest_api(uploaded_files):
    files = [
        (
            "files",
            (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type or "text/plain",
            ),
        )
        for uploaded_file in uploaded_files
    ]

    return requests.post(
        f"{API_BASE_URL}/ingest",
        files=files,
        timeout=120,
    )

api_available = check_api_health()
google_api_key = os.getenv("GOOGLE_API_KEY")

if api_available:
    st.success("API disponible.")
elif not google_api_key:
    st.error(
        "No se encontró GOOGLE_API_KEY. "
        "Configura la clave en el archivo .env antes de iniciar FastAPI."
    )
else:
    st.error("No se pudo conectar con la API.")


query_tab, admin_tab = st.tabs(
    [
        "Consulta",
        "Administración del corpus",
    ]
)


with query_tab:
    question = st.text_input("Pregunta")

    top_k = st.number_input(
        "top_k",
        min_value=1,
        value=5,
        step=1,
    )

    if st.button("Consultar"):
        question = question.strip()

        if not question:
            st.warning("La pregunta no puede estar vacía.")

        elif not api_available:
            st.error("No se pudo conectar con la API.")

        else:
            payload = {
                "question": question,
                "top_k": int(top_k),
            }

            try:
                with st.spinner("Consultando..."):
                    response = requests.post(
                        f"{API_BASE_URL}/query",
                        json=payload,
                        timeout=60,
                    )

                if response.status_code == 200:
                    result = response.json()

                    st.subheader("Respuesta")

                    if result["abstained"]:
                        st.warning(result["answer"])
                    else:
                        st.write(result["answer"])

                    st.subheader("Citas utilizadas")

                    citations = result["citations"]

                    if citations:
                        st.write(
                            ", ".join(
                                f"[{citation}]"
                                for citation in citations
                            )
                        )
                    else:
                        st.write("Sin citas.")

                    st.subheader("Evidencia recuperada")

                    for item in result["retrieved"]:
                        rank = item["rank"]
                        source = item["source"]
                        distance = item["distance"]

                        cited = rank in citations

                        label = (
                            f"[{rank}] {source} — "
                            f"distance {distance:.4f}"
                        )

                        if cited:
                            label += " — Citado"

                        with st.expander(label):
                            st.write(item["text"])

                            st.caption(
                                f"doc_title: {item['doc_title']} | "
                                f"index: {item['index']} | "
                                f"id: {item['id']}"
                            )

                elif response.status_code == 400:
                    detail = response.json().get(
                        "detail",
                        "Solicitud inválida.",
                    )
                    st.warning(detail)

                else:
                    st.error(
                        f"Error del servidor: "
                        f"HTTP {response.status_code}"
                    )

            except requests.Timeout:
                st.error(
                    "La consulta tardó demasiado en responder."
                )

            except requests.RequestException:
                st.error("No se pudo conectar con la API.")


with admin_tab:
    st.subheader("Administración del corpus")

    st.write(
        "Esta sección permite agregar documentos al índice "
        "del RAG y está destinada al mantenimiento del "
        "conocimiento del sistema."
    )

    st.info(
        "Los documentos ingeridos se incorporan a la "
        "base de conocimiento."
    )

    uploaded_files = st.file_uploader(
        "Selecciona documentos",
        type=["md", "txt"],
        accept_multiple_files=True,
    )

    if uploaded_files:
        st.write(
            f"Archivos seleccionados: {len(uploaded_files)}"
        )

        for uploaded_file in uploaded_files:
            st.write(
                f"- {uploaded_file.name} "
                f"({uploaded_file.type or 'tipo no informado'}, "
                f"{uploaded_file.size} bytes)"
            )
    else:
        st.caption("No hay archivos seleccionados.")
    
    if st.button("Ingerir documentos"):
        if not uploaded_files:
            st.warning("Selecciona al menos un archivo.")
    
        elif not api_available:
            st.error("No se pudo conectar con la API.")
    
        else:
            try:
                with st.spinner("Ingeriendo documentos..."):
                    response = ingest_api(uploaded_files)
    
                if response.status_code == 200:
                    result = response.json()
                
                    st.success("Ingestión completada.")
                
                    col1, col2 = st.columns(2)
                
                    with col1:
                        st.metric(
                            "Documentos procesados",
                            result["documents"],
                        )
                
                        st.metric(
                            "Chunks nuevos indexados",
                            result["chunks_indexed"],
                        )
                
                    with col2:
                        st.metric(
                            "Chunks detectados",
                            result["chunks"],
                        )
                
                        st.metric(
                            "Total en colección",
                            result["total_records"],
                        )
    
                elif response.status_code == 400:
                    detail = response.json().get(
                        "detail",
                        "Solicitud inválida.",
                    )
                    st.warning(detail)
    
                else:
                    st.error(
                        f"Error del servidor: "
                        f"HTTP {response.status_code}"
                    )
    
            except requests.Timeout:
                st.error(
                    "La ingestión tardó demasiado en responder."
                )
    
            except requests.RequestException:
                st.error("No se pudo conectar con la API.")