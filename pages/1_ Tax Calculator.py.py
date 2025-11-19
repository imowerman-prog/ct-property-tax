import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_parquet("data/ct_mill_rates.parquet")

df = load_data()
latest_year = df['grand_list_year'].max()

latest = df[df['grand_list_year'] == latest_year].copy()

st.title(f"CT Property Tax Calculator ({latest_year})")

col1, col2 = st.columns(2)
with col1:
    town = st.selectbox("Select Town", sorted(latest['town'].unique()))
with col2:
    st.write(" ")  # spacer

town_data = latest[latest['town'] == town].iloc[0]

house_value = st.number_input("Assessed Home Value ($)", min_value=0, value=300000, step=10000)
car_value = st.number_input("Assessed Vehicle Value ($)", min_value=0, value=25000, step=1000)

# Mill rates (per $1,000 of assessed value)
mill_real = town_data['mill_rate_real_personal'] or town_data['mill_rate']
mill_car = town_data['mill_rate_motor_vehicle'] or town_data['mill_rate']

tax_house = (house_value / 1000) * mill_real
tax_car = (car_value / 1000) * mill_car
total_tax = tax_house + tax_car

st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Home Tax", f"${tax_house:,.0f}")
c2.metric("Vehicle Tax", f"${tax_car:,.0f}")
c3.metric("Total Estimated Tax", f"${total_tax:,.0f}", delta=f"{latest_year}")

st.info(f"""
**Rates used** ({town}, {latest_year})\n
- Real Estate/Personal Property: {mill_real} mills\n
- Motor Vehicle: {mill_car} mills
""")