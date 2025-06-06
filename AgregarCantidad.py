from conexionDB import cursor, conn

def agregar_cantidad_a_producto(codigo, cantidad_a_agregar):
    try:
        # Buscar el producto en la base de datos
        cursor.execute("SELECT cantidad FROM productos WHERE codigo = ?", (codigo,))
        resultado = cursor.fetchone()

        if resultado is None:
            return "❌ Producto no encontrado."

        cantidad_actual = resultado[0]
        nueva_cantidad = cantidad_actual + cantidad_a_agregar

        # Actualizar la cantidad del producto
        cursor.execute("UPDATE productos SET cantidad = ? WHERE codigo = ?", (nueva_cantidad, codigo))
        conn.commit()

        return f"✅ Cantidad actualizada. Nuevo stock: {nueva_cantidad}"
    
    except Exception as e:
        return f"❌ Error al actualizar el producto: {str(e)}"
