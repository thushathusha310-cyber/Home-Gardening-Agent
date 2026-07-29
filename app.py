import streamlit as st
from agent_controller import agent_controller

st.title("🌱 Home Gardening Assistant")

st.write("Welcome to the AI Home Gardening Assistant!")

question = st.text_input("Ask your gardening question:")

if question:
    st.write("**Your Question:**", question)

    with st.spinner("AI Agent is thinking..."):
        answer = agent_controller(question)

    st.subheader("Answer")
    st.write(answer)