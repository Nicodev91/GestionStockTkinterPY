import AgregarProducto 
import EliminarProducto
import conexionDB
import BuscarProducto
import MostrarProductos

while True:
    print("Bienvenido al inventario")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Buscar producto por código")
    print("4. Mostrar productos")
    print("9. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        codigo = int(input("Ingrese el código del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        AgregarProducto.agregar_producto(nombre, codigo, cantidad)

    elif opcion == "2":
        codigo = int(input("Ingrese el código del producto a eliminar: "))
        EliminarProducto.eliminar_producto(codigo)

    elif opcion == "3":
        codigo = int(input("Ingrese el código del producto a buscar: "))
        BuscarProducto.buscar_producto_por_codigo(codigo)
    
    elif opcion == "4":

        MostrarProductos.mostrar_productos()

    elif opcion == "9":
        print("Gracias por usar el inventario")
        break
        
    else:
        print("Opción inválida. Intente nuevamente.")
