# app.py
# app.py  (only the top part – the rest stays exactly the same)

import streamlit as st

# Custom header with guaranteed-working local logo
st.markdown("""
<style>
    .header-container {
        background: linear-gradient(90deg, #0b1d42, #1e40af);
        padding: 25px 40px;
        border-bottom: 7px solid #f4b400;
        border-radius: 0 0 20px 20px;
        box-shadow: 0 6px 25px rgba(0,0,0,0.5);
        margin-bottom: 40px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
    }
    .header-title h1 { 
        margin: 0; 
        font-size: 2.9rem; 
        font-weight: 800; 
        text-shadow: 3px 3px 8px rgba(0,0,0,0.7);
    }
    .header-title p { 
        margin: 10px 0 0 0; 
        font-size: 1.35rem; 
        opacity: 0.95;
    }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])

with col1:
    st.markdown("""
        <div class="header-container">
            <div class="header-title">
                <h1>Connecticut Property Tax Explorer</h1>
                <p>Real-time mill rates • Tax calculator • Historical trends</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # This line is the magic — it forces Streamlit to serve the local file correctly
    st.markdown(
        f'<img src="assets/logo.webp" width="180" style="border-radius:50%; border:7px solid #f4b400; box-shadow:0 0 30px white, 0 10px 35px rgba(0,0,0,0.7); background:white; padding:12px;">',
        unsafe_allow_html=True
    )
st.set_page_config(page_title="CT Property Tax Explorer", layout="wide")


st.markdown("""
Select a page from the sidebar →  
Data is automatically updated from [data.ct.gov](https://data.ct.gov)
""")