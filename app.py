import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Dashboard de anuncios de vehículos')

build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Histograma de kilometraje')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Mostrar gráfico de dispersión')

if build_scatter:
    st.write('Relación entre precio y kilometraje')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)