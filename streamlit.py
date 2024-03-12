import streamlit as st

st.set_page_config(layout="wide")

st.title("Domestic violence victims helper")

st.markdown(
    f"""
    This application is designed to help domestic violence victims to gey access to justice.
    """
)

st.text_input('Are you a victim of domestic violence? Tell me what happened.')