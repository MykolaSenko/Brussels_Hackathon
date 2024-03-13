import streamlit as st


def ask_chat(prompt):

    response = f"Tell me more about: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    answer = st.session_state.messages.append({"role": "assistant", "content": response})    

    return answer