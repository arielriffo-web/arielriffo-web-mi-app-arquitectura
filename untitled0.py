import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="ArqAI", layout="wide")
st.title("🏗️ ArqAI: Consultor")

with st.sidebar:
    api_key = st.text_input("Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Usamos el nombre de modelo más estándar y estable
        model = genai.GenerativeModel('gemini-1.5-flash-latest') 
        
        archivo = st.file_uploader("Sube tu imagen", type=["jpg", "png", "jpeg"])
        comando = st.text_input("Comando:", "Rediseño moderno")
        
        if archivo and st.button("Generar Propuesta"):
            img = Image.open(archivo)
            # Simplificamos el envío para evitar errores de versión
            response = model.generate_content([comando, img])
            st.markdown(response.text)
            
    except Exception as e:
        st.error(f"Error técnico: {e}")
else:
    st.info("Introduce la API Key")
