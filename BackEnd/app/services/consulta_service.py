import time
from app.utils.document_loader import buscar_respuesta_en_documentos

def procesar_consulta(cliente_id: str, pregunta: str) -> str:
    # Simulación de procesamiento con modelo de lenguaje (GPT, etc.)
    time.sleep(1.5)  # Simula latencia de modelo externo
    respuesta = buscar_respuesta_en_documentos(cliente_id, pregunta)
    return respuesta
