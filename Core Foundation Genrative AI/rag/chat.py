from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

# Initialize OpenAI client
openai_client = OpenAI()

# Vector embedding model
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Connect to existing Qdrant collection
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

# Take the user input
user_query = input("Ask something: ")

# Retrieve similar documents
search_results = vector_db.similarity_search(query=user_query, k=3)

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

# Query OpenAI model
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",   # replace with gpt-5 when available in your account
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)

# Print response
print("🤖", response.choices[0].message.content)
