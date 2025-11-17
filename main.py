import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation(
    [
        st.Page("app/home_page.py", title="Home", icon=":material/home:", default=True),
        st.Page(
            "app/readme_page.py",
            title="Readme Page!",
            icon=":material/chrome_reader_mode:",
        ),
    ],
    position="top",
)
pg.run()
