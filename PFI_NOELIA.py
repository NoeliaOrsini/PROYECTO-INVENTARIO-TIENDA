import sqlite3
from colorama import Fore, Style

# Definir la ruta de la base de datos como una variable global
RUTA_DB = r"C:\\Users\\IRON\\Documents\\Noe\\PYTHON\\CLASES_PYTHON\\PFI\\inventario.db"

# CREACIÓN BASE DE DATOS Y TABLA
def inicializar_ddbb():
    # Conexión a la base de datos (se crea automáticamente si no existe)
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    # Crear la tabla 'productos' si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Código TEXT NOT NULL,
            Nombre TEXT NOT NULL,
            Descripción TEXT,
            Cantidad INTEGER,
            Precio REAL,
            Categoria TEXT
        )
    ''')

    # Confirmar los cambios
    conexion.commit()
    conexion.close()

# Ejecutar la función para inicializar la base de datos
inicializar_ddbb()

# MENÚ DE OPCIONES
def mostrar_menu():
    from colorama import Fore, Style

# UTILIZO COLORAMA PARA MEJOR VISUALIZACION Y ESTETICA
print(Fore.GREEN + Style.BRIGHT + "\n" + "-"*75)  # Línea superior

# Título en verde
print(Fore.GREEN + Style.BRIGHT + "\t\t Menú para la Gestión de Productos:")

print(Fore.GREEN + Style.BRIGHT + "\n" + "-"*75)  # Línea inferior al título

print(Fore.CYAN + "1. Registro: Alta de productos nuevos.")
print(Fore.YELLOW + "2. Búsqueda: Consulta de datos de un producto específico.")
print("\033[38;5;214m3. Actualización: Modificar los datos de un producto.")
print(Fore.LIGHTBLACK_EX + "4. Eliminación: Dar de baja productos.")
# Usando color naranja aproximado para las opciones
print(Fore.LIGHTGREEN_EX + "5. Listado: Listado completo de los productos en la base de datos.")
# Opción de reporte de bajo stock en rojo
print(Fore.RED + "6. Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.")
# Opción de "Salir" en magenta
print(Fore.MAGENTA + "7. Salir.")
print(Fore.GREEN + Style.BRIGHT + "-"*75 + Style.RESET_ALL)  # Línea inferior


# FUNCION PARA REGISTRAR PRODUCTO - OPCION 1
def registrar_producto():
    print(Fore.CYAN + "\n --- Registro de Producto Nuevo ---")

    nombre = input(Fore.CYAN + "Nombre del producto:").strip()
    descripcion = input("Descripción del producto:").strip()

    while True:
        try:
            precio = float(input(Fore.CYAN + "Precio del producto:"))
            if precio > 0:
                break
            else:
                print(Fore.CYAN + "Entrada inválida. Debe ingresar un número decimal mayor a 0.")
        except ValueError:
            print(Fore.CYAN +"Entrada inválida. Debe ingresar un valor numérico decimal mayor a 0.")

    while True:
        try:
            cantidad = int(input(Fore.CYAN + f"Cantidad en stock de {nombre}:"))
            if cantidad >= 0:
                break
            else:
                print("Entrada inválida. El stock no puede ser negativo.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un valor numérico entero mayor a 0.")

    categoria = input(Fore.CYAN + "Categoría del producto:").strip()

    # LLAMAMOS A LA BASE DE DATOS
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    try:
        cursor.execute('''
            INSERT INTO productos (Código, Nombre, Descripción, Cantidad, Precio, Categoria)
            VALUES (NULL, ?, ?, ?, ?, ?)''',
            (nombre, descripcion, cantidad, precio, categoria)
        )

        id_producto = cursor.lastrowid
        codigo = f"PROD{id_producto}"

        cursor.execute('''
        UPDATE productos SET Código = ? WHERE id = ?''',
        (codigo, id_producto))

        conexion.commit()

        print(Fore.CYAN + Style.BRIGHT + f"Producto registrado con éxito. Código asignado: {codigo}" + Style.RESET_ALL)

    except sqlite3.IntegrityError:
        print("Error. No se pudo registrar el producto.")

    finally:
        conexion.close()

# FUNCION PARA BUSCAR PRODUCTO - OPCION 2
def buscar_producto():
    print(Fore.LIGHTYELLOW_EX + "\n --- Búsqueda de Producto ---")
    codigo_input = input(Fore.LIGHTYELLOW_EX + "Ingrese el código del producto (por ejemplo, PROD123):").strip().lower()

    # Verificamos si el código tiene el prefijo "prod" y si no lo tiene, lo agregamos.
    if not codigo_input.startswith("prod"):
        codigo_input = "prod" + codigo_input

    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE Código = ?", (codigo_input.upper(),))  # .upper() para manejar mayúsculas y minúsculas

    producto = cursor.fetchone()
    conexion.close()

    if producto: 
        _, codigo, nombre, descripcion, cantidad, precio, categoria = producto 
        print(Fore.LIGHTYELLOW_EX + f"\nProducto encontrado con el código: {codigo}")
        print(Fore.LIGHTYELLOW_EX + f"Nombre      :    {nombre}")
        print(Fore.LIGHTYELLOW_EX + f"Descripción :    {descripcion}")
        print(Fore.LIGHTYELLOW_EX + f"Cantidad    :    {cantidad}")
        print(Fore.LIGHTYELLOW_EX + f"Precio      :   ${precio}")
        print(Fore.LIGHTYELLOW_EX + f"Categoría   :    {categoria}")
    else:
        print(Fore.LIGHTYELLOW_EX + f"No se encontró el producto registrado bajo el código: {codigo_input.upper()}"+ Style.RESET_ALL)

# FUNCION PARA ACTUALIZAR PRODUCTO - OPCION 3
def actualizar_producto():
    print("\033[38;5;214m\n --- Actualización de Producto ---")
    codigo = input("\033[38;5;214mIngrese el código del producto que desea actualizar (por ejemplo, PROD123):").strip().lower()

    # Verificamos si el código tiene el prefijo "prod" y si no lo tiene, lo agregamos.
    if not codigo.startswith("prod"):
        codigo = "prod" + codigo

    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    # Buscar el código sin importar si el usuario lo ingresó en minúsculas o mayúsculas
    cursor.execute("SELECT * FROM productos WHERE Código = ?", (codigo.upper(),))  # El código ya se convierte a mayúsculas para la consulta
    producto = cursor.fetchone()

    if producto:
        _, codigo, nombre, descripcion, cantidad, precio, categoria = producto
        print(f"\nProducto encontrado con el código: {codigo}")
        print(f"Nombre      :    {nombre}")
        print(f"Descripción :    {descripcion}")
        print(f"Cantidad    :    {cantidad}")
        print(f"Precio      :   ${precio}")
        print(f"Categoría   :    {categoria}")

        nombre_nuevo = input("\033[38;5;214m\nNuevo nombre (dejar en blanco para no modificar): \033[0m").strip() or nombre
        descripcion_nueva = input("\033[38;5;214mNueva descripción (dejar en blanco para no modificar): \033[0m").strip() or descripcion

        while True:
            try:
                cantidad_nueva = input("\033[38;5;214mNueva cantidad (dejar en blanco para no modificar): \033[0m").strip()

                if cantidad_nueva == "":
                    cantidad_nueva = cantidad
                    break
                cantidad_nueva = int(cantidad_nueva)
                if cantidad_nueva >= 0:
                    break
                else:
                    print("\033[38;5;196mLa cantidad debe ser mayor o igual a 0.\033[0m")

            except ValueError:
                print("\033[38;5;196mEntrada inválida. Debe ingresar un valor numérico.\033[0m")

        while True:
            try:
                precio_nuevo = input("\033[38;5;214mNuevo precio (dejar en blanco para no modificar): \033[0m").strip()

                if precio_nuevo == "":
                    precio_nuevo = precio
                    break
                precio_nuevo = float(precio_nuevo)
                if precio_nuevo > 0:
                    break
                else:
                    print("\033[38;5;196mEl precio debe ser mayor a 0.\033[0m")

            except ValueError:
                print("\033[38;5;196mEntrada inválida. Debe ingresar un valor numérico.\033[0m")

        categoria_nueva = input("\033[38;5;214mNueva categoría (dejar en blanco para no modificar): \033[0m").strip() or categoria

        try:
            cursor.execute('''
            UPDATE productos SET Nombre = ?, Descripción = ?, Precio = ?, Cantidad = ?, Categoria = ? WHERE Código = ?''',
            (nombre_nuevo, descripcion_nueva, precio_nuevo, cantidad_nueva, categoria_nueva, codigo))
            conexion.commit()
            print("\033[38;5;214mProducto actualizado con éxito.\033[0m")

        except sqlite3.IntegrityError:
            print("\033[38;5;196mError al actualizar el producto.\033[0m")

    else:
        print("\033[38;5;214mNo se encontró el producto con ese código.\033[0m")

    conexion.close()

# FUNCION PARA ELIMINAR PRODUCTO - OPCION 4
def eliminar_producto():
    print(Fore.LIGHTBLACK_EX +"\n --- Eliminación de Producto ---")
    codigo = input(Fore.LIGHTBLACK_EX +"Ingrese el código del producto que desea eliminar:").strip().lower()

    # Verificamos si el código tiene el prefijo "prod" y si no lo tiene, lo agregamos.
    if not codigo.startswith("prod"):
        codigo = "prod" + codigo

    # Conexión a la base de datos
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    # Aseguramos que estamos buscando en la base de datos con el prefijo "prod" en mayúsculas
    cursor.execute("SELECT * FROM productos WHERE Código = ?", (codigo.upper(),))
    producto = cursor.fetchone()

    if producto:
        cursor.execute("DELETE FROM productos WHERE Código = ?", (codigo.upper(),))
        conexion.commit()
        print(Fore.LIGHTBLACK_EX +"Producto eliminado con éxito.")
    else:
        print(Fore.LIGHTBLACK_EX +"No se encontró el producto con ese código."+ Style.RESET_ALL)

    conexion.close()

# FUNCION PARA MOSTRAR LISTADO DE TODOS LOS PRODUCTOS - OPCION 5
def mostrar_productos():
    print(Fore.LIGHTGREEN_EX + "\n --- Todos los Productos ---")
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        print(Fore.LIGHTGREEN_EX + "El inventario esta vacio. No hay productos registrados.")
    else:
        for _, codigo, nombre, descripcion, cantidad, precio, categoria in productos:
            print(Fore.LIGHTGREEN_EX + f"\nCódigo      :    {codigo}")
            print(Fore.LIGHTGREEN_EX + f"Nombre      :    {nombre}")
            print(Fore.LIGHTGREEN_EX + f"Descripción :    {descripcion}")
            print(Fore.LIGHTGREEN_EX + f"Cantidad    :    {cantidad}")
            print(Fore.LIGHTGREEN_EX + f"Precio      :   ${precio}")
            print(Fore.LIGHTGREEN_EX + f"Categoría   :    {categoria}"+ Style.RESET_ALL)

# FUNCION PARA MOSTRAR PRODUCTOS CON BAJO STOCK- OPCION 6
def reporte_bajo_stock():
    print(Fore.RED + Style.BRIGHT + "\n --- Reporte de Bajo Stock ---")
    minimo_stock = 5 

    # Conexión a la base de datos
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    try:
        # Realiza la consulta
        cursor.execute("SELECT * FROM productos WHERE Cantidad <= ?", (minimo_stock,))
        productos_bajo_stock = cursor.fetchall()
        
        if not productos_bajo_stock:
            print(f"No hay productos con stock menor o igual a {minimo_stock}.")
        else:
            for _, codigo, nombre, descripcion, cantidad, precio, categoria in productos_bajo_stock:

                print(Fore.RED + Style.BRIGHT + f"\nCódigo    :    {codigo}" + Style.RESET_ALL)
                print(Fore.RED + Style.BRIGHT + f"Nombre      :    {nombre}" + Style.RESET_ALL)
                print(Fore.RED + Style.BRIGHT + f"Descripción :    {descripcion}" + Style.RESET_ALL)
                print(Fore.RED + Style.BRIGHT + f"Cantidad    :    {cantidad}" + Style.RESET_ALL)
                print(Fore.RED + Style.BRIGHT + f"Precio      :   ${precio}" + Style.RESET_ALL)
                print(Fore.RED + Style.BRIGHT + f"Categoría   :    {categoria}" + Style.RESET_ALL)

    finally:
        # Aseguramos que la conexión y el cursor se cierren siempre
        cursor.close()
        conexion.close()


# FUNCION PRINCIPAL
def main():
    while True:
        mostrar_menu()
        opcion = input("\n Elija una opción (1-7):").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            mostrar_productos()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.MAGENTA + Style.BRIGHT + "\n Gracias por utilizar el sistema. ¡Hasta pronto! \n")
            break
        else:
            print("Opción no válida. Por favor, elija entre 1 y 7.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
