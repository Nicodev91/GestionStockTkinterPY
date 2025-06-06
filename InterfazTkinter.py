import tkinter as tk
import AgregarProducto
import EliminarProducto
import BuscarProducto
import MostrarProductos
import AgregarVariosProductos
from tkinter import filedialog
import EliminarTodo
from tkinter import simpledialog
from AgregarCantidad import agregar_cantidad_a_producto
from RestarCantidad import restar_cantidad

def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Sistema de Inventario")
    ventana.geometry("800x600")

def actualizar_salida(texto):
    salida_text.config(state='normal')
    salida_text.delete("1.0", tk.END)
    salida_text.insert(tk.END, texto)
    salida_text.config(state='disabled')

def agregar_producto():
    try:
        nombre = entry_nombre.get()
        codigo = int(entry_codigo.get())
        cantidad = int(entry_cantidad.get())
        AgregarProducto.agregar_producto(nombre, codigo, cantidad)
        actualizar_salida("✅ Producto agregado correctamente.")
    except Exception as e:
        actualizar_salida(f"❌ Error: {str(e)}")

def agregar_stock():
    try:
        codigo = int(entry_codigo.get())
        cantidad = int(entry_cantidad.get())
        mensaje = agregar_cantidad_a_producto(codigo, cantidad)
        actualizar_salida(mensaje)
    except Exception as e:
        actualizar_salida(f"❌ Error: {str(e)}")

def restar_stock():
    try:
        codigo = int(entry_codigo.get())
        cantidad = int(entry_cantidad.get())
        mensaje = restar_cantidad(codigo, cantidad)
        actualizar_salida(mensaje)
    except Exception as e:
        actualizar_salida(f"❌ Error: {str(e)}")


def eliminar_producto():
    try:
        codigo = int(entry_codigo.get())
        EliminarProducto.eliminar_producto(codigo)
        actualizar_salida("✅ Producto eliminado correctamente.")
    except Exception as e:
        actualizar_salida(f"❌ Error: {str(e)}")

def buscar_producto():
    try:
        codigo = int(entry_codigo.get())
        resultado = BuscarProducto.buscar_producto_por_codigo(codigo)
        
        if resultado:
            id_producto, nombre, codigo, cantidad = resultado
            mensaje = (
                "🔎 Producto encontrado:\n\n"
               # f"🆔 ID: {id_producto}\n"
                f"📦 Nombre: {nombre.strip()}\n"
                f"🏷️ Código: {codigo}\n"
                f"📦 Cantidad: {cantidad}"
            )
        else:
            mensaje = "❌ Producto no encontrado."
        
        actualizar_salida(mensaje)

    except Exception as e:
        actualizar_salida(f"❌ Error: {str(e)}")

def mostrar_productos():
    try:
        productos = MostrarProductos.mostrar_productos()
        actualizar_salida("📦 Lista de productos:\n" + str(productos))
    except Exception as e:
        actualizar_salida(f"❌ Error: {str(e)}")

def importar_excel():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos Excel", "*.xlsx")])
    if archivo:
        resultado = AgregarVariosProductos.agregar_productos_desde_excel(archivo)
        actualizar_salida(resultado)

def eliminar_todos_los_productos():
    contraseña = simpledialog.askstring("Confirmación", "Ingrese la contraseña para eliminar todo:", show='*')

    if contraseña:
        resultado = EliminarTodo.eliminar_todo(contraseña)
        actualizar_salida(resultado)
    else:
        messagebox.showerror("Contraseña incorrecta", "Operación cancelada.")



# Interfaz principal
ventana = tk.Tk()
ventana.title("Sistema de Inventario")
ventana.geometry("800x600")  # ventana más grande

# Frame de entradas
frame_entradas = tk.Frame(ventana, padx=10, pady=10)
frame_entradas.pack(fill=tk.X)

tk.Label(frame_entradas, text="Nombre del producto:").grid(row=0, column=0, sticky='w')
entry_nombre = tk.Entry(frame_entradas, width=40)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_entradas, text="Código del producto:").grid(row=1, column=0, sticky='w')
entry_codigo = tk.Entry(frame_entradas, width=40)
entry_codigo.grid(row=1, column=1)

tk.Label(frame_entradas, text="Cantidad del producto:").grid(row=2, column=0, sticky='w')
entry_cantidad = tk.Entry(frame_entradas, width=40)
entry_cantidad.grid(row=2, column=1)

def validar_longitud(new_value):
    return len(new_value) <= 15

# Registra la función de validación en Tkinter
validacion = ventana.register(validar_longitud)

# Aplica la validación a los Entry
entry_nombre.config(validate="key", validatecommand=(validacion, '%P'))
entry_codigo.config(validate="key", validatecommand=(validacion, '%P'))
entry_cantidad.config(validate="key", validatecommand=(validacion, '%P'))


# Frame de botones
frame_botones = tk.Frame(ventana, pady=10)
frame_botones.pack()

tk.Button(frame_botones, text="Importar desde Excel", command=importar_excel, width=20).grid(row=1, column=0, padx=5, pady=10)
tk.Button(frame_botones, text="Agregar Producto", command=agregar_producto, width=20).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Agregar Stock", command=agregar_stock, width=20).grid(row=1, column=1, padx=5, pady=10)
tk.Button(frame_botones, text="Agregar Stock", command=agregar_stock, width=20).grid(row=1, column=1, padx=5, pady=10)
tk.Button(frame_botones, text="Eliminar Producto", command=eliminar_producto, width=20).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Restar Stock", command=restar_stock, width=20).grid(row=1, column=2, padx=5, pady=10)
tk.Button(frame_botones, text="Buscar Producto", command=buscar_producto, width=20).grid(row=0, column=2, padx=5)
tk.Button(frame_botones, text="Mostrar Productos", command=mostrar_productos, width=20).grid(row=0, column=3, padx=5)
tk.Button(frame_botones, text="Eliminar Todos", command=eliminar_todos_los_productos, width=20).grid(row=0, column=4, padx=5)


# Frame de salida
frame_salida = tk.LabelFrame(ventana, text="Resultados", padx=10, pady=10)
frame_salida.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

salida_text = tk.Text(frame_salida, height=20, wrap=tk.WORD, state='disabled', bg="#f0f0f0", font=("Arial", 11))
salida_text.pack(fill=tk.BOTH, expand=True)

ventana.mainloop()


