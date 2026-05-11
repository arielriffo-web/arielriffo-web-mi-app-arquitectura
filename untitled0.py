import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración de página
st.set_page_config(page_title="ArqAI Chile", layout="wide")
st.title("🏗️ ArqAI: Consultor Arquitectónico")

# 1. Configurar la API Key de forma directa (¡La tuya ya está guardada aquí!)
API_KEY_POR_DEFECTO = "AIzaSyAjNQLOyAb5ToEAdxQulFc18jGjONbuSMM"

# 2. Barra lateral simplificada (ya no necesitas escribir la clave)
with st.sidebar:
    st.header("Configuración")
    st.success("🔑 API Key cargada con éxito por el sistema.")
    st.info("Desarrollado para el proyecto final de Informática.")

# Activamos el cerebro de la aplicación usando tu clave
try:
    genai.configure(api_key=API_KEY_POR_DEFECTO)
    
    # Usamos la llamada al modelo estándar para la versión de librería moderna
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 3. Interfaz de usuario para subir archivos y comandos
    archivo = st.file_uploader("Sube la foto de la zona", type=["jpg", "jpeg", "png"])
    comando = st.text_input("¿Qué quieres construir?", "Haz una cancha de tenis")
    
    if archivo and st.button("🚀 Generar Propuesta Técnica"):
        img = Image.open(archivo)
        
        with st.spinner("El arquitecto IA está analizando la imagen..."):
            # Formato de mensaje explícito compatible con Gemini en Chile
            prompt_parts = [
                f"Actúa como arquitecto e ingeniero experto en Chile. Rediseña la zona de la imagen según esta instrucción: '{comando}'. "
                "Detalla la estructura, la estabilidad y los materiales necesarios de manera muy realista.",
                img
            ]
            
            response = model.generate_content(prompt_parts)
            
            if response.text:
                st.subheader("📋 Propuesta Técnica")
                st.success("Análisis completado con éxito")
                st.markdown(response.text)
            else:
                st.error("La IA no pudo procesar la imagen. Intenta con un formato diferente.")
                
except Exception as e:
    # Captura cualquier error de versión o clave
    if "404" in str(e):
        st.error("Error de conexión (404). Por favor, asegúrate de que tu 'requirements.txt' esté actualizado y haz un 'Reboot App' en Streamlit.")
    else:
        st.error(f"Error del sistema: {e}")
