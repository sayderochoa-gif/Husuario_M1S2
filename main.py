from servicios import *
inventario = []






opcion = ""

while opcion != "4": 

    print("=== Menú ===")   
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Calcular estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    
    opcion = input("Elija una opción (1-9): ")
    

    if opcion == "1":
        agregar_producto(inventario)
    
    elif opcion == "2":
        mostrar_inventario(inventario)
    
    elif opcion == "3":
        calcular_estadisticas(inventario)
    
    elif opcion == "4":
        print("Ha seleccionado salir. ¡Hasta luego!")
    
    else:
        print("Opción inválida. ")