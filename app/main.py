import streamlit as st

pg = st.navigation([
    st.Page("home_page.py", title="Home", icon=":material/home:", default=True),
    st.Page("readme_page.py", title='Readme Page!', icon=":material/chrome_reader_mode:")
], position='top')
pg.run()