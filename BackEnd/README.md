# Sistema de Consulta Inteligente

## 🏗️ Arquitectura Hexagonal (Clean Architecture)

Este proyecto implementa la Arquitectura Hexagonal (también conocida como Clean Architecture) para garantizar una estructura modular, mantenible y escalable. La arquitectura se divide en las siguientes capas:

### 1. Dominio (Core)
- **Ubicación**: `src/domain/`
- **Contenido**: 
  - Entidades del negocio
  - Casos de uso
  - Interfaces de puertos
- **Responsabilidad**: Contiene la lógica de negocio pura, independiente de frameworks y tecnologías externas.

### 2. Aplicación (Application)
- **Ubicación**: `src/application/`
- **Contenido**:
  - Implementación de casos de uso
  - Servicios de aplicación
  - DTOs
- **Responsabilidad**: Orquesta los casos de uso y coordina el flujo de datos entre el dominio y los adaptadores.

### 3. Adaptadores (Adapters)
- **Ubicación**: `src/adapters/`
- **Contenido**:
  - **Primarios (Entrantes)**:
    - `primary/http/`: Controladores REST
    - `primary/api/`: Endpoints de la API
  - **Secundarios (Salientes)**:
    - `secondary/document_loader/`: Carga de documentos
    - `secondary/storage/`: Persistencia de datos
- **Responsabilidad**: Adapta las tecnologías externas a la lógica de negocio.

### 4. Infraestructura (Infrastructure)
- **Ubicación**: `src/infrastructure/`
- **Contenido**:
  - Configuración de la aplicación
  - Servicios externos
  - Utilidades
- **Responsabilidad**: Proporciona implementaciones concretas de las interfaces definidas en el dominio.

## 🎯 Ventajas de la Arquitectura Hexagonal

1. **Independencia de Frameworks**
   - El dominio no depende de frameworks externos
   - Fácil cambio de tecnologías sin afectar la lógica de negocio

2. **Testabilidad**
   - Facilita la escritura de pruebas unitarias
   - Permite mockear dependencias externas

3. **Mantenibilidad**
   - Separación clara de responsabilidades
   - Código más organizado y fácil de entender

4. **Escalabilidad**
   - Fácil adición de nuevas funcionalidades
   - Adaptación a nuevos requerimientos

## 📁 Estructura del Proyecto

```
src/
├── domain/                    # Capa de dominio
│   ├── entities/             # Entidades del negocio
│   ├── use_cases/            # Casos de uso
│   └── ports/                # Interfaces (puertos)
│
├── application/              # Capa de aplicación
│   ├── services/            # Servicios de aplicación
│   └── dtos/                # Objetos de transferencia de datos
│
├── adapters/                # Capa de adaptadores
│   ├── primary/             # Adaptadores primarios (entrantes)
│   │   ├── http/           # Controladores HTTP
│   │   └── api/            # Endpoints de la API
│   │
│   └── secondary/          # Adaptadores secundarios (salientes)
│       ├── document_loader/ # Carga de documentos
│       └── storage/        # Persistencia de datos
│
└── infrastructure/          # Capa de infraestructura
    ├── config/             # Configuración
    └── utils/              # Utilidades

documents/                   # Documentos de clientes
├── cliente1/
├── cliente2/
└── cliente3/
```

## 🚀 Ejecución del Proyecto

1. Instalar dependencias:
```bash
pip install -r requirements.txt
```

2. Configurar variables de entorno:
```bash
cp .env.example .env
```

3. Ejecutar la aplicación:
```bash
python src/main.py
```

## 📝 Ejemplos de Uso

### Consulta a Cliente 1 (Productos Financieros)
```json
POST /api/v1/consulta
{
    "cliente_id": "cliente1",
    "pregunta": "¿Cuál es la tasa de interés de la cuenta de ahorros?"
}
```

### Consulta a Cliente 2 (Seguridad)
```json
POST /api/v1/consulta
{
    "cliente_id": "cliente2",
    "pregunta": "¿Cuáles son los requisitos de contraseña?"
}
```

### Consulta a Cliente 3 (Atención al Cliente)
```json
POST /api/v1/consulta
{
    "cliente_id": "cliente3",
    "pregunta": "¿Cuáles son los tiempos de respuesta para urgencia alta?"
}
```

## 🔧 Tecnologías Utilizadas

- FastAPI
- Python 3.8+
- Uvicorn
- Pydantic
- Swagger UI

## 📚 Documentación API

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 👥 Clientes y Documentos Disponibles

El sistema incluye tres clientes preconfigurados con sus respectivos documentos:

### Cliente 1: Productos Financieros
- **documento1.txt**: Información sobre productos financieros (cuentas, tarjetas, préstamos)
- **configuracion.json**: Configuración de cuenta y preferencias

### Cliente 2: Seguridad y Privacidad
- **documento1.txt**: Políticas de seguridad y privacidad
- **configuracion.json**: Configuración de políticas de seguridad

### Cliente 3: Atención al Cliente
- **documento1.txt**: Procedimientos de atención al cliente
- **configuracion.json**: SLA y métricas de servicio

## 🔄 Endpoints

### POST /api/v1/consulta

```json
{
  "cliente_id": "string",
  "pregunta": "string"
}
```

## 📝 Contenido de los Documentos

### Cliente 1 - Productos Financieros
- Cuenta de Ahorros (tasa 2.5% anual)
- Tarjeta de Crédito (línea desde $5,000)
- Préstamo Personal (hasta $100,000)
- Configuración de límites y notificaciones

### Cliente 2 - Seguridad
- Protección de Datos
- Acceso y Autenticación
- Monitoreo y Auditoría
- Políticas de contraseñas y sesiones

### Cliente 3 - Atención al Cliente
- Canales de Atención (24/7)
- Niveles de Soporte
- Tiempos de Respuesta
- SLA y métricas de servicio

## 🛠️ Tecnologías Utilizadas

- FastAPI: Framework web moderno y rápido
- Pydantic: Validación de datos
- Python-dotenv: Manejo de variables de entorno
- Uvicorn: Servidor ASGI

## 🔍 Características

- ✅ Endpoint REST para consultas
- ✅ Soporte multicliente
- ✅ Búsqueda en documentos .txt y .json
- ✅ Validación de datos
- ✅ Documentación automática
- ✅ CORS habilitado para desarrollo frontend

## ⚠️ Notas Importantes

1. El sistema simula un modelo de lenguaje con un delay de 1.5 segundos
2. Las respuestas se basan en búsqueda de texto en los documentos
3. Se soportan archivos .txt y .json
4. Los IDs de cliente deben coincidir exactamente con los nombres de las carpetas