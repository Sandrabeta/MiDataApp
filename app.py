import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generar un DataFrame de ejemplo
data = {
    'x': np.random.rand(50),
    'y': np.random.rand(50),
    'label': np.random.choice(['A', 'B'], size=50)
}
df = pd.DataFrame(data)

# Título de la aplicación
st.title("Aplicación de Visualización de Datos")

# Sidebar para los botones
with st.sidebar:
    st.header("Controles")
    if st.button("Mostrar DataFrame"):
        st.session_state.show_dataframe = True
    else:
        st.session_state.show_dataframe = False

    if st.button("Graficar Datos"):
        st.session_state.show_plot = True
    else:
        st.session_state.show_plot = False

# Contenedor principal para la visualización
col1, col2 = st.columns([1, 4])  # Proporción 20% - 80%

with col1:
    # Aquí puedes dejar el espacio para los botones en la sidebar
    st.write("")  # Espacio vacío para mantener el diseño

with col2:
    if st.session_state.get('show_dataframe', False):
        st.subheader("DataFrame")
        st.dataframe(df)

    if st.session_state.get('show_plot', False):
        st.subheader("Gráfico de Dispersión")
        plt.figure(figsize=(10, 6))
        plt.scatter(df['x'], df['y'], c=df['label'].apply(lambda x: 1 if x == 'A' else 2), cmap='viridis')
        plt.title("Gráfico de Dispersión")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.colorbar(label='Label')
        st.pyplot(plt)
