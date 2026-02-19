# 🧠 DocuBrain: AI-Powered PDF Assistant

**DocuBrain** is a Retrieval-Augmented Generation (RAG) tool that allows users to chat with their PDF documents instantly. Built with Python and powered by Google's **Gemini 2.0 Flash** model, it processes documents in seconds and provides accurate, context-aware answers.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Gemini%20Flash-8E75B2?style=for-the-badge&logo=google&logoColor=white)

## 🚀 Key Features

- **Dual Interface:**
  - 🖥️ **CLI Tool:** Fast and minimalist terminal interface for developers.
  - 🌐 **Web App:** Modern, drag-and-drop interface built with Streamlit.
- **Instant Analysis:** Ingests entire PDFs using Gemini's large context window (no vector DB required for standard docs).
- **Secure by Design:** Runs locally; API keys are never stored in the code.
- **Cost-Effective:** Optimized for the Gemini Flash tier.

<img width="1859" height="797" alt="Captura de pantalla 2026-02-18 225217" src="https://github.com/user-attachments/assets/cfe20e79-3373-4823-adb5-0ac0a3c80046" />


## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/TU_USUARIO/DocuBrain.git](https://github.com/TU_USUARIO/DocuBrain.git)
   cd DocuBrain
   ```

2. Create a Virtual Environment:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. Install Dependencies:

```bash
pip install -r requirements.txt
```

📖 Usage

Option 1: Web Interface (Recommended)

Launch the interactive web app:

```bash
streamlit run app.py
```

The app will open in your default browser.

Option 2: Terminal Mode (CLI)

Run the script directly in your console:

```bash
python cli_tool.py
```

🔑 Configuration

To use this tool, you need a Google Gemini API Key.

Get it for free at Google AI Studio.

When you run the app, you will be prompted to enter your key securely.

🤖 Tech Stack

Core: Python 3.12

AI Model: Google Gemini 2.0 Flash

PDF Processing: PyPDF

Frontend: Streamlit

Developed by xdutk.
