import streamlit as st

col1,  col2 = st.columns(2)

with col1:
    st.image( "../resources/images/Photo.png", width=1000)
    st.write("**Arun Prasad**")

with col2:
    #st.write("**Arun Prasad**")
    content = """111
    2322
    3333
    4444"""
    st.write(content)


st.write("Column 33333333333333")
