# 🚗 Vehículos en Venta - Dashboard Interactivo con Streamlit

Este proyecto consiste en una aplicación web interactiva construida con **Streamlit**, cuyo objetivo es explorar visualmente un conjunto de datos de vehículos en venta en Estados Unidos.

## 📊 Funcionalidades

- Carga interactiva del conjunto de datos `vehicles_us.csv`.
- Visualización de:
  - Histograma de precios de vehículos.
  - Conteo de vehículos por condición.
  - Gráfico de dispersión entre precio y kilometraje.
- Filtro dinámico por tipo de vehículo.
- Visualización de tabla filtrada y estadísticas descriptivas.

## 🛠️ Tecnologías utilizadas

- Python
- pandas
- plotly.express
- streamlit
- seaborn
- matplotlib

## 📁 Estructura del proyecto

```
.
├── app.py                 # Script principal de la aplicación Streamlit
├── vehicles_us.csv       # Dataset utilizado
├── notebooks/
│   └── EDA.ipynb         # Análisis exploratorio previo en Jupyter
├── requirements.txt      # Librerías necesarias para ejecutar la app
└── README.md             # Descripción del proyecto
```

## 🌐 Despliegue

Este proyecto ha sido desplegado utilizando [Render](https://render.com/), lo que permite que la aplicación esté disponible directamente en la web.

➡️ **Link de la app**: _[Agrega aquí la URL después del despliegue]_

## 📦 Instalación local (opcional)

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
pip install -r requirements.txt
streamlit run app.py
```
