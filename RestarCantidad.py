
from conexionDB import cursor, conn

def restar_cantidad(codigo, cantidad_a_restar):
    try:
        # Verificar si el producto existe
        cursor.execute("SELECT cantidad FROM productos WHERE codigo = ?", (codigo,))
        resultado = cursor.fetchone()

        if resultado is None:
            return "❌ Producto no encontrado."

        cantidad_actual = resultado[0]

        nueva_cantidad = cantidad_actual - cantidad_a_restar

        if nueva_cantidad < 0:
            return "❌ No se puede restar más cantidad que la existente."

        # Actualizar la cantidad en la base de datos
        cursor.execute("UPDATE productos SET cantidad = ? WHERE codigo = ?", (nueva_cantidad, codigo))
        conn.commit()
        return "✅ Cantidad restada correctamente."

    except Exception as e:
        return f"❌ Error: {str(e)}"