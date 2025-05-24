import json
import os
from typing import List, Optional
from src.domain.ports.document_repository import DocumentRepository

class DocumentRepositoryImpl(DocumentRepository):
    """Implementación del repositorio de documentos."""

    def __init__(self, base_path: str = "documents"):
        """
        Inicializa el repositorio.
        
        Args:
            base_path: Ruta base donde se encuentran los documentos
        """
        self.base_path = base_path

    def buscar_en_documentos(self, cliente_id: str, pregunta: str) -> Optional[str]:
        """
        Busca una respuesta en los documentos del cliente.
        
        Args:
            cliente_id: Identificador del cliente
            pregunta: Pregunta a buscar en los documentos
            
        Returns:
            str: Respuesta encontrada o None si no se encuentra
        """
        documentos = self.obtener_documentos_cliente(cliente_id)
        if not documentos:
            return None

        # Palabras clave para búsqueda
        keywords = {
            'tasas': ['tasa', 'interés', 'rendimiento'],
            'límites': ['límite', 'máximo', 'transferencia'],
            'requisitos': ['requisito', 'contraseña', 'seguridad'],
            'tiempos': ['tiempo', 'respuesta', 'urgencia']
        }

        # Buscar en cada documento
        for doc_path in documentos:
            if doc_path.endswith('.txt'):
                respuesta = self._buscar_en_txt(doc_path, pregunta, keywords)
            elif doc_path.endswith('.json'):
                respuesta = self._buscar_en_json(doc_path, pregunta, keywords)
            
            if respuesta:
                return respuesta

        return None

    def obtener_documentos_cliente(self, cliente_id: str) -> List[str]:
        """
        Obtiene la lista de documentos disponibles para un cliente.
        
        Args:
            cliente_id: Identificador del cliente
            
        Returns:
            List[str]: Lista de rutas de documentos
        """
        cliente_path = os.path.join(self.base_path, cliente_id)
        if not os.path.exists(cliente_path):
            return []

        documentos = []
        for archivo in os.listdir(cliente_path):
            if archivo.endswith(('.txt', '.json')):
                documentos.append(os.path.join(cliente_path, archivo))
        
        return documentos

    def _buscar_en_txt(self, doc_path: str, pregunta: str, keywords: dict) -> Optional[str]:
        """Busca en archivos de texto."""
        try:
            with open(doc_path, 'r', encoding='utf-8') as f:
                contenido = f.read()
                
            # Buscar palabras clave en el contenido
            for categoria, palabras in keywords.items():
                if any(palabra in pregunta.lower() for palabra in palabras):
                    # Buscar líneas relevantes
                    lineas = contenido.split('\n')
                    for linea in lineas:
                        if any(palabra in linea.lower() for palabra in palabras):
                            return linea.strip()
        except Exception:
            return None
        return None

    def _buscar_en_json(self, doc_path: str, pregunta: str, keywords: dict) -> Optional[str]:
        """Busca en archivos JSON."""
        try:
            with open(doc_path, 'r', encoding='utf-8') as f:
                datos = json.load(f)
                
            # Buscar en el JSON
            for categoria, palabras in keywords.items():
                if any(palabra in pregunta.lower() for palabra in palabras):
                    # Buscar en las claves del JSON
                    for clave, valor in datos.items():
                        if any(palabra in clave.lower() for palabra in palabras):
                            if isinstance(valor, (str, int, float)):
                                return str(valor)
                            elif isinstance(valor, dict):
                                return json.dumps(valor, ensure_ascii=False)
        except Exception:
            return None
        return None 