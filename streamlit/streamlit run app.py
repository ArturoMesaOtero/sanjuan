import streamlit as st
import pandas as pd
import io

def procesar_archivo(archivo):
    # Aquí iría la lógica para procesar el archivo Excel
    df = pd.read_excel(archivo)
    return f"Archivo procesado. Tiene {len(df)} filas y {len(df.columns)} columnas."

def procesar_pregunta(pregunta):
    # Aquí iría la lógica para procesar la pregunta
    return f"Respuesta a: {pregunta}"

st.title("Mi Aplicación Web")

# Sección para cargar archivos
st.header("Cargar archivo Excel")
archivo = st.file_uploader("Selecciona un archivo Excel", type=["xlsx", "xls"])
if archivo is not None:
    resultado_archivo = procesar_archivo(archivo)
    st.write(resultado_archivo)

# Sección de chat
st.header("Chat")
pregunta = st.text_input("Haz una pregunta:")
if pregunta:
    respuesta = procesar_pregunta(pregunta)
    st.write(respuesta)