from conexionDB import conn, cursor

def eliminar_producto(codigo):
    cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Producto con código {codigo} eliminado.")
    else:
        print(f"No se encontró producto con código {codigo}.")
