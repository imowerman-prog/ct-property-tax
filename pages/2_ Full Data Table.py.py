import streamlit as st
import pandas as pd

df = pd.read_parquet("data/ct_mill_rates.parquet")

st.title("Full CT Mill Rates Dataset")
st.write(f"{len(df):,} records | Years {df['grand_list_year'].min()}–{df['grand_list_year'].max()}")

st.dataframe(df, use_container_width=True)