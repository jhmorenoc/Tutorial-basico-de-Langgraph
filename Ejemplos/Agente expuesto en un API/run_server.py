"""
Script para ejecutar el servidor de la API del agente con memoria.

Este script facilita el inicio del servidor con configuración personalizada
y proporciona un punto de entrada único para la aplicación.
"""

import os
import sys
import uvicorn
from pathlib import Path

# Agregar el directorio actual al path para las importaciones
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def load_env_file():
    """Cargar variables de entorno desde archivo .env si existe."""
    env_file = current_dir / ".env"
    if env_file.exists():
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)
            print(f"✅ Variables de entorno cargadas desde {env_file}")
        except ImportError:
            print("⚠️ python-dotenv no está instalado. Variables de entorno .env no cargadas.")
            print("   Instalar con: pip install python-dotenv")
    else:
        print(f"ℹ️ No se encontró archivo .env en {env_file}")
        print("   Puedes crear uno basándote en .env.example")

def check_requirements():
    """Verificar que los requisitos mínimos estén disponibles."""
    missing_modules = []
    
    try:
        import fastapi
    except ImportError:
        missing_modules.append("fastapi")
    
    try:
        import uvicorn
    except ImportError:
        missing_modules.append("uvicorn")
    
    try:
        import langchain_google_genai
    except ImportError:
        missing_modules.append("langchain-google-genai")
    
    try:
        import langgraph
    except ImportError:
        missing_modules.append("langgraph")
    
    if missing_modules:
        print("❌ Faltan dependencias requeridas:")
        for module in missing_modules:
            print(f"   - {module}")
        print("\n💡 Instalar con: pip install -r requirements.txt")
        return False
    
    return True

def check_api_key():
    """Verificar que la API key de Google esté configurada."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("❌ GOOGLE_API_KEY no está configurada")
        print("\n🔧 Configúrala de una de estas formas:")
        print("   1. Variable de entorno: export GOOGLE_API_KEY=tu_clave")
        print("   2. Archivo .env (ver .env.example)")
        print("   3. Configúrala ahora mismo:")
        
        api_key = input("   Ingresa tu Google API Key: ").strip()
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key
            print("✅ API Key configurada temporalmente")
            return True
        else:
            print("❌ No se proporcionó API Key")
            return False
    else:
        # Mostrar solo los primeros y últimos caracteres por seguridad
        masked_key = api_key[:8] + "..." + api_key[-4:]
        print(f"✅ Google API Key encontrada: {masked_key}")
        return True

def main():
    """Función principal para ejecutar el servidor."""
    print("🚀 Iniciando servidor del Agente con Memoria API")
    print("=" * 50)
    
    # Cargar variables de entorno
    load_env_file()
    
    # Verificar requisitos
    if not check_requirements():
        sys.exit(1)
    
    # Verificar API key
    if not check_api_key():
        sys.exit(1)
    
    # Configuración del servidor
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))
    reload = os.environ.get("RELOAD", "true").lower() == "true"
    log_level = os.environ.get("LOG_LEVEL", "info")
    
    print("\n📋 Configuración del servidor:")
    print(f"   Host: {host}")
    print(f"   Puerto: {port}")
    print(f"   Recarga automática: {reload}")
    print(f"   Nivel de log: {log_level}")
    
    print("\n🌐 URLs disponibles:")
    print(f"   API: http://{host}:{port}")
    print(f"   Docs: http://{host}:{port}/docs")
    print(f"   ReDoc: http://{host}:{port}/redoc")
    
    print("\n💡 Para probar la API:")
    print("   python test_api.py                    # Pruebas automáticas")
    print("   python test_api.py --interactive      # Chat interactivo")
    
    print("\n" + "=" * 50)
    print("🟢 Iniciando servidor...")
    
    try:
        # Ejecutar el servidor
        uvicorn.run(
            "app.main:app",
            host=host,
            port=port,
            reload=reload,
            log_level=log_level,
            access_log=True
        )
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor detenido por el usuario")
    except Exception as e:
        print(f"\n❌ Error al iniciar el servidor: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()