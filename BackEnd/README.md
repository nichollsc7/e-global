# Sistema de Consulta Inteligente

## 📋 Descripción General
Sistema de consulta inteligente que permite acceder a información específica de cada cliente mediante procesamiento de lenguaje natural. Implementado con FastAPI y React, utilizando arquitectura hexagonal para garantizar escalabilidad y mantenibilidad.

## 🎯 Características Principales
- Búsqueda semántica en documentos
- Soporte multi-cliente
- Respuestas precisas y contextuales
- Procesamiento en tiempo real
- Integración real con LangChain y Google Gemini (API Key de Google AI Studio, sin costo)
- Soporte para archivos .txt y .json

## 🏗️ Arquitectura
El sistema está implementado siguiendo la arquitectura hexagonal (ports and adapters):

```
BackEnd/
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   └── utils/
├── documents/
├── requirements.txt
├── README.md
├── .env.example
```

## 🤖 Integración RAG+LLM Real con LangChain y Google Gemini (API Key de Google AI Studio)
El sistema utiliza un pipeline real de Recuperación Aumentada por Generación (RAG) con LangChain y Google Gemini (API Key gratuita de Google AI Studio):

- Recupera fragmentos relevantes de los documentos del cliente
- Usa búsqueda simple por coincidencia de palabras para simular RAG
- Genera la respuesta final usando un modelo LLM real (Gemini) a través de LangChain y Google AI Studio
- Sin costos de Vertex AI, ideal para pruebas y prototipos
- **Actualmente se utiliza el modelo `gemini-2.0-flash-lite`, que permite hasta 30 requests por minuto gratis**

### Instalación de dependencias

```bash
pip install langchain langchain-google-genai faiss-cpu tiktoken python-dotenv
```

### Configuración de la API Key de Google AI Studio

1. Ve a https://aistudio.google.com/app/apikey y genera tu API Key gratuita.
2. Renombra el archivo `.env.example` a `.env`.
3. Agrega tu API Key en el archivo `.env` así:
   ```
   GOOGLE_API_KEY=tu_api_key_de_ai_studio
   ```
4. **Nota:** El archivo `.env` está en el `.gitignore` y **no se sube al repositorio**. Cada evaluador debe generar y agregar su propia API Key.

## ⚠️ Advertencia sobre límites de la API Key gratuita
- La API Key gratuita de Google AI Studio tiene **límites** de uso (tokens y solicitudes por minuto y por día).
- El modelo `gemini-2.0-flash-lite` permite hasta **30 requests por minuto gratis**.
- Si haces muchas pruebas seguidas, puedes recibir errores 429 (Too Many Requests) como:
  ```
  429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.
  ```
- **Solución:** Espera unos minutos y vuelve a probar. Los límites se reinician cada minuto y cada día.
- No es posible aumentar el límite en la API Key gratuita. Si necesitas más capacidad, solo es posible con una cuenta de Google Cloud y Vertex AI (de pago).
- Consulta los límites oficiales aquí: [https://ai.google.dev/gemini-api/docs/rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits)

## 📄 Soporte de Documentos
El sistema soporta búsqueda en documentos con:

- Archivos `.txt` y `.json`
- Estructura de documentos por cliente
- Búsqueda semántica en contenido (simulada)
- Respuestas contextuales basadas en el tipo de documento

### Ejemplo de Estructura de Documentos
```json
{
    "cliente1": {
        "cuentas.txt": [
            "Tasa de interés: 2.5% anual",
            "Saldo mínimo: $1,000"
        ],
        "tarjetas.json": {
            "límites": ["$5,000", "$10,000"],
            "beneficios": ["Cashback 2%"]
        }
    }
}
```

## 👥 Clientes Disponibles

### 1️⃣ Cliente 1 - Productos Financieros
| Categoría | Temas Disponibles |
|-----------|-------------------|
| 💰 Cuentas | Tasas de interés, saldos mínimos, beneficios |
| 💳 Tarjetas | Límites, beneficios, requisitos |
| 📊 Préstamos | Tasas, plazos, requisitos |
| 📈 Inversiones | Certificados, rendimientos |
| 💸 Transferencias | Límites diarios y mensuales |
| 🏦 Servicios | Banca en línea, móvil |

### 2️⃣ Cliente 2 - Seguridad y Privacidad
| Categoría | Temas Disponibles |
|-----------|-------------------|
| 🔒 Seguridad | Políticas, protocolos, estándares |
| 🔑 Acceso | Contraseñas, autenticación |
| 📊 Auditoría | Monitoreo, registros |
| 🛡️ Protección | Datos, transacciones |
| ⚖️ Límites | Operaciones, transferencias |
| 📱 Dispositivos | Móvil, token |

### 3️⃣ Cliente 3 - Atención al Cliente
| Categoría | Temas Disponibles |
|-----------|-------------------|
| 📞 Canales | Teléfono, chat, email, redes |
| ⏱️ Tiempos | Respuesta, resolución |
| 🎯 SLA | Métricas, objetivos |
| 📊 Soporte | Niveles, especialistas |
| ⚙️ Operaciones | Límites, procesos |
| 📝 Reclamos | Procesos, seguimiento |

## 📝 Ejemplos de Consultas

### 💰 Consultas Financieras (Cliente 1)
```json
{
    "cliente_id": "cliente1",
    "pregunta": "¿Cuál es la tasa de interés de la cuenta de ahorros?"
}
```
**Respuesta:**
```json
{
    "respuesta": "Tasa de interés: 2.5% anual"
}
```

### 🔒 Consultas de Seguridad (Cliente 2)
```json
{
    "cliente_id": "cliente2",
    "pregunta": "¿Cuáles son los requisitos de contraseña?"
}
```
**Respuesta:**
```json
{
    "respuesta": "Longitud mínima: 12 caracteres, requiere mayúsculas, números y caracteres especiales"
}
```

## ⚙️ Notas Técnicas
- Pipeline RAG+LLM real con LangChain y Google Gemini (API Key de Google AI Studio)
- Búsqueda semántica simulada (por coincidencia de palabras)
- 📄 Formatos soportados: .txt y .json
- 🔄 Consultas flexibles entre clientes
- 📊 Respuestas consistentes en límites
- 🔍 Búsqueda semántica básica
- Sin costos de Vertex AI
- **Modelo usado: `gemini-2.0-flash-lite` (30 requests por minuto gratis)**

## 🚀 Códigos de Respuesta
| Código | Descripción |
|--------|-------------|
| 200 | ✅ Consulta exitosa |
| 400 | ❌ Error en la consulta |

## 📌 Consideraciones
- Los IDs de cliente deben coincidir exactamente con los nombres de las carpetas
- Las consultas son case-insensitive
- Se soportan preguntas en lenguaje natural
- Las respuestas son contextuales al cliente