# app.py
import streamlit as st
import base64
import os

st.set_page_config(
    page_title="CT Property Tax Explorer",
    layout="wide",
    initial_sidebar_state="expanded",      
    menu_items=None
)

st.sidebar.page_link("app.py", label="HOME")


logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.jpeg")
if os.path.exists(logo_path):
    with open(logo_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    logo_url = f"data:image/jpeg;base64,{encoded}"
else:
    logo_url = "https://via.placeholder.com/140?text=LOGO"

st.markdown(f"""
<style>
    .black-banner {{
        background-color: #000000;
        padding: 25px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 40px;
    }}
    .banner-title {{
        color: #87CEEB !important;     /* Light sky blue */
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        font-family: Arial, Helvetica, sans-serif;
    }}
</style>

<div class="black-banner">
    <h1 class="banner-title" style="color:#87CEEB; margin:0;">Connecticut Property Tax Explorer</h1>
    <img src="{logo_url}" width="140" height="140">
</div>
""", unsafe_allow_html=True)


st.markdown("""
Real-time mill rates • Property tax calculator • Historical trends  
Data automatically pulled from [data.ct.gov](https://data.ct.gov)

**Select a page from the sidebar on the left**
""")

st.caption("Updated November 2025")