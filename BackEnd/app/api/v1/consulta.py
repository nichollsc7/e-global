# api/v1/consulta.py
from fastapi import APIRouter, HTTPException
from app.models.request import ConsultaRequest
from app.services.consulta_service import procesar_consulta

router = APIRouter()

@router.post("/consulta",
    summary="API de Consulta Inteligente",
    description="""
    Sistema de consulta inteligente que procesa preguntas sobre documentos específicos por cliente. Implementado con FastAPI y React, utilizando arquitectura hexagonal para garantizar escalabilidad y mantenibilidad. Incluye simulación de modelo LLM y búsqueda semántica en documentos.

    ## 📋 Descripción General
    Sistema de consulta inteligente que permite acceder a información específica de cada cliente mediante procesamiento de lenguaje natural.

    ## 🎯 Características Principales
    - Búsqueda semántica en documentos
    - Soporte multi-cliente
    - Respuestas precisas y contextuales
    - Procesamiento en tiempo real

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

    ### 📞 Consultas de Atención (Cliente 3)
    ```json
    {
        "cliente_id": "cliente3",
        "pregunta": "¿Cuáles son los tiempos de respuesta para urgencia alta?"
    }
    ```
    **Respuesta:**
    ```json
    {
        "respuesta": "Urgencia Alta: 1 hora"
    }
    ```

    ## ⚙️ Notas Técnicas
    - ⏱️ Delay de simulación: 1.5 segundos
    - 📄 Formatos soportados: .txt y .json
    - 🔄 Consultas flexibles entre clientes
    - 📊 Respuestas consistentes en límites
    - 🔍 Búsqueda semántica avanzada

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
    """,
    response_description="Respuesta basada en los documentos del cliente",
    responses={
        200: {
            "description": "✅ Consulta procesada exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "respuesta": "Tasa de interés: 2.5% anual"
                    }
                }
            }
        },
        400: {
            "description": "❌ Error en la consulta",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "No se encontraron documentos para el cliente cliente1"
                    }
                }
            }
        }
    }
)
async def consulta(data: ConsultaRequest):
    try:
        respuesta = procesar_consulta(data.cliente_id, data.pregunta)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
