from conexionDB import conn, cursor
# Ejemplo de función para consultar todos los productos
def mostrar_productos():
    # Aquí le decimos a Python que ejecute la consulta SQL para obtener todos los productos
    cursor.execute("SELECT * FROM productos")
    
    # Aquí le decimos a Python que obtenga todos los resultados de la consulta
    productos = cursor.fetchall()
    
    # Aquí le decimos a Python que imprima cada producto obtenido
    for producto in productos:
        print(producto)