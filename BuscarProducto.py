from conexionDB import conn, cursor

# Ejemplo de función para consultar un producto por código
def buscar_producto_por_codigo(codigo):
    # Aquí le decimos a Python que ejecute la consulta con filtro por código (parámetro para evitar inyección SQL)
    cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
    
    # Aquí le decimos a Python que obtenga un solo resultado (o None si no existe)
    producto = cursor.fetchone()
    
    if producto:
        print("Producto encontrado:", producto)
    else:
        print("No se encontró producto con ese código.")

    return producto