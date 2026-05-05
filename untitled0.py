import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Configuración de página
st.set_page_config(page_title="ArqAI Chile", layout="wide")
st.title("🏗️ ArqAI: Consultor Arquitectónico")

# 1. Configurar la API Key
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Introduce tu Gemini API Key:", type="password")
    st.info("Consíguela en: [Google AI Studio](https://aistudio.google.com/)")

if api_key:
    try:
        # Configuración forzada
        genai.configure(api_key=api_key)
        
        # Usamos el nombre base del modelo más estable
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 2. Interfaz de usuario
        archivo = st.file_uploader("Sube la foto de la zona", type=["jpg", "jpeg", "png"])
        comando = st.text_input("¿Qué quieres construir?", "Haz una cancha de tenis")
        
        if archivo and st.button("🚀 Generar Propuesta Técnica"):
            img = Image.open(archivo)
            
            with st.spinner("El arquitecto IA está analizando la imagen..."):
                # Formato de mensaje explícito para evitar errores de versión
                prompt_parts = [
                    f"Actúa como arquitecto experto. Rediseña según: {comando}. "
                    "Detalla estructura, estabilidad y materiales necesarios.",
                    img
                ]
                
                # Ejecución de la consulta
                response = model.generate_content(prompt_parts)
                
                if response.text:
                    st.subheader("📋 Propuesta Técnica")
                    st.success("Análisis completado con éxito")
                    st.markdown(response.text)
                else:
                    st.error("La IA no pudo generar una respuesta. Intenta con otra imagen.")
                    
    except Exception as e:
        # Si el error 404 persiste, imprimimos un mensaje útil
        if "404" in str(e):
            st.error("Error 404: El modelo no fue encontrado. Por favor, genera una API KEY NUEVA en Google AI Studio dentro de un proyecto nuevo.")
        else:
            st.error(f"Error del sistema: {e}")
else:
    st.warning("👈 Ingresa tu API Key para comenzar.")
