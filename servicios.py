

def agregar_producto(inventario):

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio, 
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("="*42)
    print("¡El producto se ha agregado correctamente!")
    print("="*42)

def mostrar_inventario(inventario):

    if len(inventario) == 0:
        print("="*56)
        print("El inventario está vacío. No hay productos para mostrar ")
        print("="*56)

    else:
        print("=== Inventario ===")
        print()
        for producto in inventario:
            print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        print()

def calcular_estadisticas(inventario):

    if len(inventario) == 0:
        print("="*33)
        print("No se pueden calcular estadísticas. El inventario está vacío. ")
        print("="*33)

    else:
        valor_total = 0
        cantidad_total = 0

        for producto in inventario:
            valor_total = valor_total + (producto["precio"] * producto["cantidad"])
            cantidad_total = cantidad_total + producto["cantidad"]

        print("=== Estadísticas ===")
        print(f"Valor total del inventario: {valor_total}")
        print(f"Cantidad total de productos: {cantidad_total}. ")

def buscar_productos(inventario,nombre):

    nombre = input("Ingrese el nombre del producto que desea buscar: ")
    for producto in inventario:
        if producto["nombre"] == nombre:
            print("¡Producto encontrado en el inventario! ")
            print(f"Nombre del producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
        else: 
            print(f"No se ha encontrado el producto {nombre} en el inventario. ")