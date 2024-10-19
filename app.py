import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Análisis de Datos")
st.write("¡Bienvenido a tu panel de control!")

# Ejemplo de datos
df = pd.DataFrame({
    "categoría": ["A", "B", "C", "D"],
    "valores": [3, 7, 2, 5]
})

# Gráfico con Plotly Express
fig = px.bar(df, x="categoría", y="valores", title="Ejemplo de gráfico")
st.plotly_chart(fig)

