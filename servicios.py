# Función para agregar productos
def agregar_producto(inventario):
    try:
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))

        # Validamos que no sean negativos
        if precio < 0 or cantidad < 0:
            print("Datos inválidos.")
            return

        # Creamos el producto como diccionario
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        # Lo agregamos a la lista
        inventario.append(producto)
        print("Producto agregado.")

    except:
        print("Error al ingresar datos.")


# Función para mostrar inventario
def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("Inventario vacío.")
    else:
        for p in inventario:
            print(p["nombre"], "|", p["precio"], "|", p["cantidad"])


# Función para buscar un producto
def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"] == nombre:
            return p  # retorna el producto
    return None  # si no lo encuentra


# Función para actualizar un producto
def actualizar_producto(inventario):
    nombre = input("Producto a actualizar: ")
    producto = buscar_producto(inventario, nombre)

    if producto == None:
        print("Producto no encontrado.")
        return

    try:
        # Permite actualizar solo lo que el usuario quiera
        nuevo_precio = input("Nuevo precio (Enter para omitir): ")
        nueva_cantidad = input("Nueva cantidad (Enter para omitir): ")

        if nuevo_precio != "":
            producto["precio"] = float(nuevo_precio)

        if nueva_cantidad != "":
            producto["cantidad"] = int(nueva_cantidad)

        print("Producto actualizado.")

    except:
        print("Error en los datos.")


# Función para eliminar producto
def eliminar_producto(inventario):
    nombre = input("Producto a eliminar: ")

    for i in range(len(inventario)):
        if inventario[i]["nombre"] == nombre:
            del inventario[i]  # elimina el producto
            print("Producto eliminado.")
            return

    print("Producto no encontrado.")


# Función de estadísticas
def calcular_estadisticas(inventario):
    if len(inventario) == 0:
        print("Inventario vacío.")
        return

    unidades = 0
    valor_total = 0

    # Calculamos totales
    for p in inventario:
        unidades += p["cantidad"]
        valor_total += p["precio"] * p["cantidad"]

    # Inicializamos con el primero
    producto_caro = inventario[0]
    producto_stock = inventario[0]

    # Buscamos el más caro y el de mayor stock
    for p in inventario:
        if p["precio"] > producto_caro["precio"]:
            producto_caro = p

        if p["cantidad"] > producto_stock["cantidad"]:
            producto_stock = p

    # Mostramos resultados
    print("\n=== ESTADÍSTICAS ===")
    print("Unidades totales:", unidades)
    print("Valor total:", valor_total)
    print("Producto más caro:", producto_caro["nombre"], producto_caro["precio"])
    print("Mayor stock:", producto_stock["nombre"], producto_stock["cantidad"])