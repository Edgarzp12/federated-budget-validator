import streamlit as st
import pandas as pd
from io import BytesIO
from limpiar import limpiar_presupuesto

st.title("Validador de Presupuesto Federativo")

uploaded_file = st.file_uploader("Suba su archivo Excel", type=["xlsx"])

if uploaded_file:
    if st.button("Procesar archivo"):

        df_limpio, total = limpiar_presupuesto(uploaded_file)

        st.success("Archivo procesado correctamente")
        st.write(f"Total detectado: ₡{total:,.2f}")

        # Crear archivo en memoria
        output = BytesIO()
        df_limpio.to_excel(output, index=False, engine="openpyxl")
        output.seek(0)

        st.download_button(
            label="Descargar archivo limpio",
            data=output,
            file_name="PlanPresupuesto_Limpio.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )