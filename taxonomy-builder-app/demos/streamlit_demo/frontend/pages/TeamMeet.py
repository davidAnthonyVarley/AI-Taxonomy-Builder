import streamlit as st

st.set_page_config(page_title="Meet the Team", page_icon="📃", layout="wide")

st.title("Meet the Team!")
st.header("Meet the SWENG24 Team Members:", divider="grey")

st.image("Images/Group Photo.jpg", caption="Our lovely team :)")

st.subheader("Ross Devine")
st.caption("Project Manager")
st.image("Images/Ross.jpg", width=200)

st.header("Data Science", divider="grey")

data1, data2 = st.columns(2)
with data1:
    st.subheader("William Doolin")
    st.caption("Data Science Lead")
    st.image("Images/Bill.jpg", width=300)

with data2:
    st.subheader("Scott McNally")
    st.caption("Data Science Developer")
    st.image("Images/Scott.png", width=250)

st.header("Frontend", divider="grey")

frontend1, frontend2, frontend3 = st.columns(3, gap="medium")
with frontend1:
    st.subheader("Martha Ryan")
    st.caption("Documentation")
    st.image("Images/Martha.jpg", width=303)

with frontend2:
    st.subheader("Xiyuan Liu")
    st.caption("Frontend Lead")
    st.image("Images/Xiyuan.jpg", width=300)

with frontend3:
    st.subheader("Madalina Costovici")
    st.caption("Frontend Developer")
    st.image("Images/Madalina.jpg", width=196)

st.header("Backend", divider="grey")

backend1, backend2, backend3 = st.columns(3, gap="medium")
with backend1:
    st.subheader("Cian Moriarty")
    st.caption("Backend Lead")
    st.image("Images/Cian.jpg", width=200)

with backend2:
    st.subheader("David Varley")
    st.caption("Backend Developer")
    st.image("Images/David.jpg", width=250)

with backend3:
    st.subheader("Norbert Papuga")
    st.caption("Backend Developer")
    st.image("Images/Norbert.jpg", width=200)

backend4, backend5 = st.columns(2, gap="small")

with backend4:
    st.subheader("Kajetan Wajszczuk")
    st.caption("Backend Developer")
    st.image("Images/Kyle.jpg", width=200)

with backend5:
    st.subheader("Brian Hurley")
    st.caption("Backend Developer")
    st.image("Images/Brian.jpg", width=170)
