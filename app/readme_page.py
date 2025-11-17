import streamlit as st

with open("README.md", "r") as f:
    readme_content = f.read()

st.markdown(readme_content, unsafe_allow_html=True)
