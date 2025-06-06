# Gestor de Stock Tkinter

Esta es una aplicación de escritorio desarrollada con Python y Tkinter para la gestión de inventario. Permite a los usuarios agregar, eliminar, buscar, mostrar y actualizar la cantidad de productos en una base de datos.

## Características

- **Agregar Producto:** Añade nuevos productos al inventario con código, nombre y cantidad.
- **Eliminar Producto:** Elimina productos existentes del inventario.
- **Buscar Producto:** Busca productos por código o nombre.
- **Mostrar Productos:** Muestra todos los productos en el inventario.
- **Agregar Cantidad:** Incrementa la cantidad de un producto existente.
- **Restar Cantidad:** Decrementa la cantidad de un producto existente.
- **Eliminar Todo:** Borra todos los productos del inventario.

## Estructura del Proyecto

- `App.py`: El archivo principal que inicia la aplicación y la interfaz gráfica.
- `InterfazTkinter.py`: Contiene la lógica para la interfaz de usuario de Tkinter.
- `conexionDB.py`: Maneja la conexión a la base de datos SQLite y las operaciones básicas.
- `AgregarProducto.py`: Función para añadir un nuevo producto a la base de datos.
- `EliminarProducto.py`: Función para eliminar un producto de la base de datos.
- `BuscarProducto.py`: Función para buscar productos en la base de datos.
- `MostrarProductos.py`: Función para mostrar todos los productos de la base de datos.
- `AgregarCantidad.py`: Función para aumentar la cantidad de un producto.
- `RestarCantidad.py`: Función para disminuir la cantidad de un producto.
- `EliminarTodo.py`: Función para eliminar todos los productos de la base de datos (Requiere contraseña la cual es: 12345).
- `AgregarVariosProductos.py`: Posiblemente para añadir múltiples productos a la vez (si está implementado).
- `inventario.db`: La base de datos SQLite que almacena la información del inventario.
- `COmando pyinstaller.txt`: Archivo de texto con comandos para compilar la aplicación con PyInstaller.

## Instalación

1.  **Clonar el repositorio (si aplica) o descargar los archivos.**

2.  **Asegúrate de tener Python instalado.** Puedes descargarlo desde [python.org](https://www.python.org/). Se recomienda Python 3.x.

3.  **Instalar las dependencias.** Esta aplicación utiliza `tkinter` (que generalmente viene con Python) y `sqlite3` (también integrado en Python). No se requieren dependencias adicionales a menos que se especifique lo contrario.

    ```bash
    # No se necesitan instalaciones adicionales para tkinter y sqlite3
    # Si se usaran otras librerías, se instalarían así:
    # pip install nombre_de_la_libreria
    ```

## Uso

Para iniciar la aplicación, ejecuta el archivo `App.py`:

```bash
python App.py

Una vez iniciada, la interfaz gráfica te permitirá interactuar con las diferentes funcionalidades de gestión de stock.

## Compilación (Opcional)
Si deseas compilar la aplicación en un ejecutable independiente, puedes usar PyInstaller. Asegúrate de tenerlo instalado:

```
pip install pyinstaller
```
Luego, puedes usar los comandos en COmando pyinstaller.txt para crear el ejecutable. Un ejemplo básico sería:

```
pyinstaller --onefile --windowed App.py
```
Esto creará un ejecutable en la carpeta dist/ .