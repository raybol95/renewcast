import streamlit as st
from country_mappings import COUNTRY_MAPPINGS
from entsoe_client import get_energy_data
from forecast import generate_forecast

st.title("Forecasting Renewable Energy Production in EU")
country = st.sidebar.selectbox("Select a Country",
    list(COUNTRY_MAPPINGS.keys()))
st.header(country)

country_code = COUNTRY_MAPPINGS[country]

df = get_energy_data(country_code)

st.area_chart(df[['Solar', 'Wind Onshore']])

forecast_horizon = st.sidebar.slider(label='Forecast Horizon (hours)',
                             min_value = 12, max_value = 168,
                             value = 48)

window_length = st.sidebar.slider(label = 'Window Length', min_value = 1,
                          value = 5)

df_wind = generate_forecast(df[['Wind Onshore']], forecast_horizon, window_length)
df_solar = generate_forecast(df[['Solar']], forecast_horizon, window_length)

st.line_chart(df_wind)
st.line_chart(df_solar)