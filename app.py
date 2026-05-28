import streamlit as st
from dotenv import load_dotenv

from src.transcript import get_transcript
from src.chunking import split_text
from src.vectorstore import create_vector_store
from src.rag_chain import create_rag_chain

# LOAD ENV VARIABLES

load_dotenv()


# --------------
# STREAMLIT UI

st.title("Youtube Video Question Answering Chatbot")

youtube_url = st.text_input(
    "Enter YouTube Video URL"
)

question = st.text_input(
    "Ask a question about the video"
)


# ---------------
# BUTTON

if st.button("Generate Answer"):

    try:

        # get vdo ID
        video_id = youtube_url.split("v=")[-1]

        # Transcript
        text = get_transcript(video_id)

        #Text splitting -chunking
        chunks = split_text(text)

        #creating vector store
        vector_store = create_vector_store(chunks)

        #Retriever
        retriever = vector_store.as_retriever()

        #Retrieve Relevant Docs
        docs = retriever.invoke(question)

        #Context ->concatenating relevant documents
        context = "\n\n".join(
            doc.page_content for doc in docs
        )
        #Creating a chain
        chain = create_rag_chain()

        #Answer generation
        answer = chain.invoke({
            "context": context,
            "question": question
        })

        #Display answer
        st.subheader("Answer")
        st.write(answer)

    except Exception as e:

        st.error(f"Error: {str(e)}")

        import traceback
        st.code(traceback.format_exc())