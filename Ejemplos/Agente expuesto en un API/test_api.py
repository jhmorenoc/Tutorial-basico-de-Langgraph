"""
Script de prueba para la API del agente con memoria.

Este script demuestra cómo usar la API de forma programática
y realiza pruebas básicas de funcionalidad.
"""

import requests
import json
import time
from typing import Dict, Any


class AgentAPIClient:
    """Cliente para interactuar con la API del agente."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        Inicializa el cliente de la API.
        
        Args:
            base_url: URL base de la API
        """
        self.base_url = base_url.rstrip('/')
        
    def health_check(self) -> Dict[str, Any]:
        """Verificar el estado de salud de la API."""
        response = requests.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()
    
    def chat(self, message: str, thread_id: str = "default") -> Dict[str, Any]:
        """
        Enviar un mensaje al agente.
        
        Args:
            message: Mensaje para el agente
            thread_id: ID del hilo de conversación
            
        Returns:
            Respuesta del agente
        """
        data = {
            "message": message,
            "thread_id": thread_id
        }
        response = requests.post(f"{self.base_url}/chat", json=data)
        response.raise_for_status()
        return response.json()
    
    def get_conversation_history(self, thread_id: str) -> Dict[str, Any]:
        """
        Obtener el historial de una conversación.
        
        Args:
            thread_id: ID del hilo de conversación
            
        Returns:
            Historial de la conversación
        """
        response = requests.get(f"{self.base_url}/conversation/{thread_id}")
        response.raise_for_status()
        return response.json()
    
    def clear_conversation(self, thread_id: str) -> Dict[str, Any]:
        """
        Limpiar una conversación.
        
        Args:
            thread_id: ID del hilo de conversación
            
        Returns:
            Confirmación de limpieza
        """
        response = requests.delete(f"{self.base_url}/conversation/{thread_id}")
        response.raise_for_status()
        return response.json()
    
    def get_tools(self) -> Dict[str, Any]:
        """Obtener las herramientas disponibles."""
        response = requests.get(f"{self.base_url}/tools")
        response.raise_for_status()
        return response.json()


def test_basic_functionality():
    """Prueba la funcionalidad básica de la API."""
    print("🧪 Iniciando pruebas de la API del agente...")
    
    # Crear cliente
    client = AgentAPIClient()
    
    try:
        # 1. Verificar salud
        print("\n1️⃣ Verificando estado de salud...")
        health = client.health_check()
        print(f"✅ Estado: {health['status']}")
        print(f"✅ Agente listo: {health['agent_ready']}")
        print(f"✅ Versión: {health['version']}")
        
        # 2. Obtener herramientas
        print("\n2️⃣ Obteniendo herramientas disponibles...")
        tools = client.get_tools()
        print(f"✅ Herramientas disponibles: {len(tools['tools'])}")
        for tool in tools['tools']:
            print(f"   - {tool['name']}: {tool['description']}")
        
        # 3. Prueba de operación simple
        print("\n3️⃣ Prueba de operación simple...")
        thread_id = "test_simple"
        response = client.chat("Suma 15 y 25", thread_id)
        print(f"✅ Pregunta: Suma 15 y 25")
        print(f"✅ Respuesta: {response['response']}")
        print(f"✅ Herramientas usadas: {response['tools_used']}")
        
        # 4. Prueba de memoria (primera parte)
        print("\n4️⃣ Prueba de memoria - Parte 1...")
        thread_id = "test_memory"
        response1 = client.chat("Multiplica 6 por 7", thread_id)
        print(f"✅ Pregunta 1: Multiplica 6 por 7")
        print(f"✅ Respuesta 1: {response1['response']}")
        
        # 5. Prueba de memoria (segunda parte - debe recordar)
        print("\n5️⃣ Prueba de memoria - Parte 2...")
        response2 = client.chat("Ahora divide ese resultado entre 3", thread_id)
        print(f"✅ Pregunta 2: Ahora divide ese resultado entre 3")
        print(f"✅ Respuesta 2: {response2['response']}")
        
        # 6. Verificar historial
        print("\n6️⃣ Verificando historial de conversación...")
        history = client.get_conversation_history(thread_id)
        print(f"✅ Mensajes en el historial: {history['message_count']}")
        print(f"✅ Thread ID: {history['thread_id']}")
        
        # 7. Prueba de separación de threads
        print("\n7️⃣ Prueba de separación de threads...")
        thread_id_2 = "test_separate"
        response3 = client.chat("¿Cuál fue mi último cálculo?", thread_id_2)
        print(f"✅ Pregunta en thread nuevo: ¿Cuál fue mi último cálculo?")
        print(f"✅ Respuesta: {response3['response']}")
        print("✅ El agente no debería recordar cálculos de otros threads")
        
        # 8. Limpiar conversaciones de prueba
        print("\n8️⃣ Limpiando conversaciones de prueba...")
        client.clear_conversation(thread_id)
        client.clear_conversation(thread_id_2)
        print("✅ Conversaciones limpiadas")
        
        print("\n🎉 ¡Todas las pruebas completadas exitosamente!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar a la API. ¿Está el servidor ejecutándose?")
        print("   Inicia el servidor con: python app/main.py")
    except requests.exceptions.HTTPError as e:
        print(f"❌ Error HTTP: {e}")
        print("   Verifica que la API key de Google esté configurada correctamente")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


def interactive_chat():
    """Modo de chat interactivo con el agente."""
    print("💬 Modo de chat interactivo iniciado")
    print("Escribe 'salir' para terminar\n")
    
    client = AgentAPIClient()
    thread_id = f"interactive_{int(time.time())}"
    
    try:
        # Verificar que la API esté disponible
        client.health_check()
        
        while True:
            # Obtener mensaje del usuario
            user_input = input("👤 Tú: ").strip()
            
            if user_input.lower() in ['salir', 'exit', 'quit']:
                break
            
            if not user_input:
                continue
            
            try:
                # Enviar mensaje al agente
                response = client.chat(user_input, thread_id)
                print(f"🤖 Agente: {response['response']}")
                
                # Mostrar herramientas usadas si las hay
                if response['tools_used']:
                    print(f"🔧 Herramientas usadas: {response['tools_used']}")
                
                print()  # Línea en blanco
                
            except Exception as e:
                print(f"❌ Error: {e}\n")
    
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se puede conectar a la API. ¿Está el servidor ejecutándose?")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("👋 ¡Hasta luego!")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_chat()
    else:
        test_basic_functionality()