from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from src.domain.use_cases.procesar_consulta import ProcesarConsultaUseCase
from src.config.dependencies import get_procesar_consulta_use_case

router = APIRouter()

class ConsultaRequest(BaseModel):
    """Modelo de solicitud de consulta."""
    cliente_id: str
    pregunta: str

class ConsultaResponse(BaseModel):
    """Modelo de respuesta de consulta."""
    respuesta: str

@router.post("/consulta",
    summary="Sistema de Consulta Inteligente",
    description="""
    # 📚 Sistema de Consulta Inteligente

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
    """,
    response_model=ConsultaResponse
)
async def consulta(
    request: ConsultaRequest,
    use_case: ProcesarConsultaUseCase = Depends(get_procesar_consulta_use_case)
):
    """
    Procesa una consulta del cliente y devuelve una respuesta basada en los documentos disponibles.
    
    - **cliente_id**: Identificador del cliente (debe coincidir con el nombre de la carpeta)
    - **pregunta**: La pregunta o consulta del cliente
    
    El sistema buscará en los documentos del cliente y devolverá la respuesta más relevante.
    """
    try:
        consulta = use_case.ejecutar(request.cliente_id, request.pregunta)
        if not consulta.respuesta:
            raise HTTPException(
                status_code=404,
                detail="No se encontró información relevante para la consulta"
            )
        return ConsultaResponse(respuesta=consulta.respuesta)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al procesar la consulta: {str(e)}"
        ) 