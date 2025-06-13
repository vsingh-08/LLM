import streamlit as st
from backend import ask_groq

st.set_page_config(page_title="Descriptive QA System", layout="centered")
st.title("Descriptive Question Answering System (Groq - LLaMA3)")

question = st.text_area("Enter your question:")

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Generating answer..."):
            answer = ask_groq(question)
            st.success("Answer:")
            st.markdown(f"**{answer}**")
