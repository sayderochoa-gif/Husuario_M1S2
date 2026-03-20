print("="*33)
print("Bienvenido al inventario de M1S2")
print("="*33)
print("")

inventario  = []

def agregar_producto():

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

def mostrar_inventario():

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

def calcular_estadisticas():

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

opcion = ""

while opcion != "4": 

    print("=== Menú ===")   
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        agregar_producto()
    
    elif opcion == "2":
        mostrar_inventario()
    
    elif opcion == "3":
        calcular_estadisticas()
    
    elif opcion == "4":
        print("Ha seleccionado salir. ¡Hasta luego!")
    
    else:
        print("Opción inválida. ")