"""
Script de configuración inicial para el proyecto del Agente con Memoria API.

Este script ayuda a configurar el entorno y verificar que todo esté listo
para ejecutar la API del agente.
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    """Imprimir encabezado del script."""
    print("🤖 Setup del Agente con Memoria API")
    print("=" * 40)

def check_python_version():
    """Verificar la versión de Python."""
    print("🐍 Verificando versión de Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} (compatible)")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} (requiere 3.8+)")
        return False

def install_dependencies():
    """Instalar dependencias del proyecto."""
    print("\n📦 Instalando dependencias...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print("❌ Archivo requirements.txt no encontrado")
        return False
    
    try:
        # Actualizar pip primero
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                      check=True, capture_output=True)
        print("✅ pip actualizado")
        
        # Instalar dependencias
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", str(requirements_file)], 
                               check=True, capture_output=True, text=True)
        print("✅ Dependencias instaladas correctamente")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar dependencias: {e}")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        return False

def setup_environment_file():
    """Configurar archivo de variables de entorno."""
    print("\n🔧 Configurando variables de entorno...")
    
    env_file = Path(__file__).parent / ".env"
    env_example_file = Path(__file__).parent / ".env.example"
    
    if env_file.exists():
        print("✅ Archivo .env ya existe")
        return True
    
    print("📝 Creando archivo .env...")
    
    # Solicitar API key
    print("\n🔑 Necesitas una Google API Key para usar Gemini:")
    print("   1. Ve a https://makersuite.google.com/")
    print("   2. Crea una nueva API key")
    print("   3. Cópiala y pégala aquí")
    
    api_key = input("\n   Ingresa tu Google API Key (o presiona Enter para configurar después): ").strip()
    
    # Crear archivo .env
    env_content = f"""# Configuración del Agente con Memoria API

# API Key de Google Gemini (REQUERIDO)
GOOGLE_API_KEY={api_key if api_key else 'tu_clave_api_de_google_aqui'}

# Configuración del servidor (OPCIONAL)
HOST=0.0.0.0
PORT=8000
RELOAD=true
LOG_LEVEL=info
"""
    
    try:
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(env_content)
        
        if api_key:
            print("✅ Archivo .env creado con tu API key")
        else:
            print("⚠️ Archivo .env creado - necesitas agregar tu API key")
            print(f"   Edita el archivo: {env_file}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error al crear archivo .env: {e}")
        return False

def verify_installation():
    """Verificar que la instalación sea correcta."""
    print("\n🧪 Verificando instalación...")
    
    required_modules = [
        "fastapi",
        "uvicorn", 
        "langchain_google_genai",
        "langgraph",
        "pydantic"
    ]
    
    missing_modules = []
    
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError:
            print(f"❌ {module}")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n❌ Faltan módulos: {', '.join(missing_modules)}")
        return False
    else:
        print("\n✅ Todos los módulos requeridos están disponibles")
        return True

def show_next_steps():
    """Mostrar los siguientes pasos."""
    print("\n🎉 ¡Configuración completada!")
    print("\n📋 Siguientes pasos:")
    print("   1. Asegúrate de que tu GOOGLE_API_KEY esté configurada en .env")
    print("   2. Ejecuta el servidor:")
    print("      python run_server.py")
    print("   3. Prueba la API:")
    print("      python test_api.py")
    print("   4. Modo interactivo:")
    print("      python test_api.py --interactive")
    print("\n🌐 URLs una vez iniciado el servidor:")
    print("   • API: http://localhost:8000")
    print("   • Documentación: http://localhost:8000/docs")
    print("   • ReDoc: http://localhost:8000/redoc")

def main():
    """Función principal del setup."""
    print_header()
    
    # Verificar Python
    if not check_python_version():
        print("\n❌ Actualiza Python a la versión 3.8 o superior")
        sys.exit(1)
    
    # Instalar dependencias
    if not install_dependencies():
        print("\n❌ Error en la instalación de dependencias")
        sys.exit(1)
    
    # Configurar entorno
    setup_environment_file()
    
    # Verificar instalación
    if not verify_installation():
        print("\n❌ Verificación fallida - revisa la instalación")
        sys.exit(1)
    
    # Mostrar siguientes pasos
    show_next_steps()

if __name__ == "__main__":
    main()