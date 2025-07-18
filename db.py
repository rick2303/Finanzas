import sqlite3

# Primero definimos la función de conexión
def get_connection():
    conn = sqlite3.connect("finanzas.db")
    return conn

# Luego definimos la función que inicializa la base de datos
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            monto REAL NOT NULL,
            descripcion TEXT,
            fecha TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()
