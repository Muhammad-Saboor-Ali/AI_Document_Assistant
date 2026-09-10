from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
def create_embedding():
    embeddings = HuggingFaceEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings