import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px



@st.cache_data
def load_data():
    df_inner = pd.read_csv("city_hour.csv")
    df_inner['Datetime'] = pd.to_datetime(df_inner['Datetime'])
    df_inner = df_inner.dropna(subset=['City'])
    return df_inner

df = load_data()
print(df.columns)
cities = df['City'].unique()

st.sidebar.title("Air Quality Explorer")
selected_city = st.sidebar.selectbox("Select a City:", sorted(cities))
date_range = st.sidebar.date_input("Select Date Range",[df['Datetime'].min(), df['Datetime'].max()])

#Filter Data
mask = (
    (df['City'] == selected_city) &
    (df['Datetime'] >= pd.to_datetime(date_range[0])) &
    (df['Datetime'] <=pd.to_datetime(date_range[1]))
)

city_data = df[mask]

#Data printing
st.header("Presenting Data")
st.write("Filtered data shape:", city_data.shape)
st.dataframe(city_data.head())

st.html("<hr>")
st.title(f"Air Quality in {selected_city}")
st.markdown(f"Showing data from **{date_range[0]}** to **{date_range[1]}**")

#Plot: Trend
fig_pm25 = px.line(city_data,x='Datetime',y='PM2.5',title='PM2.5 levels over time')
st.plotly_chart(fig_pm25)
st.subheader("Other Pollutants")
st.html("<hr>")

for pollutant in ['PM10', 'NO', 'NO2', 'NOx', 'NH3', 'CO','SO2', 'O3']:
    fig = px.line(city_data,x='Datetime',y=pollutant,title=f"{pollutant} Levels")
    st.plotly_chart(fig)
    st.html("<hr>")
