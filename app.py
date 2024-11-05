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

# Botón para visualizar el DataFrame
if st.button("Mostrar DataFrame"):
    st.dataframe(df)

# Botón para graficar los datos
if st.button("Graficar Datos"):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['x'], df['y'], c=df['label'].apply(lambda x: 1 if x == 'A' else 2), cmap='viridis')
    plt.title("Gráfico de Dispersión")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.colorbar(label='Label')
    st.pyplot(plt)
