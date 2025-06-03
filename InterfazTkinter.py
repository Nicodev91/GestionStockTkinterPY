import tkinter as tk
from tkinter import messagebox
import AgregarProducto
import EliminarProducto
import BuscarProducto
import MostrarProductos

def agregar_producto():
    try:
        nombre = entry_nombre.get()
        codigo = int(entry_codigo.get())
        cantidad = int(entry_cantidad.get())
        AgregarProducto.agregar_producto(nombre, codigo, cantidad)
        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar_producto():
    try:
        codigo = int(entry_codigo.get())
        EliminarProducto.eliminar_producto(codigo)
        messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def buscar_producto():
    try:
        codigo = int(entry_codigo.get())
        resultado = BuscarProducto.buscar_producto_por_codigo(codigo)
        messagebox.showinfo("Resultado de búsqueda", str(resultado))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_productos():
    try:
        productos = MostrarProductos.mostrar_productos()
        messagebox.showinfo("Productos", str(productos))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Interfaz principal
ventana = tk.Tk()
ventana.title("Sistema de Inventario")
ventana.geometry("400x400")

# Entradas
tk.Label(ventana, text="Nombre del producto:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Código del producto:").pack()
entry_codigo = tk.Entry(ventana)
entry_codigo.pack()

tk.Label(ventana, text="Cantidad del producto:").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

# Botones
tk.Button(ventana, text="Agregar Producto", command=agregar_producto).pack(pady=5)
tk.Button(ventana, text="Eliminar Producto", command=eliminar_producto).pack(pady=5)
tk.Button(ventana, text="Buscar Producto", command=buscar_producto).pack(pady=5)
tk.Button(ventana, text="Mostrar Productos", command=mostrar_productos).pack(pady=5)

ventana.mainloop()
