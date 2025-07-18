import streamlit as st
from transactions import agregar_transaccion, listar_transacciones, obtener_total_por_tipo
from db import init_db
init_db()

st.title("Gesto de finanzas personales")

st.subheader("Registrar nueva transacción")

with st.form("trans_form"):
    tipo = st.selectbox("Tipo", ["Egreso", "Ingreso"])
    categoria = st.text_input("Categoría")
    monto = st.number_input("Monto", min_value=0.0, format="%.2f")
    descripcion = st.text_input("Descripción")
    submitted = st.form_submit_button("Guardar")

    if submitted:
        agregar_transaccion(tipo, categoria, monto, descripcion)
        st.success("✅ Transacción registrada")

st.subheader("📋 Historial de transacciones")

transacciones = listar_transacciones()
if transacciones:
    st.table(transacciones)
else:
    st.info("No hay transacciones registradas aún.")

total_ingresos = obtener_total_por_tipo("Ingreso")
total_gastos = obtener_total_por_tipo("Egreso")
balance = total_ingresos - total_gastos

col1, col2, col3 = st.columns(3)
col1.metric("Total Ingresos", f"${total_ingresos:,.2f}")
col2.metric("Total Gastos", f"${total_gastos:,.2f}")
col3.metric("Balance", f"${balance:,.2f}", delta_color="inverse")