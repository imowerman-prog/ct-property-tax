import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_parquet("data/ct_mill_rates.parquet")
df = df.sort_values('grand_list_year')

st.title("Mill Rate Trends by Town")

town = st.selectbox("Choose Town", sorted(df['town'].unique()), key="town")

town_df = df[df['town'] == town].copy()

fig = px.line(
    town_df,
    x="grand_list_year",
    y=["mill_rate", "mill_rate_real_personal", "mill_rate_motor_vehicle"],
    title=f"Mill Rates Over Time – {town}",
    labels={"value": "Mill Rate", "variable": "Category"},
    markers=True
)
fig.update_layout(hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)