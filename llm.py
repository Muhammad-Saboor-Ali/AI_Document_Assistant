from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
def create_llm():
    llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-20b",task="text-generation")
    model = ChatHuggingFace(llm=llm)
    return model