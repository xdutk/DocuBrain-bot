import os
import google.generativeai as genai
from pypdf import PdfReader
import getpass 

# Configuración de generación
GENERATION_CONFIG = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

def extract_text_from_pdf(pdf_path):
    """Lee el PDF."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        print(f"📄 Leyendo '{pdf_path}'... ({len(reader.pages)} páginas)")
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"❌ Error leyendo el PDF: {e}")
        return None

def main():
    print("🤖 --- BIENVENIDO A DOCUBRAIN (CLI Edition) ---")
    
    # 1. PEDIR API KEY (Seguridad: No la guardamos en código)
    try:
        api_key = getpass.getpass("🔑 Ingresa tu Gemini API Key (Input oculto): ").strip()
    except:
        api_key = input("🔑 Ingresa tu Gemini API Key: ").strip()

    if not api_key:
        print("❌ Necesitas una API Key para continuar.")
        return

    # 2. Configurar Gemini en tiempo de ejecución
    try:
        genai.configure(api_key=api_key)
        # Inicializamos el modelo AQUÍ, después de tener la clave
        model = genai.GenerativeModel(
            model_name="gemini-flash-latest", # O "gemini-2.0-flash" si tu cuenta lo permite
            generation_config=GENERATION_CONFIG,
        )
    except Exception as e:
        print(f"❌ Error de configuración: {e}")
        return

    # 3. Pedir archivo
    pdf_input = input("📂 Arrastra tu archivo PDF aquí y dale Enter: ").strip()
    pdf_path = pdf_input.replace('"', '').replace("'", "")
    
    # 4. Extraer texto
    document_text = extract_text_from_pdf(pdf_path)
    
    if not document_text:
        print("⚠️ El PDF parece estar vacío o no se pudo leer.")
        return

    print("\n✅ Documento analizado. ¡Pregúntame lo que quieras!")
    print("(Escribe 'salir' para terminar)\n")

    # 5. Iniciar Chat
    try:
        chat = model.start_chat(history=[
            {
                "role": "user",
                "parts": [f"Analiza este documento y responde basándote SOLO en él:\n\n{document_text}"]
            },
            {
                "role": "model",
                "parts": ["Entendido. Responderé preguntas basándome únicamente en el documento proporcionado."]
            }
        ])

        while True:
            question = input("Tú: ")
            if question.lower() in ['salir', 'exit', 'bye']:
                break
                
            try:
                print("Thinking...", end="\r")
                response = chat.send_message(question)
                print(f"🤖 Gemini: {response.text}\n")
            except Exception as e:
                print(f"⚠️ Error: {e}")

    except Exception as e:
        print(f"❌ Error al iniciar el chat (Revisa tu API Key): {e}")

if __name__ == "__main__":
    main()