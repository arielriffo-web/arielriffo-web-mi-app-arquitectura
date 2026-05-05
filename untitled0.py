import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración visual de la App
st.set_page_config(page_title="ArqAI - Rediseño Estructural", layout="wide")

st.title("🏗️ ArqAI: Consultor de Rediseño Arquitectónico")
st.markdown("""
Esta herramienta utiliza **Inteligencia Artificial Multimodal** para analizar estructuras y proponer 
rediseños detallados, incluyendo estabilidad y materiales.
""")

# 2. Configuración de la API Key (Barra lateral)
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Introduce tu Gemini API Key:", type="password")
    st.info("Obtén tu clave gratis en: [Google AI Studio](https://aistudio.google.com/)")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 3. Interfaz de carga
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📸 Carga tu imagen")
            archivo_subido = st.file_uploader("Sube una foto de la zona a rediseñar", type=["jpg", "jpeg", "png"])
            comando = st.text_area("Instrucciones de rediseño:", 
                                  placeholder="Ejemplo: Rediseña este patio trasero para que sea una oficina minimalista de cristal con estructura de acero.")
        
        if archivo_subido is not None:
            imagen = Image.open(archivo_subido)
            st.image(imagen, caption="Imagen cargada con éxito", use_container_width=True)
            
            if st.button("🚀 Generar Propuesta Técnica"):
                with st.spinner("Analizando geometría y materiales..."):
                    # El PROMPT corregido para que sea profesional
                    prompt_instruccion = f"""
                    Actúa como un Arquitecto e Ingeniero Estructural. Analiza la imagen adjunta y el siguiente comando del usuario: '{comando}'.
                    
                    Proporciona una respuesta técnica dividida en:
                    1.  **CONCEPTO DE DISEÑO**: Describe la nueva estética y funcionalidad.
                    2.  **ESTRUCTURA Y ESTABILIDAD**: Explica cómo se sostendrá la estructura, puntos de apoyo necesarios y consideraciones de carga.
                    3.  **LISTA DE MATERIALES**: Recomienda materiales específicos (resistencia del concreto, tipos de perfiles de acero, tipos de vidrio, etc.) para que el proyecto sea viable.
                    4.  **RECOMENDACIÓN TÉCNICA**: Un consejo sobre
