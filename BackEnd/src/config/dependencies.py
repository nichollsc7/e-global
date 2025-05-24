from src.adapters.secondary.document_loader.document_repository_impl import DocumentRepositoryImpl
from src.domain.ports.document_repository import DocumentRepository
from src.domain.use_cases.procesar_consulta import ProcesarConsultaUseCase

def get_document_repository() -> DocumentRepository:
    return DocumentRepositoryImpl()

def get_procesar_consulta_use_case() -> ProcesarConsultaUseCase:
    return ProcesarConsultaUseCase(get_document_repository()) 