import csv

# Guardar inventario en CSV
def guardar_csv(inventario, ruta, incluir_header=True):

    if len(inventario) == 0:
        print("Inventario vacío.")
        return

    try:
        archivo = open(ruta, "w", newline="", encoding="utf-8")
        writer = csv.writer(archivo)

        # Encabezados
        if incluir_header:
            writer.writerow(["nombre", "precio", "cantidad"])

        # Escribir datos
        for p in inventario:
            writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        archivo.close()
        print("Inventario guardado.")

    except:
        print("Error al guardar archivo.")


# Cargar archivo CSV
def cargar_csv(ruta):

    inventario = []
    errores = 0

    try:
        archivo = open(ruta, "r", encoding="utf-8")
        reader = csv.reader(archivo)

        # Leer encabezado
        header = next(reader)

        if header != ["nombre", "precio", "cantidad"]:
            print("Formato incorrecto.")
            return None

        # Leer filas
        for fila in reader:
            try:
                if len(fila) != 3:
                    errores += 1
                    continue

                nombre = fila[0]
                precio = float(fila[1])
                cantidad = int(fila[2])

                if precio < 0 or cantidad < 0:
                    errores += 1
                    continue

                inventario.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })

            except:
                errores += 1

        archivo.close()

        print("Productos cargados:", len(inventario))
        print("Errores:", errores)

        return inventario

    except:
        print("Error al cargar archivo.")
        return None


# Fusionar inventarios
def fusionar_inventarios(actual, nuevos):

    for nuevo in nuevos:
        existe = False

        for p in actual:
            if p["nombre"] == nuevo["nombre"]:
                # suma cantidades y actualiza precio
                p["cantidad"] += nuevo["cantidad"]
                p["precio"] = nuevo["precio"]
                existe = True
                break

        if existe == False:
            actual.append(nuevo)

    print("Inventarios fusionados.")