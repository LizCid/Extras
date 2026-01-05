# -----------------------------------------------------------------------------
# SISTEMA DE CAJA REGISTRADORA
# Este programa permite registrar productos, calcular subtotales, aplicar
# descuentos basados en condiciones y procesar diferentes formas de pago.
# -----------------------------------------------------------------------------

# Inicializamos una lista vacía llamada 'productos' para almacenar los diccionarios
# que contendrán la información (nombre, precio, cantidad) de cada artículo.
productos = []

print("\n--- SISTEMA DE CAJA REGISTRADORA ---")

# -----------------------------------------------------------------------------
# SECCIÓN: REGISTRO DE PRODUCTOS
# Usamos un bucle 'while True' para permitir al usuario ingresar tantos productos
# como desee hasta que escriba la palabra 'fin'.
# -----------------------------------------------------------------------------
while True:
    # .strip() elimina espacios en blanco accidentales al inicio o final del texto
    nombre = input("\nIngrese el nombre del producto (o 'fin' para terminar): ").strip()

    # Validación: El nombre no puede ser un texto vacío
    if nombre == "":
        print("El nombre no puede estar vacío.")
        continue

    # Condición de salida: Si el usuario escribe 'fin', se rompe el bucle principal
    if nombre.lower() == "fin":
        break

    # Bucle de validación para el PRECIO:
    # Asegura que el usuario ingrese un número y que este sea mayor a cero.
    while True:
        precio = input("Ingrese el precio del producto: ")
        if precio.isdigit():  # Verifica si la entrada contiene solo números
            precio = float(precio)
            if precio > 0:
                break
        print("Precio inválido. Ingrese un número válido.")

    # Bucle de validación para la CANTIDAD:
    # Asegura que la cantidad sea un número entero positivo.
    while True:
        cantidad = input("Ingrese la cantidad: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if cantidad > 0:
                break
        print("Cantidad inválida. Ingrese un número válido.")

    # Creamos un diccionario para agrupar los datos del producto actual
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    # Guardamos el diccionario del producto en nuestra lista general de 'productos'
    productos.append(producto)

# -----------------------------------------------------------------------------
# SECCIÓN: CÁLCULO DEL SUBTOTAL
# Recorremos la lista de productos y multiplicamos el precio por la cantidad
# de cada uno para obtener el costo total antes de descuentos.
# -----------------------------------------------------------------------------
subtotal = 0
for p in productos:
    subtotal += p["precio"] * p["cantidad"]

print("\nSubtotal de la compra:", subtotal)

# -----------------------------------------------------------------------------
# SECCIÓN: GESTIÓN DE MEMBRESÍA Y DESCUENTOS
# Primero determinamos si el cliente tiene membresía con una validación de SI/NO.
# -----------------------------------------------------------------------------
descuento = 0

while True:
    respuesta = input("¿El cliente tiene membresía? (SI/NO): ").upper()
    if respuesta == "SI":
        membresia = True
        break
    elif respuesta == "NO":
        membresia = False
        break
    else:
        print("Respuesta inválida. Escriba SI o NO.")

# Lógica de aplicación de descuentos:
# 1. Si la compra es mayor a 500, se aplica el 10% (prioridad alta).
# 2. Si no es mayor a 500 pero tiene membresía, se aplica el 5%.
if subtotal > 500:
    descuento = subtotal * 0.10
elif membresia:
    descuento = subtotal * 0.05

# Cálculo del monto final restando el descuento obtenido
total = subtotal - descuento

# -----------------------------------------------------------------------------
# SECCIÓN: PROCESO DE PAGO
# Permite al usuario elegir entre pago con efectivo (calculando cambio) 
# o pago con tarjeta.
# -----------------------------------------------------------------------------
print("\nTotal a pagar:", total)
print("Forma de pago:")
print("1. Efectivo")
print("2. Tarjeta")

while True:
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Lógica para pago en efectivo y cálculo de cambio
        while True:
            pago = input("Ingrese el monto con el que paga: ")
            if pago.isdigit():
                pago = float(pago)
                if pago >= total:
                    cambio = pago - total
                    break
                else:
                    print("El monto es insuficiente.")
            else:
                print("Ingrese un monto válido.")
        break

    elif opcion == "2":
        # Para tarjeta se asume pago exitoso y el cambio queda en 0
        print("Pago realizado con tarjeta.")
        cambio = 0 
        break

    else:
        print("Opción inválida. Elija 1 o 2.")

# -----------------------------------------------------------------------------
# SECCIÓN: RESUMEN FINAL (TICKET)
# Muestra el detalle de los productos comprados y el desglose de costos.
# -----------------------------------------------------------------------------
print("\n--- RESUMEN DE COMPRA ---")
for p in productos:
    # Imprime cada producto con su cantidad y precio unitario
    print(p["nombre"], "-", p["cantidad"], "x", p["precio"])

print("Subtotal:", subtotal)
print("Descuento aplicado:", descuento)
print("Total final:", total)
print("Cambio:", cambio)

print("\nGracias por su compra.")