import os
import json

def buscar_respuesta_en_documentos(cliente_id: str, pregunta: str) -> str:
    ruta = f"documents/{cliente_id}"
    if not os.path.exists(ruta):
        raise Exception(f"No se encontraron documentos para el cliente {cliente_id}")

    # Convertir la pregunta a minúsculas para búsqueda case-insensitive
    pregunta_lower = pregunta.lower()
    
    # Palabras clave comunes
    palabras_clave = {
        'tasa': ['tasa', 'interés', 'interes', 'porcentaje', 'rendimiento'],
        'requisitos': ['requisito', 'requisitos', 'necesito', 'necesita', 'requiere'],
        'tiempo': ['tiempo', 'tiempos', 'duración', 'duracion', 'espera', 'respuesta'],
        'limite': ['limite', 'límite', 'máximo', 'maximo', 'mínimo', 'minimo', 'transferencia'],
        'seguridad': ['seguridad', 'protección', 'proteccion', 'autenticación', 'autenticacion'],
        'servicio': ['servicio', 'atención', 'atencion', 'soporte', 'ayuda']
    }

    # Función para buscar en el contenido
    def buscar_en_contenido(contenido: str, palabras_buscar: list) -> str:
        contenido_lower = contenido.lower()
        lineas_relevantes = []
        
        for linea in contenido.split('\n'):
            linea_lower = linea.lower()
            if any(palabra in linea_lower for palabra in palabras_buscar):
                lineas_relevantes.append(linea.strip())
        
        if lineas_relevantes:
            return ' | '.join(lineas_relevantes)
        return None

    # Buscar en archivos
    respuestas_encontradas = []
    
    for archivo in os.listdir(ruta):
        path = os.path.join(ruta, archivo)
        if archivo.endswith('.txt'):
            with open(path, 'r', encoding='utf-8') as f:
                contenido = f.read()
                
                # Buscar por palabras clave
                for tipo, palabras in palabras_clave.items():
                    if any(palabra in pregunta_lower for palabra in palabras):
                        respuesta = buscar_en_contenido(contenido, palabras)
                        if respuesta:
                            respuestas_encontradas.append(respuesta)

                # Búsqueda general si no se encontró por palabras clave
                if pregunta_lower in contenido.lower():
                    for linea in contenido.split('\n'):
                        if pregunta_lower in linea.lower():
                            respuestas_encontradas.append(linea.strip())

        elif archivo.endswith('.json'):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                json_str = json.dumps(data, ensure_ascii=False).lower()
                
                # Buscar por palabras clave en JSON
                for tipo, palabras in palabras_clave.items():
                    if any(palabra in pregunta_lower for palabra in palabras):
                        for key, value in data.items():
                            if any(palabra in str(value).lower() for palabra in palabras):
                                respuestas_encontradas.append(f"{key}: {value}")

                # Búsqueda general en JSON
                if pregunta_lower in json_str:
                    for key, value in data.items():
                        if pregunta_lower in str(value).lower():
                            respuestas_encontradas.append(f"{key}: {value}")

    if respuestas_encontradas:
        # Si hay múltiples respuestas, las unimos
        return ' | '.join(respuestas_encontradas)
    
    return "No se encontró una respuesta específica en los documentos disponibles."
