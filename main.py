import streamlit as st
from langchain_module import get_few_shot_db_chain

st.title("T Shirts sales and revenue: Database details 👕")

question = st.text_input("Type your query: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)