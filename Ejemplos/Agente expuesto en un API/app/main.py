"""
API REST FastAPI para el agente con memoria.

Esta aplicación expone el agente conversacional con memoria a través de endpoints REST,
permitiendo interacciones de chat, gestión de conversaciones y monitoreo del sistema.
"""

import os
import sys
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager

# Agregar el directorio padre al path para importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
import uvicorn

from agente.memory_agent import MemoryAgent


# Modelos Pydantic para las solicitudes y respuestas
class ChatRequest(BaseModel):
    """Modelo para solicitudes de chat."""
    message: str = Field(..., description="Mensaje del usuario", min_length=1)
    thread_id: str = Field(default="default", description="ID del hilo de conversación")


class ChatResponse(BaseModel):
    """Modelo para respuestas de chat."""
    response: str = Field(..., description="Respuesta del agente")
    thread_id: str = Field(..., description="ID del hilo de conversación")
    message_count: int = Field(..., description="Número total de mensajes en la conversación")
    tools_used: List[Dict[str, Any]] = Field(default=[], description="Herramientas utilizadas en esta respuesta")


class ConversationHistoryResponse(BaseModel):
    """Modelo para el historial de conversación."""
    thread_id: str = Field(..., description="ID del hilo de conversación")
    messages: List[Dict[str, Any]] = Field(..., description="Lista de mensajes del historial")
    message_count: int = Field(..., description="Número total de mensajes")


class HealthResponse(BaseModel):
    """Modelo para el estado de salud de la API."""
    status: str = Field(..., description="Estado de la API")
    agent_ready: bool = Field(..., description="Estado del agente")
    version: str = Field(..., description="Versión de la API")


# Variable global para el agente
agent = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestión del ciclo de vida de la aplicación."""
    global agent
    
    # Startup
    try:
        # Verificar que la API key esté disponible
        if not os.environ.get("GOOGLE_API_KEY"):
            raise ValueError("GOOGLE_API_KEY no está configurada en las variables de entorno")
        
        # Inicializar el agente
        agent = MemoryAgent()
        print("✅ Agente con memoria inicializado correctamente")
        
    except Exception as e:
        print(f"❌ Error al inicializar el agente: {e}")
        raise
    
    yield
    
    # Shutdown
    print("🔄 Cerrando aplicación...")


# Crear la aplicación FastAPI
app = FastAPI(
    title="Agente con Memoria API",
    description="API REST para interactuar con un agente conversacional que mantiene memoria de las conversaciones y puede realizar operaciones matemáticas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=HealthResponse)
async def root():
    """Endpoint de estado de salud de la API."""
    return HealthResponse(
        status="healthy",
        agent_ready=agent is not None,
        version="1.0.0"
    )


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Endpoint detallado de verificación de salud."""
    if agent is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="El agente no está inicializado"
        )
    
    return HealthResponse(
        status="healthy",
        agent_ready=True,
        version="1.0.0"
    )


@app.post("/chat", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    """
    Envía un mensaje al agente y recibe una respuesta.
    
    El agente mantiene memoria de la conversación usando el thread_id,
    lo que permite referencias a mensajes anteriores y continuidad en la conversación.
    """
    if agent is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="El agente no está disponible"
        )
    
    try:
        # Procesar el mensaje con el agente
        result = agent.chat(message=request.message, thread_id=request.thread_id)
        
        return ChatResponse(
            response=result["response"],
            thread_id=result["thread_id"],
            message_count=result["message_count"],
            tools_used=result["tools_used"]
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al procesar el mensaje: {str(e)}"
        )


@app.get("/conversation/{thread_id}", response_model=ConversationHistoryResponse)
async def get_conversation_history(thread_id: str):
    """
    Obtiene el historial completo de una conversación.
    
    Retorna todos los mensajes intercambiados en el hilo de conversación especificado.
    """
    if agent is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="El agente no está disponible"
        )
    
    try:
        history = agent.get_conversation_history(thread_id)
        
        return ConversationHistoryResponse(
            thread_id=thread_id,
            messages=history,
            message_count=len(history)
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener el historial: {str(e)}"
        )


@app.delete("/conversation/{thread_id}")
async def clear_conversation(thread_id: str):
    """
    Limpia el historial de una conversación específica.
    
    Elimina todos los mensajes del hilo de conversación especificado.
    """
    if agent is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="El agente no está disponible"
        )
    
    try:
        success = agent.clear_conversation(thread_id)
        
        if success:
            return {"message": f"Conversación {thread_id} limpiada exitosamente"}
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="No se pudo limpiar la conversación"
            )
            
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al limpiar la conversación: {str(e)}"
        )


@app.get("/tools")
async def get_available_tools():
    """
    Obtiene la lista de herramientas disponibles para el agente.
    
    Retorna información sobre las funciones que el agente puede utilizar.
    """
    tools_info = [
        {
            "name": "add",
            "description": "Suma dos números enteros",
            "parameters": ["a: int", "b: int"],
            "returns": "int"
        },
        {
            "name": "multiply", 
            "description": "Multiplica dos números enteros",
            "parameters": ["a: int", "b: int"],
            "returns": "int"
        },
        {
            "name": "divide",
            "description": "Divide dos números enteros",
            "parameters": ["a: int", "b: int"],
            "returns": "float"
        }
    ]
    
    return {"tools": tools_info}


# Manejo de errores globales
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Manejo global de excepciones no controladas."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": f"Error interno del servidor: {str(exc)}"}
    )


if __name__ == "__main__":
    # Configuración para desarrollo local
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )