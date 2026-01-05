# -----------------------------------------------------------------------------
# CALCULADORA DE GASTOS MENSUALES
# Este programa gestiona finanzas personales organizando gastos por categorías
# y calculando porcentajes de ahorro y alertas de presupuesto.
# -----------------------------------------------------------------------------

# Diccionario principal: las llaves serán las categorías y los valores serán listas.
gastos = {}

# -----------------------------------------------------------------------------
# ENTRADA DE INGRESOS
# Validamos que el ingreso sea un número positivo antes de continuar.
# -----------------------------------------------------------------------------
while True:
    ingreso_texto = input("Ingresa tu ingreso mensual: ")
    if ingreso_texto.isdigit():
        ingreso = float(ingreso_texto)
        if ingreso > 0:
            break
    print("Ingreso inválido. Ingresa solo números.")

# Definimos las categorías que el sistema aceptará para mantener el orden.
categorias_validas = [
    "Gastos fijos",
    "Gastos variables",
    "Gastos hormiga",
    "Gastos discrecionales"
]

# -----------------------------------------------------------------------------
# BUCLE PRINCIPAL (MENÚ)
# -----------------------------------------------------------------------------
while True:
    print("\n--- MENÚ DE GASTOS ---")
    print("1. Agregar gasto")
    print("2. Ver totales")
    print("3. Buscar gasto por descripción")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    # -------------------------------------------------------------------------
    # OPCIÓN 1: AGREGAR GASTO
    # Permite clasificar un gasto nuevo dentro de las categorías permitidas.
    # -------------------------------------------------------------------------
    if opcion == "1":
        print("\nCategorías disponibles:")
        for cat in categorias_validas:
            print("-", cat)

        categoria = input("Categoría del gasto: ").strip()

        # Verificamos que la categoría escrita exista en nuestra lista de permitidas.
        if categoria not in categorias_validas:
            print("Categoría inválida.")
            continue

        # Validación de descripción: solo letras y espacios para evitar caracteres extraños.
        while True:
            descripcion = input("Descripción del gasto: ").strip()
            if descripcion != "" and descripcion.replace(" ", "").isalpha():
                break
            print("Descripción inválida. Solo letras y espacios.")

        # Validación de monto: debe ser un número positivo.
        while True:
            monto_texto = input("Monto del gasto: ")
            if monto_texto.isdigit():
                monto = float(monto_texto)
                if monto > 0:
                    break
            print("Monto inválido. Ingresa solo números.")

        # Si es la primera vez que usamos esta categoría, inicializamos su lista.
        if categoria not in gastos:
            gastos[categoria] = []

        # Creamos el registro del gasto individual.
        gasto = {
            "descripcion": descripcion,
            "monto": monto
        }

        # Agregamos el diccionario del gasto a la lista de esa categoría.
        gastos[categoria].append(gasto)
        print("Gasto agregado correctamente.")

    # -------------------------------------------------------------------------
    # OPCIÓN 2: VER TOTALES Y ADVERTENCIAS
    # Realiza cálculos matemáticos sobre los datos almacenados.
    # -------------------------------------------------------------------------
    elif opcion == "2":
        total_mensual = 0
        print("\n--- RESUMEN DE GASTOS ---")

        # Primer recorrido: Calcular cuánto se gastó en total.
        for categoria in gastos:
            total_categoria = 0
            # Sumamos todos los montos dentro de la categoría actual.
            for gasto in gastos[categoria]:
                total_categoria += gasto["monto"]
            
            total_mensual += total_categoria
            print(f"{categoria}: ${total_categoria}")

        print("\nTotal mensual gastado: $", total_mensual)

        # SECCIÓN DE ALERTAS:
        # Usamos operadores lógicos para detectar desbalances financieros.
        for categoria in gastos:
            suma_cat = sum(g["monto"] for g in gastos[categoria])
            
            # Advertencia: Si una sola categoría consume más del 50% del total.
            if total_mensual > 0 and suma_cat > (total_mensual * 0.5):
                print(f"¡ADVERTENCIA!: {categoria} representa más del 50% de tus gastos.")

        # SECCIÓN DE AHORRO:
        ahorro = ingreso - total_mensual
        # Si el ahorro supera el 20% del ingreso inicial.
        if ingreso > 0 and ahorro > (ingreso * 0.2):
            print("¡Excelente trabajo! Has logrado ahorrar más del 20% de tu sueldo.")
        elif ahorro < 0:
            print("Cuidado: Tus gastos superan tus ingresos.")

    # -------------------------------------------------------------------------
    # OPCIÓN 3: BUSCAR GASTO
    # Implementa una búsqueda lineal comparando strings.
    # -------------------------------------------------------------------------
    elif opcion == "3":
        buscar = input("Ingresa la descripción a buscar: ").strip()
        encontrado = False

        # Navegamos por la estructura: Diccionario -> Listas -> Diccionarios.
        for categoria, lista_gastos in gastos.items():
            for gasto in lista_gastos:
                # Comparamos en minúsculas para que la búsqueda no sea sensible a mayúsculas.
                if gasto["descripcion"].lower() == buscar.lower():
                    print(f"Encontrado en {categoria}: ${gasto['monto']}")
                    encontrado = True

        if not encontrado:
            print("No se encontró ningún gasto con esa descripción.")

    # -------------------------------------------------------------------------
    # OPCIÓN 4: SALIR
    # -------------------------------------------------------------------------
    elif opcion == "4":
        print("Programa finalizado. ¡Cuida tus finanzas!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")