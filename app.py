import streamlit as st

st.set_page_config(
    page_title="AI Home Gardening Assistant",
    page_icon="🌸"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #E8F5E9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🌸 AI Home Gardening Assistant 🌿")

st.write("🌺 Welcome to your smart gardening companion!")
st.write("🌱 Ask questions about plants, flowers, soil, watering, and gardening care.")