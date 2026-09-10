import streamlit as st
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from document_loader import load_pdf
from text_splitter import split_document
from embedding import create_embedding
from vector_store import create_vector_store
from retriever import create_retriever
from prompt import create_prompt
from llm import create_llm
# Page configure
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄"
)
# Title
st.title("AI Documnet Assistant")
st.write("Upload a PDF and ask questions about it.")

# PDF uploader
uploaded_file = st.file_uploader("Upload your Pdf",type=["pdf"])

# Process PDF
if uploaded_file is not None:

    with st.spinner("Processing Document......"):

        # Save uploaded PDF temporarily
        pdf_path = "uploaded_document.pdf"

        with open(pdf_path,"wb") as f:
            f.write(uploaded_file.getbuffer())

        

# pdf_path = "data/Muhammad_Saboor_Ali_Professional_Resume.pdf"
        # load pdf
        documents = load_pdf(pdf_path)

        # Split Document
        chunks = split_document(documents)

        # Create Embedding
        embeddings = create_embedding()

        # Create vector store
        vectorstore = create_vector_store(chunks,embeddings)

        # Create Retriever
        retriever = create_retriever(vectorstore)

# question = "give me the Linkedin profile"

        # Create Prompt
        prompt = create_prompt()

        # Create llm
        llm = create_llm()

        # Create RAG chain
        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )

st.success("PDf processed Successfully!")
question = st.text_input("Ask question about your Document:")

# Ask Button
if st.button("Ask question"):

    if question:

        with st.spinner("Generating Answer...."):

            response = chain.invoke(question)

        st.subheader("Answer")
        st.write(response)

    else:
        st.warning("Please enter a question")

        