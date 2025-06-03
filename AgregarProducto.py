from conexionDB import conn, cursor

# Crear una tabla para almacenar los productos

cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    codigo TEXT UNIQUE NOT NULL,
    cantidad INTEGER NOT NULL
)
''')
conn.commit() #Aqui le decimos a python que guarde los cambios hechos a la base de datos

inventario = []

def agregar_producto(nombre, codigo, cantidad):
    try:
        cursor.execute("INSERT INTO productos (nombre, codigo, cantidad) VALUES (?, ?, ?)", 
        (nombre, codigo, cantidad))
        conn.commit()
        print("Producto agregado a la base de datos.")
    except sqlite3.IntegrityError:
        print("El código del producto ya existe en la base de datos.")
    
    
