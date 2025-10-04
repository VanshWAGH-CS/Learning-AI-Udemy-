from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize embedding model
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

# Connect to existing Qdrant collection
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

def process_query(query: str):
    # Perform similarity search
    search_results = vector_db.similarity_search(query, k=5)

    # Prepare context from retrieved docs
    context = "\n\n\n".join([
        f"Page content: {result.page_content}\n"
        f"Page Number: {result.metadata.get('page_label', 'N/A')}\n"
        f"File Location: {result.metadata.get('source', 'N/A')}"
        for result in search_results
    ])

    # System + Context Prompt
    SYSTEM_PROMPT = f"""
    You are a helpful AI assistant. 
    Answer the user query based ONLY on the following context from the PDF:

    {context}
    """

    return SYSTEM_PROMPT
