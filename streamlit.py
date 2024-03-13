import streamlit as st
import random
import time
from script.script import ask_chat

st.set_page_config(layout="wide")

st.title("Domestic violence victims helper")

st.markdown(
    f"""
    This application is designed to help domestic violence victims to gey access to justice.
    """
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Are you a victim of domestic violence? Tell me what happened."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    answer = ask_chat(prompt)