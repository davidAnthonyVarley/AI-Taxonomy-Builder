import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="📔",
)

st.header("Projects", divider="grey")
st.caption(
    "Welcome to your projects page. Select from previous taxonomies or create a new taxonomy"
)

st.page_link("pages/Mainpage.py", label="Tax1", icon="🏠")
st.page_link("pages/2_❓_FunctionalityOrPage.py", label="Func/Page1", icon="❓")
st.page_link("pages/3_❓_FunctionalityOrPage.py", label="Func/Page2", icon="❓")
st.page_link("HomePage.py", label="Home")
