# models/request.py
from pydantic import BaseModel, Field, validator
from typing import Literal

class ConsultaRequest(BaseModel):
    cliente_id: str = Field(
        ...,
        description="ID del cliente (cliente1, cliente2, cliente3)",
        example="cliente1"
    )
    pregunta: str = Field(
        ...,
        description="Pregunta a consultar en los documentos del cliente",
        example="¿Cuál es la tasa de interés de la cuenta de ahorros?"
    )

    @validator('cliente_id')
    def validate_cliente_id(cls, v):
        clientes_validos = ['cliente1', 'cliente2', 'cliente3']
        if v not in clientes_validos:
            raise ValueError(f"El cliente_id debe ser uno de: {', '.join(clientes_validos)}")
        return v

    class Config:
        schema_extra = {
            "example": {
                "cliente_id": "cliente1",
                "pregunta": "¿Cuál es la tasa de interés de la cuenta de ahorros?"
            }
        }
