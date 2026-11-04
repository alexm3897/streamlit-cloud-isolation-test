import streamlit as st

st.set_page_config(page_title="Streamlit Cloud Isolation Test")
st.title("Streamlit Cloud Isolation Test")
st.write("Testing frontend component loading.")
st.text_input("Test password field", type="password")
st.success("Frontend rendered successfully.")
