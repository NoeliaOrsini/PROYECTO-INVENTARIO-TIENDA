# Proyecto Final Integrador: Gestor de Inventario para Tienda

Este proyecto consiste en un programa desarrollado en Python que permite gestionar el inventario de una pequeña tienda. 
Incluye un menú de opciones para realizar tareas como registrar nuevos productos, buscar productos específicos, actualizar información de productos, eliminar productos, y generar reportes sobre el inventario. 
Además, utiliza bases de datos SQLite para almacenar los datos de forma persistente y la librería `colorama` para mejorar la visualización en consola.

## Características Principales
- **Base de datos SQLite**: Persistencia de datos en un archivo local.
- **Interfaz de usuario en consola**: Menú intuitivo y organizado.
- **Estilo visual**: Uso de colores gracias a la librería `colorama`.
- **Gestor de inventario completo**: Alta, búsqueda, modificación, eliminación y listado de productos.
- **Reporte de bajo stock**: Identificación de productos con cantidades menores al mínimo especificado.

## Requisitos Previos
- Python 3.7 o superior.
- Librería `colorama` (puedes instalarla con `pip install colorama`).
- SQLite (incluido con la mayoría de las distribuciones de Python).

## Configuración
La ruta de la base de datos se define como una variable global para facilitar su uso en todas las funciones del programa:
```python
RUTA_DB = r"C:\\Users\\IRON\\Documents\\Noe\\PYTHON\\CLASES_PYTHON\\PFI\\inventario.db"
```
Esto evita la necesidad de declarar la ruta en cada función, mejorando la claridad del código.

## Menú de Opciones
El programa incluye un menú con las siguientes opciones:
1. **Registro**: Alta de productos nuevos.
2. **Búsqueda**: Consulta de datos de un producto específico.
3. **Actualización**: Modificar los datos de un producto.
4. **Eliminación**: Dar de baja productos.
5. **Listado**: Mostrar un listado completo de los productos registrados.
6. **Reporte de Bajo Stock**: Listar productos cuya cantidad es inferior al mínimo establecido.
7. **Salir**: Finalizar el programa.

## Estructura del Código
### 1. Inicialización de la Base de Datos
La base de datos y la tabla `productos` se crean automáticamente si no existen. Esto garantiza que el programa sea ejecutable desde cero:
```python
def inicializar_ddbb():
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()
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
    conexion.commit()
    conexion.close()
```

### 2. Registro de Productos
Permite agregar nuevos productos al inventario, generando un código único para cada producto registrado:
```python
def registrar_producto():
    # Solicitar datos al usuario y validarlos
    # Guardar el producto en la base de datos
```

### 3. Búsqueda de Productos
Busca productos por código y muestra todos sus detalles si se encuentra:
```python
def buscar_producto():
    # Solicitar el código al usuario
    # Realizar la consulta en la base de datos
```

### 4. Actualización de Productos
Permite modificar cualquier campo de un producto existente:
```python
def actualizar_producto():
    # Solicitar el código del producto
    # Actualizar los campos seleccionados
```

### 5. Eliminación de Productos
Elimina productos del inventario:
```python
def eliminar_producto():
    # Solicitar el código del producto
    # Confirmar y eliminar
```

### 6. Listado de Productos
Muestra un listado completo de todos los productos registrados:
```python
def mostrar_productos():
    # Consultar y mostrar todos los productos
```

### 7. Reporte de Bajo Stock
Genera un reporte de productos cuya cantidad está por debajo del mínimo permitido:
```python
def reporte_bajo_stock():
    # Filtrar productos con bajo stock
```

## Uso de Librería `colorama`
`colorama` se utiliza para mejorar la estética del menú y los mensajes:
```python
from colorama import Fore, Style

print(Fore.GREEN + Style.BRIGHT + "\tMenú para la Gestión de Productos")
print(Fore.CYAN + "1. Registro")
```
Esto permite distinguir visualmente las opciones y mensajes importantes.

## Bucles y Condicionales
- El programa utiliza bucles para permitir la ejecución continua hasta que el usuario elija salir.
- Los condicionales se emplean para validar entradas del usuario y manejar errores (por ejemplo, entradas inválidas al registrar productos).

## Manejo de Errores
- El sistema está diseñado para manejar diferentes tipos de errores en las operaciones de registro, búsqueda, actualización y eliminación. 
Aquí se describen algunos de los errores más comunes:

## Búsqueda de Producto
Si el usuario ingresa un código incorrecto (ya sea un código inexistente o mal formateado), se le informará con el siguiente mensaje:

"No se encontró el producto registrado bajo el código: PRODxxx"

## Actualización de Producto
Al intentar actualizar un producto, se validan los siguientes aspectos:

Si el código del producto no existe, se muestra el siguiente error:
"No se encontró el producto con ese código."
Si los valores ingresados para cantidad o precio no son válidos, el sistema sigue pidiendo la entrada hasta que se proporcione un valor válido:
"La cantidad no puede ser negativa."
"El precio debe ser mayor que 0."

## Eliminación de Producto
En el caso de intentar eliminar un producto que no existe, el sistema mostrará:
"No se encontró el producto con ese código."
Ejemplo de Entrada y Salida
1. Registrar Producto
Entrada:
Nombre del producto: Teclado
Descripción del producto: Teclado mecánico RGB
Precio del producto: 80.5
Cantidad en stock de Teclado: 50
Categoría del producto: Tecnología
Salida:
Producto registrado con éxito. Código asignado: PROD123

2. Buscar Producto
Entrada:
Ingrese el código del producto (por ejemplo, PROD123): prod123
Salida:
Producto encontrado con el código: PROD123
Nombre      :    Teclado
Descripción :    Teclado mecánico RGB
Cantidad    :    50
Precio      :   $80.5
Categoría   :    Tecnología

3. Actualizar Producto
Entrada:

Ingrese el código del producto que desea actualizar (por ejemplo, PROD123): prod123
Nuevo nombre (dejar en blanco para no modificar): Teclado actualizado
Salida:
Producto actualizado con éxito.

4. Eliminar Producto
Entrada:
Ingrese el código del producto que desea eliminar: prod123
Salida:
Producto eliminado con éxito.

En las opciones 2,3 y 4 en las que son necesario identificar un producto por su codigo PRODXXX; Si el usuario ingresa un código sin el prefijo, el programa puede agregar el prefijo prod automáticamente antes de realizar la búsqueda, actualización o eliminación. 
if not codigo.startswith('prod'):
            codigo = 'prod' + codigo  # Agregar el prefijo 'prod' si no está presente
Lo mismo si coloca el prod en minúscula, el sistema lo corrige para ser reconocido el código.
Para ello se utiliza el método .lower() en Python convierte todas las letras de una cadena de texto a minúsculas.

## Ejecución
1. Descarga el código y asegúrate de que la ruta de la base de datos `RUTA_DB` sea correcta.
2. Ejecuta el archivo Python desde la consola:
```bash
python gestor_inventario.py
```
3. Sigue las instrucciones del menú para interactuar con el programa.

## Conclusión
Este proyecto integra conocimientos de Python como manejo de bases de datos, estructuras de control, funciones, y bibliotecas externas, demostrando habilidades para desarrollar aplicaciones útiles y eficientes.

Te invito a ver su funcionamiento en el siguiente link:https://www.youtube.com/watch?v=NcFhVqYrZCE

Realizado por Noelia Orsini para Talento Tech.
