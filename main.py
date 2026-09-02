import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY missing in .env")

# -----------------------------
# Gemini + LlamaIndex Setup
# -----------------------------
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core import StorageContext, load_index_from_storage

# Configure global LlamaIndex settings
Settings.llm = GoogleGenAI(
    model="gemini-2.5-flash",
    api_key=API_KEY
)

Settings.embed_model = GoogleGenAIEmbedding(
    model_name="models/gemini-embedding-001",
    api_key=API_KEY
)

# -----------------------------
# Load documents
# -----------------------------
def load_docs():
    try:
        docs = SimpleDirectoryReader("knowledge_base").load_data()
        if not docs:
            raise RuntimeError("❌ No documents found in knowledge_base/")
        return docs
    except Exception as e:
        raise RuntimeError(f"❌ Failed to load documents: {e}")

# -----------------------------
# Build & persist index (first run)
# -----------------------------
def build_index():
    docs = load_docs()
    index = VectorStoreIndex.from_documents(docs)
    index.storage_context.persist("./storage")
    print("✅ Index built and persisted to ./storage")
    return index

# -----------------------------
# Load existing index (subsequent runs)
# -----------------------------
def load_existing_index():
    try:
        ctx = StorageContext.from_defaults(persist_dir="./storage")
        index = load_index_from_storage(ctx)
        print("✅ Loaded existing index from ./storage")
        return index
    except Exception as e:
        print(f"⚠️ Could not load existing index: {e}")
        print("➡️ Rebuilding index instead...")
        return build_index()

# -----------------------------
# Query Engine
# -----------------------------
def query_index(query: str):
    index = load_existing_index()
    engine = index.as_query_engine()
    response = engine.query(query)
    return str(response)

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    print("🚀 Running Gemini + LlamaIndex RAG System")

    # Example query
    answer = query_index(input("Enter your query: "))
    print("\n📘 Response:")
    print(answer)
