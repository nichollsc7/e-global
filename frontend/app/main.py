from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import json
from datetime import datetime

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular por defecto
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Consulta(BaseModel):
    cliente_id: str
    pregunta: str

class Respuesta(BaseModel):
    respuesta: str
    documento_fuente: Optional[str] = None
    timestamp: str

# Simulación de documentos por cliente
DOCUMENTOS = {
    "cliente1": {
        "doc1.txt": "Este es un documento de ejemplo para el cliente 1.",
        "doc2.txt": "Información adicional para el cliente 1."
    },
    "cliente2": {
        "doc1.txt": "Documento específico para el cliente 2.",
        "doc2.txt": "Más información para el cliente 2."
    },
    "cliente3": {
        "doc1.txt": "Contenido exclusivo para el cliente 3.",
        "doc2.txt": "Datos adicionales del cliente 3."
    }
}

@app.post("/api/v1/consulta", response_model=Respuesta)
async def consultar(consulta: Consulta):
    # Validar cliente
    if consulta.cliente_id not in DOCUMENTOS:
        raise HTTPException(status_code=400, detail="Cliente no válido")
    
    # Simular búsqueda en documentos
    documentos_cliente = DOCUMENTOS[consulta.cliente_id]
    respuesta = ""
    documento_fuente = None
    
    # Simular búsqueda simple
    for doc_name, content in documentos_cliente.items():
        if consulta.pregunta.lower() in content.lower():
            respuesta = content
            documento_fuente = doc_name
            break
    
    if not respuesta:
        respuesta = "Lo siento, no encontré información relevante para tu consulta."
        documento_fuente = None
    
    return Respuesta(
        respuesta=respuesta,
        documento_fuente=documento_fuente,
        timestamp=datetime.now().isoformat()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 