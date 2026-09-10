from langchain_core.prompts import ChatPromptTemplate


def create_prompt():
    prompt = ChatPromptTemplate.from_template("""
    Answer the question based only on the following context.

    Context:
    {context}

    Question:
    {question}

    If the answer is not present in the context,
    say "I don't know based on the provided document."
    """)

    return prompt