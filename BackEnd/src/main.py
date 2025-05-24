from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from src.adapters.primary.http.consulta_controller import router as consulta_router

app = FastAPI(
    title="Sistema de Consulta Inteligente",
    description="API para consultas inteligentes en documentos de clientes",
    version="1.0.0",
    docs_url=None,
    redoc_url=None
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(consulta_router, prefix="/api/v1")

# Configuración personalizada de Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Sistema de Consulta Inteligente",
        version="1.0.0",
        description="API para consultas inteligentes en documentos de clientes",
        routes=app.routes,
    )
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Sistema de Consulta Inteligente",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css",
        swagger_ui_parameters={
            "defaultModelsExpandDepth": 3,
            "defaultModelExpandDepth": 3,
            "displayRequestDuration": True,
            "filter": True,
            "docExpansion": "list",
            "syntaxHighlight.theme": "monokai",
            "persistAuthorization": True,
            "displayOperationId": True,
            "tryItOutEnabled": True
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 