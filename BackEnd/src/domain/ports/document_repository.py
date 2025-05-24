from abc import ABC, abstractmethod
from typing import List, Optional

class DocumentRepository(ABC):
    """Puerto para el repositorio de documentos."""

    @abstractmethod
    def buscar_en_documentos(self, cliente_id: str, pregunta: str) -> Optional[str]:
        """
        Busca una respuesta en los documentos del cliente.
        
        Args:
            cliente_id: Identificador del cliente
            pregunta: Pregunta a buscar en los documentos
            
        Returns:
            str: Respuesta encontrada o None si no se encuentra
        """
        pass

    @abstractmethod
    def obtener_documentos_cliente(self, cliente_id: str) -> List[str]:
        """
        Obtiene la lista de documentos disponibles para un cliente.
        
        Args:
            cliente_id: Identificador del cliente
            
        Returns:
            List[str]: Lista de rutas de documentos
        """
        pass 