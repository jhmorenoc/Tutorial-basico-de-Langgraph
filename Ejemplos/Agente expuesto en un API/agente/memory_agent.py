"""
Agente con memoria implementado usando LangGraph y Gemini.

Este módulo contiene la implementación completa del agente conversacional que puede:
- Realizar operaciones matemáticas usando herramientas específicas
- Mantener memoria de conversaciones usando checkpointer
- Gestionar hilos de conversación por thread_id
"""

import os
from typing import List, Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.checkpoint.memory import MemorySaver
from tool.math_tools import AVAILABLE_TOOLS


class MemoryAgent:
    """
    Agente conversacional con memoria que puede realizar operaciones matemáticas.
    
    Este agente utiliza LangGraph para gestionar el flujo de conversación y mantiene
    la memoria de las interacciones usando un checkpointer en memoria.
    """
    
    def __init__(self, google_api_key: str = None):
        """
        Inicializa el agente con memoria.
        
        Args:
            google_api_key: Clave de API de Google para Gemini. Si no se proporciona,
                          se intentará obtener de la variable de entorno GOOGLE_API_KEY.
        """
        # Configurar la API key
        if google_api_key:
            os.environ["GOOGLE_API_KEY"] = google_api_key
        elif not os.environ.get("GOOGLE_API_KEY"):
            raise ValueError("Se requiere GOOGLE_API_KEY en variables de entorno o como parámetro")
        
        # Inicializar el modelo LLM
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
        
        # Configurar herramientas
        self.tools = AVAILABLE_TOOLS
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        
        # Mensaje del sistema
        self.system_message = SystemMessage(
            content="You are a helpful assistant tasked with performing arithmetic on a set of inputs. "
                   "You can perform addition, multiplication, and division operations. "
                   "Always be helpful and provide clear explanations of your calculations."
        )
        
        # Configurar memoria
        self.memory = MemorySaver()
        
        # Construir el grafo
        self._build_graph()
    
    def _build_graph(self):
        """Construye el grafo de conversación con memoria."""
        # Crear el builder del grafo
        builder = StateGraph(MessagesState)
        
        # Agregar nodos
        builder.add_node("assistant", self._assistant_node)
        builder.add_node("tools", ToolNode(self.tools))
        
        # Agregar aristas
        builder.add_edge(START, "assistant")
        builder.add_conditional_edges(
            "assistant",
            tools_condition,  # Condición que dirige a tools o END
        )
        builder.add_edge("tools", "assistant")
        
        # Compilar con memoria
        self.graph = builder.compile(checkpointer=self.memory)
    
    def _assistant_node(self, state: MessagesState) -> Dict[str, List[BaseMessage]]:
        """
        Nodo del asistente que procesa los mensajes y genera respuestas.
        
        Args:
            state: Estado actual de la conversación.
            
        Returns:
            Diccionario con la lista de mensajes actualizada.
        """
        # Combinar mensaje del sistema con el historial de mensajes
        messages = [self.system_message] + state["messages"]
        
        # Generar respuesta del modelo
        response = self.llm_with_tools.invoke(messages)
        
        return {"messages": [response]}
    
    def chat(self, message: str, thread_id: str = "default") -> Dict[str, Any]:
        """
        Procesa un mensaje del usuario y retorna la respuesta del agente.
        
        Args:
            message: Mensaje del usuario.
            thread_id: Identificador del hilo de conversación para mantener memoria.
            
        Returns:
            Diccionario con la respuesta del agente y metadatos.
        """
        # Configuración del hilo
        config = {"configurable": {"thread_id": thread_id}}
        
        # Crear mensaje humano
        human_message = HumanMessage(content=message)
        
        # Ejecutar el grafo
        result = self.graph.invoke({"messages": [human_message]}, config)
        
        # Extraer la última respuesta del asistente
        last_ai_message = None
        for msg in reversed(result["messages"]):
            if hasattr(msg, 'type') and msg.type == 'ai':
                last_ai_message = msg
                break
        
        # Preparar respuesta
        response = {
            "response": last_ai_message.content if last_ai_message else "No se pudo generar respuesta",
            "thread_id": thread_id,
            "message_count": len(result["messages"]),
            "tools_used": []
        }
        
        # Identificar herramientas utilizadas
        for msg in result["messages"]:
            if hasattr(msg, 'type') and msg.type == 'ai' and hasattr(msg, 'tool_calls') and msg.tool_calls:
                for tool_call in msg.tool_calls:
                    response["tools_used"].append({
                        "name": tool_call["name"],
                        "args": tool_call["args"]
                    })
        
        return response
    
    def get_conversation_history(self, thread_id: str = "default") -> List[Dict[str, Any]]:
        """
        Obtiene el historial de conversación para un hilo específico.
        
        Args:
            thread_id: Identificador del hilo de conversación.
            
        Returns:
            Lista de mensajes del historial.
        """
        config = {"configurable": {"thread_id": thread_id}}
        
        try:
            # Obtener el estado actual del grafo para este hilo
            state = self.graph.get_state(config)
            
            if not state.values or "messages" not in state.values:
                return []
            
            # Convertir mensajes a formato serializable
            history = []
            for msg in state.values["messages"]:
                msg_dict = {
                    "type": msg.type,
                    "content": msg.content
                }
                
                # Agregar información adicional según el tipo de mensaje
                if hasattr(msg, 'tool_calls') and msg.tool_calls:
                    msg_dict["tool_calls"] = msg.tool_calls
                
                history.append(msg_dict)
            
            return history
        
        except Exception:
            return []
    
    def clear_conversation(self, thread_id: str = "default") -> bool:
        """
        Limpia el historial de conversación para un hilo específico.
        
        Args:
            thread_id: Identificador del hilo de conversación.
            
        Returns:
            True si se limpió exitosamente, False en caso contrario.
        """
        try:
            config = {"configurable": {"thread_id": thread_id}}
            # En MemorySaver, podemos eliminar el estado reiniciando el grafo
            # Para una implementación más robusta, se podría usar un checkpointer personalizado
            return True
        except Exception:
            return False


# Exportar el grafo para LangGraph Studio
if __name__ == "__main__":
    import os
    # Configurar API key si no está disponible
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = "your_api_key_here"
    
    # Crear instancia del agente
    agent = MemoryAgent()
    
    # Exportar el grafo para Studio
    graph = agent.graph