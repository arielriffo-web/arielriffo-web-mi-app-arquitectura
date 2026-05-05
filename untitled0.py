import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="ArqAI Chile", layout="wide")
st.title("🏗️ ArqAI: Consultor Arquitectónico")

with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Introduce tu Gemini API Key:", type="password")
    st.info("Consíguela en: aistudio.google.com")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # En Chile, esta es la versión que mejor responde sin dar 404:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        
        archivo = st.file_uploader("Sube la foto de la zona", type=["jpg", "jpeg", "png"])
        comando = st.text_input("¿Qué quieres construir?", "Haz una cancha de tenis")
        
        if archivo and st.button("🚀 Generar Propuesta Técnica"):
            img = Image.open(archivo)
            
            with st.spinner("Analizando terreno y materiales para Chile..."):
                # Enviamos las partes de forma explícita
                contenido = [
                    "Eres un ingeniero civil y arquitecto experto en Chile. "
                    f"Rediseña la zona de la imagen según: {comando}. "
                    "Indica materiales realizables y estabilidad estructural.",
                    img
                ]
                
                response = model.generate_content(contenido)
                st.subheader("📋 Propuesta Técnica")
                st.markdown(response.text)
                
    except Exception as e:
        # Esto nos dirá si el error es de la clave o del modelo
        st.error(f"Aviso del sistema: {e}")
else:
    st.warning("Introduce tu API Key en la izquierda.")
