# 📘 **Gemini 2.5 Flash + LlamaIndex RAG System**

A production‑ready **Retrieval‑Augmented Generation (RAG)** pipeline built using:

- **Google Gemini 2.5 Flash** (LLM)
- **Gemini Embedding 001**
- **LlamaIndex** (indexing, storage, querying)
- **Python 3.10+**
- **Persistent vector storage**

This project loads documents from a `knowledge_base/` directory, builds a vector index, persists it to disk, and enables fast semantic querying using Gemini.

---

## 🚀 **Features**

- Semantic search over your documents  
- Powered by Gemini 2.5 Flash  
- Automatic document loading  
- Persistent vector index (`./storage`)  
- Environment‑based API key management  
- Modular architecture ready for expansion (FastAPI, Streamlit, Docker)

---

## 📁 **Project Structure**

    your-project/
    │
    ├── knowledge_base/        # Place your .txt, .md, .pdf, .docx files here
    │
    ├── storage/               # Auto-created after first run (vector index)
    │
    ├── main.py                # Main RAG pipeline
    ├── requirements.txt       # Python dependencies
    └── .env                   # Gemini API key

---

## 🔧 **Prerequisites**

- Python 3.10+
- A Gemini API key from Google AI Studio
- PowerShell execution policy allowing venv activation:

    Set-ExecutionPolicy RemoteSigned

---

## 📦 **Installation**

### 1. Clone the repository

    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>

### 2. Create and activate a virtual environment

    python -m venv venv
    venv\Scripts\activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Add your Gemini API key

Create a `.env` file:

    GEMINI_API_KEY=your_api_key_here

### 5. Add documents

Place any `.txt`, `.md`, `.pdf`, `.docx`, or `.html` files inside:

    knowledge_base/

---

## ▶️ **Running the Project**

### First run — build and persist the index

    python main.py

This will:

- Load documents  
- Build a vector index  
- Save it to `./storage`  
- Run a sample query  

### Subsequent runs — load the saved index

    python main.py

The system automatically loads the existing index for fast startup.

---

## 🧩 **How It Works**

### 1. Document Loading

LlamaIndex reads all files in `knowledge_base/`.

### 2. Embedding

Documents are embedded using:

    models/gemini-embedding-001

### 3. Indexing

A `VectorStoreIndex` is created and persisted.

### 4. Query Engine

Queries are answered using **Gemini 2.5 Flash**.

---

## 🛠️ **Technologies Used**

- Python  
- LlamaIndex  
- Google Gemini (google-genai SDK)  
- python-dotenv  
- VectorStoreIndex  

---

## 📈 **Future Improvements**

- FastAPI API endpoint  
- Streamlit UI  
- Unit tests  
- Docker container  
- Cloud deployment (GCP / Azure)  

---

## 🤝 **Contributing**

Pull requests are welcome.  
For major changes, please open an issue first to discuss what you’d like to modify.

---

## 📜 **License**

This project is licensed under the **MIT License**.
