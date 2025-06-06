#from ssl import _PasswordType
from conexionDB import cursor, conn

def eliminar_todo(password):
    if password == "12345":
        try:
            cursor.execute("DELETE FROM productos")
            conn.commit()
            return "✅ Todos los productos han sido eliminados."
        except Exception as e:
            return f"❌ Error: {str(e)}"
        
    else:
        return "❌ Contraseña incorrecta. No se eliminaron los productos."
   
