import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Cargar datos limpios
df = pd.read_csv('vehicles_clean.csv')

# Título de la app
st.title("Dashboard de vehículos en venta")
st.markdown("Explora las características de los vehículos disponibles mediante gráficos interactivos.")

# Sidebar para seleccionar tipo de visualización
st.sidebar.header("Configuración de gráficos")
grafico = st.sidebar.selectbox("Selecciona el tipo de gráfico", ['Histograma de precio', 'Condición del vehículo', 'Dispersión Precio vs Kilometraje'])

# Mostrar gráfica según selección
if grafico == 'Histograma de precio':
    st.subheader("Distribución de precios")
    fig, ax = plt.subplots()
    sns.histplot(df['price'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

elif grafico == 'Condición del vehículo':
    st.subheader("Cantidad de vehículos por condición")
    fig, ax = plt.subplots()
    sns.countplot(x='condition', data=df, order=df['condition'].value_counts().index, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif grafico == 'Dispersión Precio vs Kilometraje':
    st.subheader("Relación entre precio y kilometraje")
    fig = px.scatter(df, x='odometer', y='price', color='type', hover_data=['model'])
    st.plotly_chart(fig)

# Filtro adicional por tipo de vehículo
tipos = df['type'].unique()
tipo_seleccionado = st.sidebar.multiselect("Filtrar por tipo de vehículo", tipos, default=tipos)

# Mostrar tabla y resumen de datos filtrados
df_filtrado = df[df['type'].isin(tipo_seleccionado)]
st.markdown("### Datos filtrados")
st.dataframe(df_filtrado.head())

# Mostrar resumen
st.markdown("### Estadísticas generales del conjunto filtrado")
st.write(df_filtrado.describe())