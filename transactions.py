import sqlite3
from datetime import datetime

def agregar_transaccion(tipo, categoria, monto, descripcion=""):
    conn = sqlite3.connect("finanzas.db")
    cursor = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("""
        INSERT INTO transacciones (tipo, categoria, monto, descripcion, fecha)
        VALUES (?, ?, ?, ?, ?)
    """, (tipo, categoria, monto, descripcion, fecha))
    conn.commit()
    conn.close()
    print("✅ Transacción registrada.")

def listar_transacciones():
    conn = sqlite3.connect("finanzas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transacciones ORDER BY fecha DESC")
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def transacciones_por_categoria(categoria):
    conn = sqlite3.connect("finanzas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transacciones WHERE categoria = ?", (LOWER(categoria),))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def obtener_total_por_tipo(tipo):
    conn = sqlite3.connect("finanzas.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(monto) FROM transacciones WHERE tipo = ?
    """, (tipo,))
    resultado = cursor.fetchone()[0]
    conn.close()
    return resultado if resultado else 0.0
