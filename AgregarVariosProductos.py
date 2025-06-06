import openpyxl
import AgregarProducto
import sqlite3

def agregar_productos_desde_excel(nombre_archivo):
    try:
        wb = openpyxl.load_workbook(nombre_archivo)
        hoja = wb.active

        for fila in hoja.iter_rows(min_row=2, values_only=True):  # Ignora la cabecera
            nombre, codigo, cantidad = fila
            if nombre and codigo and cantidad:
                AgregarProducto.agregar_producto(nombre, int(codigo), int(cantidad))

        return "✅ Todos los productos fueron agregados correctamente."

    except Exception as e:
        return f"❌ Error al importar desde Excel: {str(e)}"
