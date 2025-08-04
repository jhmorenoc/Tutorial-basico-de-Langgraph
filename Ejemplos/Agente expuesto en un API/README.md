> 
⚠️ **Advertencia:** Este módulo está en construcción activa y puede contener algunos errores. En las próximas semanas estaré desplegando mejoras y corrigiendo posibles fallos. ¡Gracias por tu comprensión y paciencia!

# 🤖 Agente con Memoria - API REST

Una API REST desarrollada con **FastAPI** que expone un agente conversacional inteligente con memoria persistente, capaz de realizar operaciones matemáticas y mantener el contexto de conversaciones anteriores.

## 📋 Índice

- [Características](#-características)
- [Arquitectura](#-arquitectura)
- [Instalación Paso a Paso](#-instalación-paso-a-paso)
- [Configuración de API Keys](#-configuración-de-api-keys)
- [Ejecución del Agente](#-ejecución-del-agente)
- [Pruebas y Testing](#-pruebas-y-testing)
- [LangGraph Studio](#-langgraph-studio)
- [Endpoints de la API](#-endpoints-de-la-api)
- [Ejemplos de Uso](#-ejemplos-de-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Solución de Problemas](#-solución-de-problemas)

## 🌟 Características

- **🧠 Memoria Persistente**: Mantiene el contexto de conversaciones usando thread IDs
- **🔧 Herramientas Matemáticas**: Suma, multiplicación y división
- **🚀 FastAPI**: API REST moderna y rápida con documentación automática
- **🤖 LangGraph**: Gestión avanzada de flujos conversacionales
- **💎 Google Gemini**: Modelo de lenguaje de última generación
- **📖 Documentación Automática**: Swagger UI y ReDoc incluidos
- **🔒 Manejo de Errores**: Gestión robusta de excepciones
- **🌐 CORS**: Configurado para desarrollo multiplataforma

## 🏗️ Arquitectura

El proyecto está organizado siguiendo una arquitectura modular:

```
Agente expuesto en un API/
├── tool/                   # Herramientas del agente
│   ├── __init__.py
│   └── math_tools.py      # Funciones matemáticas
├── agente/                # Lógica del agente
│   ├── __init__.py
│   └── memory_agent.py    # Agente con memoria
├── app/                   # Aplicación FastAPI
│   ├── __init__.py
│   └── main.py           # API REST
├── setup.py              # Configuración automática
├── run_server.py         # Ejecutor del servidor
├── test_api.py           # Script de pruebas
├── requirements.txt      # Dependencias
└── README.md            # Este archivo
```

### Componentes Principales

#### 🔧 **Tool Layer** (`tool/`)
- **math_tools.py**: Contiene las herramientas matemáticas que el agente puede utilizar
- Funciones: `add()`, `multiply()`, `divide()`
- Documentación completa con ejemplos y validaciones

#### 🧠 **Agent Layer** (`agente/`)
- **memory_agent.py**: Implementa el agente conversacional con memoria
- Utiliza LangGraph para gestionar el flujo de conversación
- MemorySaver para persistencia de estado entre interacciones
- Gestión de threads para múltiples conversaciones simultáneas

#### 🌐 **App Layer** (`app/`)
- **main.py**: API REST con FastAPI
- Endpoints para chat, historial y gestión de conversaciones
- Documentación automática con Swagger UI
- Manejo de errores y validación de datos

## 🚀 Instalación Paso a Paso

### Prerrequisitos

- **Python 3.8 o superior** (recomendado Python 3.9+)
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar repositorios)
- **Cuenta de Google** para obtener API Key de Gemini

### Paso 1: Verificar Python

```bash
# Verificar versión de Python
python --version
# o si tienes Python 3 específicamente
python3 --version

# Verificar pip
pip --version
```

**Salida esperada:**
```
Python 3.9.x (o superior)
pip 21.x.x (o superior)
```

### Paso 2: Navegar al Directorio del Proyecto

```bash
# Cambiar al directorio del proyecto
cd "Ejemplos/Agente expuesto en un API"

# Verificar que estés en el directorio correcto
ls
```

**Deberías ver:**
```
agente/  app/  tool/  requirements.txt  README.md  setup.py  run_server.py  test_api.py
```

### Paso 3: Crear Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

**Verificación exitosa:**
- El prompt debería mostrar `(venv)` al inicio
- Ejemplo: `(venv) C:\Users\...\Agente expuesto en un API>`

### Paso 4: Actualizar pip (Recomendado)

```bash
# Actualizar pip a la última versión
python -m pip install --upgrade pip
```

### Paso 5: Instalar Dependencias

**Método 1: Instalación Automática**
```bash
# Usar el script de setup automático
python setup.py
```

**Método 2: Instalación Manual**
```bash
# Instalar dependencias manualmente
pip install -r requirements.txt
```

**Verificar instalación:**
```bash
# Listar paquetes instalados
pip list
```

**Deberías ver paquetes como:**
```
fastapi          0.104.1
uvicorn          0.24.0
langgraph        0.2.16
langchain-core   0.3.0
langchain-google-genai  2.0.0
pydantic         2.5.0
```

## 🔑 Configuración de API Keys

### Paso 1: Obtener Google API Key

1. **Ir a Google AI Studio:**
   - Visita: [https://makersuite.google.com/](https://makersuite.google.com/)
   - Inicia sesión con tu cuenta de Google

2. **Crear API Key:**
   - Haz clic en "Get API Key" o "Crear clave de API"
   - Selecciona o crea un proyecto
   - Copia la clave generada (guárdala de forma segura)

### Paso 2: Configurar Variable de Entorno

**Opción A: Archivo .env (Recomendado)**

1. Crear archivo `.env` en la raíz del proyecto:
```bash
# Crear archivo .env
touch .env  # En Linux/Mac
# En Windows, usar un editor de texto
```

2. Agregar contenido al archivo `.env`:
```env
# API Key de Google Gemini (REQUERIDO)
GOOGLE_API_KEY=tu_clave_api_real_aqui

# Configuración del servidor (OPCIONAL)
HOST=0.0.0.0
PORT=8000
RELOAD=true
LOG_LEVEL=info
```

**Opción B: Variable de Entorno del Sistema**

```bash
# En Windows (Command Prompt)
set GOOGLE_API_KEY=tu_clave_api_real_aqui

# En Windows (PowerShell)
$env:GOOGLE_API_KEY="tu_clave_api_real_aqui"

# En Linux/Mac
export GOOGLE_API_KEY=tu_clave_api_real_aqui
```

**Opción C: Configuración en el Entorno Virtual**

```bash
# Activar entorno virtual primero
# En Windows:
venv\Scripts\activate

# Agregar al archivo de activación del entorno virtual
# Windows (venv\Scripts\activate.bat):
echo set GOOGLE_API_KEY=tu_clave_api_real_aqui >> venv\Scripts\activate.bat

# Linux/Mac (venv/bin/activate):
echo 'export GOOGLE_API_KEY=tu_clave_api_real_aqui' >> venv/bin/activate
```

### Paso 3: Verificar Configuración

```bash
# Verificar que la variable esté configurada
# En Windows:
echo %GOOGLE_API_KEY%

# En Linux/Mac:
echo $GOOGLE_API_KEY

# En Python (opcional):
python -c "import os; print('API Key configurada:', 'GOOGLE_API_KEY' in os.environ)"
```

## 🏃 Ejecución del Agente

### Método 1: Script de Ejecución Automática (Recomendado)

```bash
# Ejecutar usando el script personalizado
python run_server.py
```

**Este script:**
- ✅ Verifica dependencias automáticamente
- ✅ Carga variables de entorno desde .env
- ✅ Valida la configuración de API Key
- ✅ Inicia el servidor con configuración óptima
- ✅ Muestra URLs útiles para acceder

### Método 2: Ejecución Manual con Uvicorn

```bash
# Ejecutar directamente con uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Método 3: Ejecutar desde el Módulo Principal

```bash
# Cambiar al directorio app y ejecutar
cd app
python main.py
```

### Verificación de Ejecución Exitosa

**Salida esperada:**
```
🚀 Iniciando servidor del Agente con Memoria API
==================================================
✅ Variables de entorno cargadas desde .env
✅ Google API Key encontrada: AIzaSyC...abc123
✅ Agente con memoria inicializado correctamente

📋 Configuración del servidor:
   Host: 0.0.0.0
   Puerto: 8000
   Recarga automática: True
   Nivel de log: info

🌐 URLs disponibles:
   API: http://0.0.0.0:8000
   Docs: http://0.0.0.0:8000/docs
   ReDoc: http://0.0.0.0:8000/redoc

==================================================
🟢 Iniciando servidor...
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Acceder a la Aplicación

Una vez ejecutado, puedes acceder a:

- **🏠 API Principal:** `http://localhost:8000`
- **📖 Documentación Swagger:** `http://localhost:8000/docs`
- **📚 Documentación ReDoc:** `http://localhost:8000/redoc`
- **❤️ Health Check:** `http://localhost:8000/health`

## 🧪 Pruebas y Testing

### Pruebas Automáticas

```bash
# Ejecutar suite completa de pruebas
python test_api.py
```

**Esto ejecutará:**
1. ✅ Verificación de estado de salud
2. ✅ Obtención de herramientas disponibles
3. ✅ Prueba de operación matemática simple
4. ✅ Prueba de memoria (primera parte)
5. ✅ Prueba de memoria (segunda parte - debe recordar)
6. ✅ Verificación de historial de conversación
7. ✅ Prueba de separación de threads
8. ✅ Limpieza de conversaciones

### Chat Interactivo

```bash
# Modo chat interactivo
python test_api.py --interactive
```

**Ejemplo de sesión:**
```
💬 Modo de chat interactivo iniciado
Escribe 'salir' para terminar

👤 Tú: Suma 15 y 25
🤖 Agente: 40
🔧 Herramientas usadas: [{'name': 'add', 'args': {'a': 15.0, 'b': 25.0}}]

👤 Tú: Multiplica ese resultado por 2
🤖 Agente: 80
🔧 Herramientas usadas: [{'name': 'multiply', 'args': {'a': 40.0, 'b': 2.0}}]

👤 Tú: salir
👋 ¡Hasta luego!
```

### Pruebas Manuales con curl

```bash
# 1. Verificar estado
curl http://localhost:8000/health

# 2. Enviar mensaje simple
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Suma 5 y 3",
       "thread_id": "test_session"
     }'

# 3. Continuar conversación (debe recordar)
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Multiplica ese resultado por 4", 
       "thread_id": "test_session"
     }'

# 4. Obtener historial
curl http://localhost:8000/conversation/test_session

# 5. Ver herramientas disponibles
curl http://localhost:8000/tools
```

### Pruebas con Python Requests

```python
import requests

# Configuración
API_BASE = "http://localhost:8000"
THREAD_ID = "mi_prueba"

# Test básico
response = requests.post(f"{API_BASE}/chat", json={
    "message": "¿Cuánto es 7 por 6?",
    "thread_id": THREAD_ID
})

print("Respuesta:", response.json())

# Test de memoria
response2 = requests.post(f"{API_BASE}/chat", json={
    "message": "Divide ese resultado entre 3",
    "thread_id": THREAD_ID
})

print("Respuesta con memoria:", response2.json())
```

## 🎨 LangGraph Studio

LangGraph Studio te permite visualizar y debuggear el flujo del agente de forma interactiva.

### Instalación de LangGraph Studio

```bash
# Instalar LangGraph CLI (si no está instalado)
pip install "langgraph-cli[inmemory]"

# Verificar instalación
langgraph --version
```

### Preparar el Agente para Studio

1. **Crear archivo `langgraph.json`** en la raíz del proyecto:

```json
{
  "dependencies": ["."],
  "graphs": {
    "memory_agent": "./agente/memory_agent.py:MemoryAgent"
  },
  "env": ".env"
}
```

2. **Modificar `memory_agent.py`** para exportar el grafo:

```python
# Agregar al final de agente/memory_agent.py
if __name__ == "__main__":
    import os
    os.environ.setdefault("GOOGLE_API_KEY", "tu_clave_api_aqui")
    agent = MemoryAgent()
    # Exportar el grafo para LangGraph Studio
    graph = agent.graph
```

### Ejecutar LangGraph Studio

```bash
# Navegar al directorio del proyecto
cd "Ejemplos/Agente expuesto en un API"

# Iniciar LangGraph Studio
langgraph dev

# Alternativamente, especificar archivo de configuración
langgraph dev --config langgraph.json
```

### Acceder a LangGraph Studio

**Salida esperada:**
```
🚀 LangGraph Studio starting...
📊 Graphs loaded: memory_agent
🌐 Studio available at: http://localhost:8123
🔧 API server: http://localhost:8000
```

**URLs de acceso:**
- **🎨 Studio UI:** `http://localhost:8123`
- **🔌 API Backend:** `http://localhost:8000`

### Características de LangGraph Studio

- **📊 Visualización del Grafo:** Ver el flujo del agente visualmente
- **🐛 Debugging:** Ejecutar paso a paso y ver estados intermedios
- **📝 Historial:** Revisar ejecuciones anteriores
- **🔄 Replay:** Re-ejecutar conversaciones para debugging
- **📈 Métricas:** Ver estadísticas de uso y rendimiento

### Usar Studio con el Agente

1. **Abrir Studio:** `http://localhost:8123`
2. **Seleccionar grafo:** "memory_agent"
3. **Crear nueva conversación:** Botón "New Thread"
4. **Enviar mensaje:** "Suma 10 y 15"
5. **Ver ejecución:** Observar cada paso del agente
6. **Continuar conversación:** "Multiplica por 2"
7. **Analizar memoria:** Ver cómo se mantiene el estado

## 📚 Endpoints de la API

### 🏠 **GET /** - Estado de Salud
```json
{
  "status": "healthy",
  "agent_ready": true,
  "version": "1.0.0"
}
```

### 💬 **POST /chat** - Conversar con el Agente
```json
// Solicitud
{
  "message": "Suma 3 y 4",
  "thread_id": "conversacion_1"
}

// Respuesta
{
  "response": "7",
  "thread_id": "conversacion_1", 
  "message_count": 2,
  "tools_used": [
    {
      "name": "add",
      "args": {"a": 3, "b": 4}
    }
  ]
}
```

### 📖 **GET /conversation/{thread_id}** - Historial de Conversación
```json
{
  "thread_id": "conversacion_1",
  "messages": [
    {
      "type": "human",
      "content": "Suma 3 y 4"
    },
    {
      "type": "ai", 
      "content": "7",
      "tool_calls": [...]
    }
  ],
  "message_count": 2
}
```

### 🗑️ **DELETE /conversation/{thread_id}** - Limpiar Conversación
```json
{
  "message": "Conversación conversacion_1 limpiada exitosamente"
}
```

### 🛠️ **GET /tools** - Herramientas Disponibles
```json
{
  "tools": [
    {
      "name": "add",
      "description": "Suma dos números enteros",
      "parameters": ["a: int", "b: int"],
      "returns": "int"
    }
  ]
}
```

## 💡 Ejemplos de Uso

### Ejemplo 1: Operación Simple

```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "¿Cuánto es 15 multiplicado por 3?",
       "thread_id": "usuario_123"
     }'
```

### Ejemplo 2: Conversación con Memoria

```bash
# Primera interacción
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Suma 10 y 5",
       "thread_id": "calculo_session"
     }'

# Segunda interacción (el agente recuerda el resultado anterior)
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Ahora multiplica ese resultado por 2",
       "thread_id": "calculo_session"
     }'
```

### Ejemplo 3: Usando Python Requests

```python
import requests

# Configuración
API_BASE = "http://localhost:8000"
THREAD_ID = "mi_conversacion"

# Función para chatear
def chat(message):
    response = requests.post(f"{API_BASE}/chat", json={
        "message": message,
        "thread_id": THREAD_ID
    })
    return response.json()

# Conversación de ejemplo
print(chat("Suma 25 y 17"))
print(chat("Divide ese resultado entre 6"))
print(chat("¿Cuál fue el primer cálculo que hicimos?"))

# Obtener historial
history = requests.get(f"{API_BASE}/conversation/{THREAD_ID}")
print(history.json())
```

## 📁 Estructura del Proyecto

```
Ejemplos/Agente expuesto en un API/
│
├── 📁 tool/                       # Capa de herramientas
│   ├── __init__.py               # Inicialización del módulo
│   └── math_tools.py             # Herramientas matemáticas
│       ├── add()                 # Función de suma
│       ├── multiply()            # Función de multiplicación
│       ├── divide()              # Función de división
│       └── AVAILABLE_TOOLS       # Lista de herramientas
│
├── 📁 agente/                     # Capa del agente
│   ├── __init__.py               # Inicialización del módulo
│   └── memory_agent.py           # Agente con memoria
│       ├── MemoryAgent           # Clase principal del agente
│       ├── _build_graph()        # Construcción del grafo LangGraph
│       ├── chat()                # Método principal de conversación
│       ├── get_conversation_history() # Obtener historial
│       └── clear_conversation()  # Limpiar conversación
│
├── 📁 app/                        # Capa de aplicación
│   ├── __init__.py               # Inicialización del módulo
│   └── main.py                   # API REST FastAPI
│       ├── ChatRequest/Response  # Modelos de datos Pydantic
│       ├── /chat                 # Endpoint de conversación
│       ├── /conversation/{id}    # Endpoint de historial
│       ├── /health               # Endpoint de salud
│       └── /tools                # Endpoint de herramientas
│
├── setup.py                      # Script de configuración automática
├── run_server.py                 # Script para ejecutar servidor
├── test_api.py                   # Script de pruebas y chat interactivo
├── requirements.txt              # Dependencias del proyecto
├── .env                          # Variables de entorno (crear)
├── langgraph.json               # Configuración LangGraph Studio (crear)
└── README.md                    # Documentación (este archivo)
```

## 🔧 Solución de Problemas

### Error: "GOOGLE_API_KEY not found"

**Problema:** La API key no está configurada correctamente.

**Soluciones:**
```bash
# 1. Verificar variable de entorno
echo $GOOGLE_API_KEY  # Linux/Mac
echo %GOOGLE_API_KEY%  # Windows

# 2. Configurar temporalmente
export GOOGLE_API_KEY=tu_clave_aqui  # Linux/Mac
set GOOGLE_API_KEY=tu_clave_aqui     # Windows

# 3. Verificar archivo .env
cat .env  # Linux/Mac
type .env  # Windows
```

### Error: "Module not found"

**Problema:** Dependencias no instaladas o entorno virtual no activado.

**Soluciones:**
```bash
# 1. Activar entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 2. Reinstalar dependencias
pip install -r requirements.txt

# 3. Verificar instalación
pip list | grep fastapi
pip list | grep langgraph
```

### Error: "Port 8000 already in use"

**Problema:** El puerto está ocupado por otro proceso.

**Soluciones:**
```bash
# 1. Cambiar puerto en run_server.py o usar variable de entorno
export PORT=8001

# 2. Matar proceso en puerto 8000 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID_NUMBER> /F

# 3. Matar proceso en puerto 8000 (Linux/Mac)
lsof -ti:8000 | xargs kill -9
```

### Error: "LangGraph Studio not starting"

**Problema:** Configuración incorrecta de LangGraph Studio.

**Soluciones:**
```bash
# 1. Verificar instalación
pip install "langgraph-cli[inmemory]"

# 2. Crear langgraph.json correcto
echo '{
  "dependencies": ["."],
  "graphs": {
    "memory_agent": "./agente/memory_agent.py:MemoryAgent"
  },
  "env": ".env"
}' > langgraph.json

# 3. Verificar estructura de archivos
ls -la agente/memory_agent.py
```

### El agente no recuerda conversaciones

**Problema:** Thread IDs no coinciden o memoria no configurada.

**Soluciones:**
- ✅ Usar el mismo `thread_id` en todas las llamadas
- ✅ Verificar que MemorySaver esté inicializado
- ✅ Comprobar logs del servidor para errores

### Respuestas lentas o timeouts

**Problema:** Latencia en la API de Google o problemas de red.

**Soluciones:**
- ✅ Verificar conexión a internet
- ✅ Probar con una API key diferente
- ✅ Revisar límites de cuota de Google AI

---

## 👤 Autor

- **Jorge Moreno**  
  [LinkedIn](https://www.linkedin.com/in/johmorenoco/)