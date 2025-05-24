from typing import Optional
from src.domain.entities.consulta import Consulta
from src.domain.ports.document_repository import DocumentRepository

class ProcesarConsultaUseCase:
    """Caso de uso para procesar consultas de clientes."""

    def __init__(self, document_repository: DocumentRepository):
        """
        Inicializa el caso de uso.
        
        Args:
            document_repository: Implementación del repositorio de documentos
        """
        self.document_repository = document_repository

    def ejecutar(self, cliente_id: str, pregunta: str) -> Consulta:
        """
        Ejecuta el caso de uso de procesamiento de consulta.
        
        Args:
            cliente_id: Identificador del cliente
            pregunta: Pregunta a procesar
            
        Returns:
            Consulta: Entidad de consulta con la respuesta
        """
        # Crear la entidad de consulta
        consulta = Consulta(cliente_id=cliente_id, pregunta=pregunta)
        
        # Buscar la respuesta en los documentos
        respuesta = self.document_repository.buscar_en_documentos(
            cliente_id=cliente_id,
            pregunta=pregunta
        )
        
        # Asignar la respuesta a la consulta
        consulta.respuesta = respuesta
        
        return consulta 