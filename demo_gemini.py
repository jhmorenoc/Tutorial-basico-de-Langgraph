#!/usr/bin/env python3
"""
Demo script que muestra cómo usar Gemini Flash
"""

import os
import getpass

def _set_env(var: str):
    """Función para configurar variables de entorno de forma segura"""
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

def main():
    print("🤖 Demo de Gemini Flash")
    print("=" * 30)
    
    # 1. Configurar API key si no existe
    print("📋 Configurando Google API Key...")
    _set_env("GOOGLE_API_KEY")
    print("✅ Google API Key configurada")
    
    # 2. Importar y configurar Gemini
    print("\n🚀 Configurando Gemini Flash...")
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.7
        )
        print("✅ Gemini Flash configurado")
        
    except ImportError:
        print("❌ Error: langchain-google-genai no instalado")
        print("🔧 Instala con: pip install langchain-google-genai")
        return
    except Exception as e:
        print(f"❌ Error al configurar Gemini: {e}")
        return
    
    # 3. Demo interactivo
    print("\n💬 Demo Interactivo - Escribe 'salir' para terminar")
    print("-" * 50)
    
    while True:
        try:
            # Obtener input del usuario
            user_input = input("\n🧑 Tú: ").strip()
            
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("👋 ¡Hasta luego!")
                break
            
            if not user_input:
                continue
            
            # Enviar a Gemini
            print("🤖 Gemini: ", end="", flush=True)
            
            try:
                response = llm.invoke(user_input)
                print(response.content)
                
            except Exception as e:
                print(f"❌ Error al consultar Gemini: {e}")
                print("💡 Verifica tu conexión a internet y API key")
        
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")

if __name__ == "__main__":
    main() 