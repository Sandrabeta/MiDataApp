import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Mi Aplicación de Streamlit")

# Crear un DataFrame de ejemplo
data = {
    'Columna 1': [1, 2, 3, 4, 5],
    'Columna 2': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)

# Botón para visualizar el DataFrame
if st.button('Mostrar DataFrame'):
    st.write(df)
