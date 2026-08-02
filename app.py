import streamlit as st
st.set_page_config(
    page_title="🌿 AI Garden Buddy",
    page_icon="🌱",
    layout="centered"
)

# Unique Plant Green Theme
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            135deg,
            #E8F5E9,
            #C8E6C9,
            #F1F8E9
        );
    }

    h1 {
        color: #1B5E20;
        text-align: center;
        font-family: "Georgia";
    }

    h2 {
        color: #33691E;
    }

    .stTextInput input {
        background-color: #F1F8E9;
        border: 2px solid #66BB6A;
        border-radius: 15px;
    }

    .stButton button {
        background-color: #43A047;
        color: white;
        border-radius: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

from agent_controller import agent_controller

st.title("🌿🏠 Home Gardening Assistant🧑‍🌾🚜")

st.write(
"""
🌱 Welcome to your intelligent plant companion!

🌻 I can help you with:

🍃 Plant Care  
🌺 Flower Growing Tips  
💧 Watering Guidance  
🪴 Soil & Fertilizer Advice  
🐛 Pest and Disease Solutions  

🌿 Ask me anything about your garden!
"""
)

st.write("Welcome to the AI Home Gardening Assistant!")

question = st.text_input("Ask your gardening question:")

if question:
    st.write("**Your Question:**", question)

    with st.spinner("AI Agent is thinking..."):
        answer = agent_controller(question)

    st.subheader("Answer")
    st.write(answer)