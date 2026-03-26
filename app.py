# Importamos todas las funciones de los otros archivos
from servicios import *
from archivos import *

# Lista donde se guardan los productos
inventario = []

# Variable para controlar el menú
opcion = ""

print("=== BIENVENIDO AL SISTEMA DE INVENTARIO ===")

# Bucle del menú (sin usar while True)
while opcion != "9":

    # Mostrar menú
    print("\n=== MENÚ ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    # Pedimos la opción al usuario
    opcion = input("Elija una opción (1-9): ")

    try:
        # Opción 1: agregar producto
        if opcion == "1":
            agregar_producto(inventario)

        # Opción 2: mostrar inventario
        elif opcion == "2":
            mostrar_inventario(inventario)

        # Opción 3: buscar producto
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            producto = buscar_producto(inventario, nombre)

            # Validamos si existe
            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")

        # Opción 4: actualizar producto
        elif opcion == "4":
            actualizar_producto(inventario)

        # Opción 5: eliminar producto
        elif opcion == "5":
            eliminar_producto(inventario)

        # Opción 6: estadísticas
        elif opcion == "6":
            calcular_estadisticas(inventario)

        # Opción 7: guardar archivo CSV
        elif opcion == "7":
            ruta = input("Ruta del archivo: ")
            guardar_csv(inventario, ruta)

        # Opción 8: cargar archivo CSV
        elif opcion == "8":
            ruta = input("Ruta del archivo: ")
            nuevos = cargar_csv(ruta)

            # Si se cargaron datos correctamente
            if nuevos != None:
                decision = input("¿Sobrescribir inventario? (S/N): ").upper()

                if decision == "S":
                    inventario = nuevos  # reemplaza todo
                else:
                    fusionar_inventarios(inventario, nuevos)  # combina datos

        # Opción 9: salir
        elif opcion == "9":
            print("Usted ha seleccionado salir. ¡Hasta luego!")

        # Opción inválida
        else:
            print("Opción inválida.")

    # Manejo de errores general
    except:
        print("Ocurrió un error, intenta de nuevo.")