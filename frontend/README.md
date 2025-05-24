# Sistema de Consultas Inteligentes

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.8+
- Node.js 18+
- npm 9+

### Instalación

1. **Backend (FastAPI)**
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar servidor
uvicorn app.main:app --reload
```

2. **Frontend (Angular)**
```bash
# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
ng serve
```

## 🔧 Configuración

### Backend
- URL: http://localhost:8000
- Método: POST
- Endpoint: /api/v1/consulta
- Headers: Content-Type: application/json
- Body:
```json
{
  "cliente_id": "string",
  "pregunta": "string"
}
```

### Frontend
- URL: http://localhost:4200
- Clientes disponibles: cliente1, cliente2, cliente3

## 📁 Estructura del Proyecto

```
├── app/                    # Backend (FastAPI)
│   └── main.py            # Punto de entrada
├── src/                   # Frontend (Angular)
│   ├── app/
│   │   ├── components/    # Componentes
│   │   ├── services/      # Servicios
│   │   └── models/        # Interfaces
│   └── ...
└── ...
```

## 🛠 Stack Tecnológico

- **Backend**: FastAPI, Python
- **Frontend**: Angular 18, Bootstrap 5, RxJS
- **UI/UX**: Font Awesome, SCSS

## ✨ Características

- UI/UX moderna y responsiva
- Validación en tiempo real
- Manejo de errores robusto
- Efectos visuales mejorados
- Diseño profesional

## 🐛 Solución de Problemas

### Errores Comunes

1. **CORS Error**
   - Verificar que el backend esté corriendo en el puerto 8000
   - Confirmar que CORS esté configurado correctamente

2. **Error de Conexión**
   - Verificar que ambos servidores estén corriendo
   - Comprobar las URLs en el servicio de consulta

## 📝 Notas Técnicas

- Arquitectura basada en componentes
- Manejo de estado con RxJS
- Validaciones del lado del cliente y servidor
- Diseño responsivo y adaptable

## 🔄 Flujo de Trabajo

1. Seleccionar cliente
2. Ingresar pregunta
3. Enviar consulta
4. Recibir y mostrar respuesta

## 🚀 Próximas Mejoras

- Autenticación de usuarios
- Sistema de logging
- Análisis de consultas
- Integración con modelos de IA

## 🏗️ Arquitectura

```
src/
├── components/          # Componentes UI
├── services/           # Lógica de negocio
└── models/             # Interfaces
```

### Stack Tecnológico
- Angular 18 (Standalone Components)
- Bootstrap 5
- RxJS
- Font Awesome

## 🎨 Características

- UI/UX moderna con animaciones
- Validación en tiempo real
- Manejo de errores robusto
- Diseño responsivo
- Feedback visual inmediato

## ⚠️ Solución de Problemas

### CORS
```bash
# Backend debe incluir headers
Access-Control-Allow-Origin: http://localhost:4200
```

### Errores Comunes
- Verificar puerto 8000 disponible
- Validar versiones de Node/Angular
- Reinstalar node_modules si es necesario

## 📝 Notas Técnicas

- Componentes standalone para mejor rendimiento
- Manejo de estado local optimizado
- Sistema de estilos modular
- Integración directa con API REST

## 🔄 Flujo de Trabajo

1. Selección de cliente
2. Ingreso de consulta
3. Procesamiento en backend
4. Visualización de respuesta

## 📈 Próximas Mejoras

- Autenticación
- Caché de respuestas
- Tests automatizados
- Logging avanzado

## Características

- Selección de cliente (cliente1, cliente2, cliente3)
- Formulario de consulta con validación
- Visualización de respuestas con animaciones
- Manejo de estados de carga
- Manejo de errores
- Interfaz responsiva y moderna
- Animaciones y transiciones suaves

## Estructura del Proyecto

```
src/
├── app/
│   ├── components/
│   │   ├── cliente-selector/     # Selector de clientes
│   │   ├── consulta-form/        # Formulario de consulta
│   │   └── respuesta-view/       # Visualización de respuestas
│   ├── services/
│   │   ├── cliente.service.ts    # Servicio de clientes
│   │   └── consulta.service.ts   # Servicio de consultas
│   ├── models/
│   │   └── interfaces.ts         # Interfaces TypeScript
│   └── app.component.ts          # Componente principal
├── styles.scss                   # Estilos globales
└── index.html                    # Página principal
```

## Características Técnicas

1. **Arquitectura**:
   - Componentes modulares y reutilizables
   - Servicios para manejo de lógica de negocio
   - Interfaces TypeScript para tipado fuerte
   - Componentes standalone

2. **Estado**:
   - Manejo de estado local en componentes
   - Comunicación entre componentes mediante Input/Output
   - Manejo de estados de carga y error

3. **UI/UX**:
   - Diseño responsivo con Bootstrap
   - Animaciones y transiciones suaves
   - Feedback visual para estados de carga y errores
   - Iconos de Font Awesome
   - Validaciones de formularios

4. **Estilos**:
   - Variables CSS para consistencia
   - Sistema de colores profesional
   - Gradientes y sombras
   - Animaciones personalizadas

## Contribución

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Cómo Agregar un Nuevo Cliente

1. Modificar el servicio `ClienteService` en `src/app/services/cliente.service.ts`
2. Agregar el nuevo cliente al array `clientes`
3. Asegurarse de que el backend tenga los documentos correspondientes para el nuevo cliente

## Próximos Pasos

- Implementar autenticación de usuarios
- Agregar sistema de logging
- Integrar con un modelo de IA real
- Implementar caché de respuestas
- Agregar pruebas unitarias y e2e

# Frontend Angular - Consulta de Documentos

## 📦 Requisitos

- Node.js + npm
- Angular CLI

## 🚀 Instalación

```bash
npm install
