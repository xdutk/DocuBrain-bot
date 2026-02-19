import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# Configuración de la página
st.set_page_config(page_title="DocuBrain AI", page_icon="🧠", layout="wide")

st.title("🧠 DocuBrain: Tu Analista de Documentos con IA")
st.markdown("Sube un PDF y hazle preguntas. Potenciado por **Gemini 2.0 Flash**.")

# Barra lateral para la API Key
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Ingresa tu Gemini API Key", type="password")
    st.markdown("---")
    st.markdown("Desarrollado por **xdutk**")

# Función para leer PDF
def get_pdf_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# Subida de archivo
uploaded_file = st.file_uploader("Arrastra tu PDF aquí", type=["pdf"])

if uploaded_file and api_key:
    # Procesamiento
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-flash-latest") # Usamos el alias universal
        
        # Leemos el PDF una sola vez y lo guardamos en cache
        if "pdf_content" not in st.session_state:
            with st.spinner("Analizando documento..."):
                text = get_pdf_text(uploaded_file)
                st.session_state.pdf_content = text
                st.session_state.chat_history = [] # Reiniciamos chat
                st.success("¡Documento procesado!")

        # Historial de Chat
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Mostrar mensajes anteriores
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        # Input del usuario
        user_question = st.chat_input("Pregunta algo sobre el documento...")
        
        if user_question:
            # 1. Mostrar pregunta usuario
            st.session_state.chat_history.append({"role": "user", "content": user_question})
            with st.chat_message("user"):
                st.write(user_question)

            # 2. Generar respuesta
            with st.chat_message("assistant"):
                with st.spinner("Pensando..."):
                    prompt = f"Basado en este texto: {st.session_state.pdf_content[:50000]}... Responde: {user_question}"
                    response = model.generate_content(prompt)
                    st.write(response.text)
                    st.session_state.chat_history.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Error: {e}")

elif uploaded_file and not api_key:
    st.warning("⚠️ Por favor ingresa tu API Key en la barra lateral para continuar.")