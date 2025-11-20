# pages/3_ Mill Rate Trends.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def load_data():
    return pd.read_parquet("data/ct_mill_rates.parquet")

df = load_data()

st.title("Mill Rate Trends: Municipality vs Connecticut Average")

col1, col2 = st.columns(2)

with col1:
    # Fixed: properly get the list of municipalities and set Hartford as default if exists
    municipalities = sorted(df['municipality'].dropna().unique())
    default_index = municipalities.index("Hartford") if "Hartford" in municipalities else 0

    municipality = st.selectbox(
        "Select Municipality",
        options=municipalities,
        index=default_index
    )

with col2:
    rate_type = st.selectbox(
        "Select Mill Rate Type",
        options=[
            ("Real Estate & Personal Property", "mill_rate_real_personal"),
            ("Motor Vehicle", "mill_rate_motor_vehicle"),
            ("General / Combined", "mill_rate")
        ],
        format_func=lambda x: x[0]
    )

col_name = rate_type[1]
title_name = rate_type[0]

# 1. Selected municipality data (exclude null rates)
muni_df = df[df['municipality'] == municipality][['grand_list_year', col_name]] \
           .dropna(subset=[col_name]) \
           .sort_values('grand_list_year')

if muni_df.empty:
    st.warning(f"No data available for {municipality} in {title_name}.")
    st.stop()

# 2. Statewide average — ONLY from towns that reported a value that year
state_avg = df.dropna(subset=[col_name]) \
              .groupby('grand_list_year')[col_name] \
              .mean() \
              .reset_index() \
              .rename(columns={col_name: "Connecticut Average"})

# 3. Combine
plot_df = muni_df.rename(columns={col_name: f"{municipality} Rate"}).merge(
    state_avg,
    on='grand_list_year',
    how='outer'
).sort_values('grand_list_year')

# Plot
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=plot_df['grand_list_year'],
    y=plot_df[f"{municipality} Rate"],
    mode='lines+markers',
    name=municipality,
    line=dict(width=5, color="#f4b400"),
    marker=dict(size=10)
))

fig.add_trace(go.Scatter(
    x=plot_df['grand_list_year'],
    y=plot_df["Connecticut Average"],
    mode='lines+markers',
    name="CT State Average",
    line=dict(width=3, color="#94a3b8", dash="dot"),
    marker=dict(size=7)
))

fig.update_layout(
    title=f"{title_name} Mill Rate<br><sub>{municipality} vs Connecticut Average (nulls excluded)</sub>",
    xaxis_title="Grand List Year",
    yaxis_title="Mill Rate (per $1,000)",
    hovermode="x unified",
    template="plotly_dark",
    height=650,
    legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1),
    margin=dict(t=150)
)

st.plotly_chart(fig, use_container_width=True)

# Data table
with st.expander("Show underlying data"):
    display_df = plot_df.copy()
    display_df.columns = ["Year", f"{municipality} Rate", "CT Average"]
    display_df = display_df.round(3)
    st.dataframe(display_df.reset_index(drop=True), use_container_width=True)

st.caption("State average calculated only from municipalities that reported a valid mill rate that year.")