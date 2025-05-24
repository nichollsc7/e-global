# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.consulta import router as consulta_router
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles
import json

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

# HTML personalizado para Swagger UI
SWAGGER_UI_CUSTOM_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Sistema de Consulta Inteligente</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css" />
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #34495e;
            --accent-color: #3498db;
            --text-color: #2c3e50;
            --background-color: #f8f9fa;
            --border-color: #e9ecef;
        }

        body {
            margin: 0;
            background-color: var(--background-color);
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        }

        .swagger-ui {
            font-family: inherit;
        }

        .swagger-ui .topbar {
            background-color: var(--primary-color);
            padding: 15px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .swagger-ui .info .title {
            color: var(--primary-color);
            font-size: 2.5em;
            font-weight: 600;
            margin: 0.5em 0;
        }

        .swagger-ui .info .description {
            font-size: 1.1em;
            line-height: 1.6;
            color: var(--text-color);
        }

        .swagger-ui .opblock {
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            margin: 0 0 20px;
            border: 1px solid var(--border-color);
            background: white;
        }

        .swagger-ui .opblock-tag {
            border-radius: 4px;
            padding: 10px 15px;
            background-color: var(--primary-color);
            color: white;
            font-weight: 600;
            margin: 0 0 10px;
        }

        .swagger-ui .opblock.opblock-post {
            border-color: var(--accent-color);
            background: white;
        }

        .swagger-ui .opblock.opblock-post .opblock-summary-method {
            background: var(--accent-color);
        }

        .swagger-ui .btn.execute {
            background-color: var(--accent-color);
            border-color: var(--accent-color);
            color: white;
            font-weight: 600;
            padding: 8px 16px;
            border-radius: 4px;
            transition: all 0.3s ease;
        }

        .swagger-ui .btn.execute:hover {
            background-color: #2980b9;
            border-color: #2980b9;
            transform: translateY(-1px);
        }

        .swagger-ui .opblock-description-wrapper p {
            font-size: 1em;
            color: var(--text-color);
            line-height: 1.6;
        }

        .swagger-ui .markdown p {
            font-size: 1em;
            line-height: 1.6;
            color: var(--text-color);
        }

        .swagger-ui .markdown table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }

        .swagger-ui .markdown table th {
            background-color: var(--primary-color);
            color: white;
            font-weight: 600;
            padding: 12px 15px;
            text-align: left;
        }

        .swagger-ui .markdown table td {
            padding: 12px 15px;
            border: 1px solid var(--border-color);
            background: white;
        }

        .swagger-ui .markdown code {
            background-color: #f8f9fa;
            padding: 2px 6px;
            border-radius: 4px;
            color: var(--accent-color);
            font-family: 'Consolas', monospace;
        }

        .swagger-ui .markdown pre {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            margin: 15px 0;
        }

        .swagger-ui .response-col_status {
            color: var(--accent-color);
            font-weight: 600;
        }

        .swagger-ui .response-col_description {
            color: var(--text-color);
        }

        .swagger-ui .scheme-container {
            background-color: var(--primary-color);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .swagger-ui .servers-title {
            color: white;
        }

        .swagger-ui .servers {
            background-color: var(--primary-color);
        }

        .swagger-ui .servers > label {
            color: white;
        }

        .swagger-ui .servers > select {
            border: 1px solid var(--border-color);
            border-radius: 4px;
            padding: 5px;
        }

        .swagger-ui .info .base-url {
            color: var(--text-color);
        }

        .swagger-ui .info .title small.version-stamp {
            background-color: var(--accent-color);
        }

        .swagger-ui .opblock .opblock-summary {
            border-bottom: 1px solid var(--border-color);
        }

        .swagger-ui .opblock .opblock-summary-description {
            color: var(--text-color);
        }

        .swagger-ui .opblock .opblock-summary-method {
            border-radius: 4px;
            font-weight: 600;
        }

        .swagger-ui .opblock .opblock-summary-path {
            color: var(--text-color);
        }

        .swagger-ui .opblock .opblock-summary-operation-id {
            color: var(--accent-color);
        }

        .swagger-ui .opblock .opblock-summary-path__deprecated {
            color: #dc3545;
        }

        .swagger-ui .opblock .opblock-summary-method {
            text-transform: uppercase;
            font-weight: 600;
        }

        .swagger-ui .opblock .opblock-summary-method.opblock-post {
            background-color: var(--accent-color);
        }

        .swagger-ui .opblock .opblock-summary-method.opblock-get {
            background-color: #2ecc71;
        }

        .swagger-ui .opblock .opblock-summary-method.opblock-put {
            background-color: #f1c40f;
        }

        .swagger-ui .opblock .opblock-summary-method.opblock-delete {
            background-color: #e74c3c;
        }

        .swagger-ui .opblock .opblock-summary-method.opblock-patch {
            background-color: #9b59b6;
        }

        .swagger-ui .opblock .opblock-summary-method.opblock-head {
            background-color: #95a5a6;
        }

        .swagger-ui .opblock .opblock-summary-method.opblock-options {
            background-color: #7f8c8d;
        }

        .swagger-ui .opblock .opblock-summary-method.opblock-trace {
            background-color: #34495e;
        }
    </style>
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js"></script>
    <script>
        window.onload = function() {
            const ui = SwaggerUIBundle({
                url: "/openapi.json",
                dom_id: '#swagger-ui',
                deepLinking: true,
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.SwaggerUIStandalonePreset
                ],
                plugins: [
                    SwaggerUIBundle.plugins.DownloadUrl
                ],
                layout: "BaseLayout",
                docExpansion: "list",
                defaultModelsExpandDepth: 3,
                defaultModelExpandDepth: 3,
                displayRequestDuration: true,
                filter: true,
                showExtensions: true,
                showCommonExtensions: true,
                syntaxHighlight: {
                    activated: true,
                    theme: "monokai"
                },
                persistAuthorization: true,
                displayOperationId: true,
                tryItOutEnabled: true,
                requestInterceptor: (req) => {
                    req.headers['X-Requested-With'] = 'XMLHttpRequest';
                    return req;
                }
            });
            window.ui = ui;
        };
    </script>
</body>
</html>
"""

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
