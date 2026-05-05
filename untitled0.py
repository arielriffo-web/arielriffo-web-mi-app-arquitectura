import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de la App
st.set_page_config(page_title="ArqAI - Consultor Arquitectónico", layout="wide")

st.title("🏗️ ArqAI: Rediseño Estructural")
st.write("Sube una foto y deja que la IA actúe como arquitecto e ingeniero.")

# 2. Configuración de la API Key en la barra lateral
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Introduce tu Gemini API Key:", type="password")
    st.info("Obtén tu clave en: [Google AI Studio](https://aistudio.google.com/)")

# 3. Lógica principal
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            archivo = st.file_uploader("Carga la imagen de la zona", type=["jpg", "png", "jpeg"])
            comando = st.text_area("¿Qué quieres hacer?", "Diseña una terraza moderna con vigas de acero y madera.")
        
        if archivo is not None:
            img = Image.open(archivo)
            st.image(img, caption="Imagen Original", use_container_width=True)
            
            if st.button("🚀 Generar Propuesta"):
                with st.spinner("El ingeniero está analizando..."):
                    # El bloque del texto (Prompt) bien cerrado
                    prompt = f"""
                    Actúa como Arquitecto e Ingeniero.
                    Analiza la imagen y rediseña según: {comando}.
                    
                    Entrega:
                    1. Diseño: Descripción estética.
                    2. Estabilidad: Cómo se apoya y soporta el peso.
                    3. Materiales: Lista detallada para construcción real.
                    """
                    
                    response = model.generate_content([prompt, img])
                    
                    with col2:
                        st.subheader("📋 Propuesta Técnica")
                        st.markdown(response.text)
                        
    except Exception as e:
        st.error(f"Error de conexión: {e}")
else:
    st.warning("👈 Introduce tu clave API para empezar.")
