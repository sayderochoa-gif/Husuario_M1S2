📦 Sistema de Inventario en Python


Aplicación de consola desarrollada en Python para la gestión de inventarios.
Permite realizar operaciones CRUD, calcular estadísticas y manejar persistencia de datos mediante archivos CSV.

-----------------------------------------------------------------------------------------------------------------------------

🚀 Demo del sistema

=== MENÚ ===
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir

-----------------------------------------------------------------------------------------------------------------------------

🧩 Funcionalidades principales

✔ Gestión completa de inventario (CRUD)
✔ Cálculo automático de estadísticas
✔ Persistencia de datos con archivos CSV
✔ Validación de entradas del usuario
✔ Manejo de errores para evitar fallos del sistema
✔ Fusión o sobrescritura de inventarios al cargar archivos

-----------------------------------------------------------------------------------------------------------------------------
🧠 Arquitectura del proyecto

El proyecto sigue una estructura modular para facilitar el mantenimiento:

📁 inventario-python/
│
├── main.py        # Control del programa y menú principal
├── servicios.py   # Lógica del negocio (CRUD + estadísticas)
└── archivos.py    # Manejo de archivos CSV

-----------------------------------------------------------------------------------------------------------------------------

📌 Modelo de datos

Cada producto se representa como un diccionario:

{
    "nombre": str,
    "precio": float,
    "cantidad": int
}

-----------------------------------------------------------------------------------------------------------------------------

⚙️ Instalación y ejecución

1. Clonar el repositorio
git clone https://github.com/sayderochoa-gif/Husuario_M1S2.git
2. Ejecutar el programa
python main.py

-----------------------------------------------------------------------------------------------------------------------------

📊 Estadísticas del sistema

El sistema calcula automáticamente:

🔢 Total de unidades en inventario
💰 Valor total del inventario
📈 Producto más costoso
📦 Producto con mayor stock

-----------------------------------------------------------------------------------------------------------------------------

💾 Persistencia de datos (CSV)

📥 Guardar inventario
Genera un archivo con formato:
nombre,precio,cantidad
📤 Cargar inventario

El sistema valida:

✔ Encabezado correcto
✔ Número de columnas
✔ Tipos de datos válidos
✔ Valores no negativos

Si hay errores:

Se omiten las filas inválidas
Se muestra un conteo de errores

-----------------------------------------------------------------------------------------------------------------------------

🔄 Fusión de inventarios

Al cargar datos, el usuario puede:

🔁 Sobrescribir el inventario actual
🔗 Fusionar inventarios:
Si el producto existe → suma cantidades y actualiza precio
Si no existe → se agrega automáticamente

-----------------------------------------------------------------------------------------------------------------------------

🛡️ Manejo de errores

El sistema implementa:

Validación de entradas
Control de excepciones (try/except)
Prevención de caídas del programa
📚 Conceptos aplicados
Estructuras de datos (listas y diccionarios)
Programación modular
Funciones en Python
Manejo de archivos (CSV)
Validación de datos
Control de flujo

-----------------------------------------------------------------------------------------------------------------------------

🧑‍💻 Autor

Sayder Jr Carreño

-----------------------------------------------------------------------------------------------------------------------------

📌 Notas finales

Este proyecto fue desarrollado con fines académicos, aplicando buenas prácticas básicas de programación y organización del código.