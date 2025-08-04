"""
Ejemplo de uso directo del agente con memoria.

Este script demuestra cómo usar el agente directamente sin la API REST,
útil para integración en otras aplicaciones Python.
"""

import os
from agente.memory_agent import MemoryAgent

def ejemplo_basico():
    """Ejemplo básico de uso del agente."""
    print("🤖 Ejemplo básico del Agente con Memoria")
    print("=" * 45)
    
    # Verificar API key
    if not os.environ.get("GOOGLE_API_KEY"):
        print("❌ Por favor, configura GOOGLE_API_KEY en tus variables de entorno")
        return
    
    # Crear agente
    print("📝 Creando agente...")
    agent = MemoryAgent()
    print("✅ Agente creado exitosamente")
    
    # ID del hilo de conversación
    thread_id = "ejemplo_basico"
    
    # Primera interacción
    print("\n💬 Primera interacción:")
    respuesta1 = agent.chat("Suma 12 y 8", thread_id)
    print(f"👤 Usuario: Suma 12 y 8")
    print(f"🤖 Agente: {respuesta1['response']}")
    print(f"🔧 Herramientas usadas: {respuesta1['tools_used']}")
    
    # Segunda interacción (debe recordar)
    print("\n💬 Segunda interacción:")
    respuesta2 = agent.chat("Multiplica ese resultado por 3", thread_id)
    print(f"👤 Usuario: Multiplica ese resultado por 3")
    print(f"🤖 Agente: {respuesta2['response']}")
    print(f"🔧 Herramientas usadas: {respuesta2['tools_used']}")
    
    # Tercera interacción (debe recordar toda la conversación)
    print("\n💬 Tercera interacción:")
    respuesta3 = agent.chat("¿Cuáles han sido todos los cálculos que hemos hecho?", thread_id)
    print(f"👤 Usuario: ¿Cuáles han sido todos los cálculos que hemos hecho?")
    print(f"🤖 Agente: {respuesta3['response']}")
    
    # Mostrar historial
    print("\n📖 Historial de conversación:")
    historial = agent.get_conversation_history(thread_id)
    for i, mensaje in enumerate(historial):
        tipo = "👤 Usuario" if mensaje["type"] == "human" else "🤖 Agente"
        print(f"  {i+1}. {tipo}: {mensaje['content']}")


def ejemplo_conversaciones_multiples():
    """Ejemplo con múltiples conversaciones simultáneas."""
    print("\n\n🔀 Ejemplo de conversaciones múltiples")
    print("=" * 45)
    
    if not os.environ.get("GOOGLE_API_KEY"):
        print("❌ Por favor, configura GOOGLE_API_KEY en tus variables de entorno")
        return
    
    # Crear agente
    agent = MemoryAgent()
    
    # Conversación 1: Matemáticas básicas
    thread1 = "matematicas_basicas"
    print(f"\n💬 Conversación 1 (Thread: {thread1}):")
    resp1 = agent.chat("Suma 5 y 7", thread1)
    print(f"🤖 {resp1['response']}")
    
    # Conversación 2: Multiplicaciones
    thread2 = "multiplicaciones"
    print(f"\n💬 Conversación 2 (Thread: {thread2}):")
    resp2 = agent.chat("Multiplica 4 por 6", thread2)
    print(f"🤖 {resp2['response']}")
    
    # Continuar conversación 1
    print(f"\n💬 Continuando conversación 1:")
    resp3 = agent.chat("Divide ese resultado entre 2", thread1)
    print(f"🤖 {resp3['response']}")
    
    # Continuar conversación 2
    print(f"\n💬 Continuando conversación 2:")
    resp4 = agent.chat("Suma 10 a ese resultado", thread2)
    print(f"🤖 {resp4['response']}")
    
    # Verificar que las conversaciones son independientes
    print(f"\n🔍 Verificando independencia:")
    resp5 = agent.chat("¿Cuál fue mi primer cálculo?", thread1)
    print(f"Thread 1 - 🤖 {resp5['response']}")
    
    resp6 = agent.chat("¿Cuál fue mi primer cálculo?", thread2)
    print(f"Thread 2 - 🤖 {resp6['response']}")


def ejemplo_manejo_errores():
    """Ejemplo de manejo de errores."""
    print("\n\n⚠️ Ejemplo de manejo de errores")
    print("=" * 45)
    
    if not os.environ.get("GOOGLE_API_KEY"):
        print("❌ Por favor, configura GOOGLE_API_KEY en tus variables de entorno")
        return
    
    agent = MemoryAgent()
    thread_id = "errores"
    
    # Intentar división por cero
    print("\n💬 Probando división por cero:")
    respuesta = agent.chat("Divide 10 entre 0", thread_id)
    print(f"🤖 {respuesta['response']}")
    
    # Operación normal después del error
    print("\n💬 Operación normal después del error:")
    respuesta = agent.chat("Suma 15 y 25", thread_id)
    print(f"🤖 {respuesta['response']}")


def ejemplo_interactivo():
    """Modo interactivo simple."""
    print("\n\n🎮 Modo interactivo")
    print("=" * 45)
    print("Escribe 'salir' para terminar")
    
    if not os.environ.get("GOOGLE_API_KEY"):
        print("❌ Por favor, configura GOOGLE_API_KEY en tus variables de entorno")
        return
    
    agent = MemoryAgent()
    thread_id = "interactivo"
    
    while True:
        try:
            mensaje = input("\n👤 Tú: ").strip()
            
            if mensaje.lower() in ['salir', 'exit', 'quit']:
                break
            
            if not mensaje:
                continue
            
            respuesta = agent.chat(mensaje, thread_id)
            print(f"🤖 Agente: {respuesta['response']}")
            
            if respuesta['tools_used']:
                print(f"🔧 Herramientas: {respuesta['tools_used']}")
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n👋 ¡Hasta luego!")


if __name__ == "__main__":
    # Verificar configuración
    if not os.environ.get("GOOGLE_API_KEY"):
        print("⚠️ GOOGLE_API_KEY no está configurada")
        print("\n💡 Configúrala con uno de estos métodos:")
        print("1. Variable de entorno: export GOOGLE_API_KEY=tu_clave")
        print("2. Archivo .env en el directorio del proyecto")
        print("3. Configurarla ahora:")
        
        api_key = input("\n🔑 Ingresa tu Google API Key (o Enter para salir): ").strip()
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key
        else:
            print("❌ Sin API key no se puede continuar")
            exit(1)
    
    print("🚀 Ejemplos de uso del Agente con Memoria")
    print("="*50)
    
    try:
        # Ejecutar ejemplos
        ejemplo_basico()
        ejemplo_conversaciones_multiples()
        ejemplo_manejo_errores()
        
        # Preguntar si quiere modo interactivo
        respuesta = input("\n🎮 ¿Quieres probar el modo interactivo? (s/n): ").lower()
        if respuesta in ['s', 'si', 'y', 'yes']:
            ejemplo_interactivo()
        
        print("\n✅ ¡Ejemplos completados!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Asegúrate de que:")
        print("- La API key de Google esté configurada correctamente")
        print("- Todas las dependencias estén instaladas (pip install -r requirements.txt)")
        print("- Tengas conexión a internet")