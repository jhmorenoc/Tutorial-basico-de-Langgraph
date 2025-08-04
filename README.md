# 🕸️ Demo LangGraph - Repositorio de Aprendizaje

**Repositorio para aprender a usar LangGraph básico con Google Gemini Flash**

Este repositorio contiene ejemplos prácticos en Jupyter notebooks para aprender a construir agentes y flujos de trabajo usando **LangGraph** con **Google Gemini Flash**.

## 🎯 ¿Qué es este repositorio?

- **📚 Repositorio educativo** para aprender LangGraph desde cero
- **🤖 Ejemplos prácticos** con Google Gemini Flash  
- **📓 Notebooks interactivos** listos para ejecutar
- **⚡ Configuración simple** - cada notebook maneja sus propias variables
- **🛠️ Herramientas** para desarrollo rápido con IA

## 📦 ¿Qué contiene?

### 📓 **Ejemplos de LangGraph (Carpeta `Ejemplos/`)**
- **`1 LLM estructurado.ipynb`** - Salidas estructuradas con Pydantic
- **`2 Encadenamiento de Prompts.ipynb`** - Encadenamiento secuencial avanzado
- **`3 Paralelizado.ipynb`** - Procesamiento paralelo de tareas
- **`4 Enrutador copy.ipynb`** - Enrutamiento condicional de flujos
- **`5 Orquestador.ipynb`** - Orquestación compleja de agentes
- **`6 evaluador-optimizador.ipynb`** - Evaluación y optimización de respuestas
- **`7 Agente con memoria.ipynb`** - Agentes con persistencia y memoria

### 🚀 **API REST del Agente**
- **`Agente expuesto en un API/`** - API completa con FastAPI para el agente con memoria

### 🛠️ **Herramientas de Desarrollo**
- **`demo_gemini.py`** - Demo interactivo con chat en terminal
- **`requirements.txt`** - Todas las dependencias necesarias
- **`.gitignore`** - Protección automática de archivos sensibles

## 🚀 Configuración (Solo 2 pasos)

### 1. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 2. **Obtener Google API Key**
1. Ve a: [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Inicia sesión con tu cuenta de Google  
3. Crea una nueva API key
4. Copia la key (empieza con `AIza...`)

¡Eso es todo! 🎉

## 📓 Ejecutar los Notebooks directamente en VS o intenta con:

```bash
# Iniciar Jupyter Notebook
jupyter notebook

# O usar Jupyter Lab  
jupyter lab
```

**Cada notebook te pedirá tu API key** la primera vez que lo ejecutes. Si usas VS Code, el prompt puede aparecer en la parte superior de la ventana. Solo pégala cuando aparezca el prompt y ¡listo!  
Ten en cuenta que esta key desaparecerá al reiniciar el kernel de Python si estás usando un entorno virtual, que es lo recomendado para trabajar.

## 💻 Uso en los Notebooks

Cada notebook incluye esta configuración automática:

```python
import os
import getpass
from langchain_google_genai import ChatGoogleGenerativeAI

# Configuración automática de API key
def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
```

## 🎯 ¿Qué aprenderás?

### 📓 **Notebooks incluidos:**
- ✅ **LLM Estructurado** - Salidas estructuradas con Pydantic
- ✅ **Encadenamiento de Prompts** - Secuencias avanzadas de prompts
- ✅ **Procesamiento Paralelo** - Ejecutar tareas en paralelo
- ✅ **Enrutador** - Flujos condicionales y decisiones
- ✅ **Orquestador** - Coordinación de múltiples agentes
- ✅ **Evaluador-Optimizador** - Evaluación y mejora automática
- ✅ **Agente con Memoria** - Persistencia entre conversaciones
- ✅ **API REST** - Exposición del agente vía FastAPI

### 🔄 **Conceptos de LangGraph:**
- 🔄 Estados y grafos de procesamiento
- 🔄 Nodos y aristas en flujos de trabajo
- 🔄 Manejo de datos entre pasos
- 🔄 Agentes con múltiples herramientas

### 🔮 **Próximamente:**
- 🔮 Más ejemplos avanzados
- 🔮 Integración con herramientas externas
- 🔮 Casos de uso con MCP

## 📖 Guía de Lectura Recomendada

Para obtener el máximo aprendizaje, sigue este orden:

1. **📓 Notebooks (en orden numérico)**:
   - `1 LLM estructurado.ipynb` → Fundamentos de salidas estructuradas
   - `2 Encadenamiento de Prompts.ipynb` → Secuencias y flujos
   - `3 Paralelizado.ipynb` → Procesamiento simultáneo
   - `4 Enrutador copy.ipynb` → Decisiones y enrutamiento
   - `5 Orquestador.ipynb` → Coordinación avanzada
   - `6 evaluador-optimizador.ipynb` → Evaluación y mejora
   - `7 Agente con memoria.ipynb` → Persistencia y memoria

2. **🚀 Proyecto Final**:
   - `Agente expuesto en un API/` → Implementación completa en producción

## 🤖 Demo Rápido

¿Quieres probar Gemini Flash inmediatamente?

```bash
python demo_gemini.py
```

Te pedirá tu API key y podrás chatear directamente con Gemini en la terminal.

## 📚 Estructura del Proyecto

```
Demo_Lg/
├── 📁 Ejemplos/                          # Notebooks de LangGraph
│   ├── 1 LLM estructurado.ipynb         # Salidas estructuradas
│   ├── 2 Encadenamiento de Prompts.ipynb # Secuencias de prompts
│   ├── 3 Paralelizado.ipynb             # Procesamiento paralelo
│   ├── 4 Enrutador.ipynb           # Enrutamiento condicional
│   ├── 5 Orquestador.ipynb              # Orquestación de agentes
│   ├── 6 evaluador-optimizador.ipynb    # Evaluación automática
│   ├── 7 Agente con memoria.ipynb       # Agentes con memoria
│   └── 🚀 Agente expuesto en un API/    # API REST con FastAPI
├── 📦 requirements.txt                  # Dependencias del proyecto
├── 🤖 demo_gemini.py                    # Demo interactivo en terminal
├── 🛡️ .gitignore                        # Protección de archivos
└── 📖 README.md                         # Este archivo
```

## 🔒 Seguridad

🛡️ **API Keys protegidas automáticamente:**
- Cada notebook usa `getpass` para ocultar tu API key
- Las keys no se guardan en archivos
- No hay riesgo de subir keys al repositorio si lo clona a uno propio

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!

- 🐛 Reportar bugs o problemas
- 💡 Sugerir mejoras o nuevos ejemplos  
- 📚 Agregar más casos de uso
- 📝 Mejorar documentación

## 📞 ¿Problemas?

1. **Instalación**: `pip install -r requirements.txt`
2. **API Key**: [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Jupyter**: `jupyter notebook` o `jupyter lab`

---

**🎉 ¡Comienza con `pip install -r requirements.txt` y abre los notebooks!** 


---

## 👤 Autor

- **Jorge Moreno**  
  [LinkedIn](https://www.linkedin.com/in/johmorenoco/)


