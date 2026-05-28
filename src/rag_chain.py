import os

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_rag_chain():

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="openai/gpt-oss-20b"
    )

    prompt=PromptTemplate(
    template="""
    You are a helpul assitant.
    Answer ONLY from the provided transcipt context.
    If the context is insufficient just say you dont know.
    {context}
    Question: {question}
     """,
    
    input_variables=["context", "question"]
    )

    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain
# #streamlit run app.py