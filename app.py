# app.py
import streamlit as st
st.set_page_config(page_title="CT Property Tax Explorer", layout="wide")

st.title("Connecticut Mill Rates & Tax Calculator")
st.markdown("""
Select a page from the sidebar →  
Data is automatically updated from [data.ct.gov](https://data.ct.gov)
""")