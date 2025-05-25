import time
from app.utils.document_loader import consulta_gemini_studio

def procesar_consulta(cliente_id: str, pregunta: str) -> str:
    # Llama al pipeline RAG+LLM real
    respuesta = consulta_gemini_studio(cliente_id, pregunta)
    return respuesta
