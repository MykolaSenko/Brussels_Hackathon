import streamlit as st
import time
from script.script_chat import ask_chat

st.set_page_config(layout="wide")

st.title("Domestic violence victims helper")

st.warning('This application is made only with learning purposes. Do not use it in the case of real domestic violence.', icon="⚠️")

st.markdown(
    f"""
    This application is designed to help domestic violence victims to gey access to justice.
    """
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "message_history" not in st.session_state:
    st.session_state.message_history = []

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
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if "message_history" not in st.session_state:
            print("message_history was empty")
            message_history = []
        else:
            message_history = st.session_state.message_history

        print("message_history is:")
        print(message_history)

        answer, message_history = ask_chat(prompt, message_history)
        st.session_state.message_history = message_history
        st.markdown(answer)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})