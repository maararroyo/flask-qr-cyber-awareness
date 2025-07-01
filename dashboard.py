# dashboard.py
import pandas as pd
import streamlit as st
import time

st.set_page_config(page_title="Dashboard en Vivo", layout="wide")

st.title("🚨 Dashboard en Tiempo Real: Accesos vía Código QR")

csv_file = 'registro_visitas.csv'

try:
    df = pd.read_csv(csv_file)
    st.success(f"Se han registrado {len(df)} visitas.")
    
    # Mostrar tabla
    st.subheader("📋 Detalles de visitantes")
    st.dataframe(df, use_container_width=True)

    # Estadísticas
    col1, col2 = st.columns(2)
    with col1:
        st.metric("🧑‍💻 Navegadores únicos", df['Navegador'].nunique())
        st.bar_chart(df['Navegador'].value_counts())

    with col2:
        st.metric("💻 Sistemas Operativos", df['Sistema Operativo'].nunique())
        st.bar_chart(df['Sistema Operativo'].value_counts())

except FileNotFoundError:
    st.warning("Aún no hay visitas registradas. Escanea el QR para comenzar.")

st.caption("Actualiza la página para ver nuevos registros.")
