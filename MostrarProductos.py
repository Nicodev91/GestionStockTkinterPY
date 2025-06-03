from conexionDB import conn, cursor

def mostrar_productos():
    cursor.execute("SELECT nombre, codigo, cantidad FROM productos")

    productos = cursor.fetchall()

    if not productos:
        return "No hay productos registrados."

    resultado = ""
    for producto in productos:
        resultado += f"Nombre: {producto[0]}, Codigo: {producto[1]}, Cantidad: {producto[2]}\n"

    
    return resultado
