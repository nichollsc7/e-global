from dataclasses import dataclass
from typing import Optional

@dataclass
class Consulta:
    """Entidad que representa una consulta en el sistema."""
    cliente_id: str
    pregunta: str
    respuesta: Optional[str] = None

    def __post_init__(self):
        """Validaciones básicas de la entidad."""
        if not self.cliente_id:
            raise ValueError("El ID del cliente es requerido")
        if not self.pregunta:
            raise ValueError("La pregunta es requerida") 