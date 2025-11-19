import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_parquet("data/ct_mill_rates.parquet")

st.title("Mill Rate Trends by Property Type (Statewide Average)")

category = st.selectbox(
    "Choose Category",
    options=[
        ("Real Estate & Personal Property", "mill_rate_real_personal"),
        ("Motor Vehicle", "mill_rate_motor_vehicle"),
        ("General Mill Rate", "mill_rate")
    ]
)

col_name = category[1]
title = category[0]

yearly_avg = df.groupby('grand_list_year')[col_name].mean().reset_index()

fig = px.line(
    yearly_avg,
    x='grand_list_year',
    y=col_name,
    title=f"Connecticut Average {title} Over Time",
    markers=True
)
fig.update_yaxes(title="Average Mill Rate")
st.plotly_chart(fig, use_container_width=True)

st.write(yearly_avg.round(2))