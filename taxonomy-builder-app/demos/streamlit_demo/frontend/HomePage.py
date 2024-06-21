import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🖥️",
)


st.title("Dashboard 🖥️")
st.subheader("What would you like to do?", divider="grey")

# Currently resides in sidebar & page.
# Might have to add some sort of project page that lists any created taxonomy,
# then add pages from there, since with multiple taxonomies it can ge messy

st.page_link("pages/Projects.py", label="Projects", icon="📔")
st.page_link("pages/TeamMeet.py", label="Meet the Team", icon="📃")
