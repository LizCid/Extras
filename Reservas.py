# -----------------------------------------------------------------------------
# SISTEMA DE RESERVAS DE HOTEL
# Gestiona el inventario de habitaciones, calcula costos con descuentos
# competitivos y emite comprobantes de reserva.
# -----------------------------------------------------------------------------

# Inventario del hotel: Estructura de diccionario anidado.
habitaciones = {
    "Individual": {"precio": 800, "disponibles": 5},
    "Doble": {"precio": 1200, "disponibles": 3},
    "Suite": {"precio": 2000, "disponibles": 2}
}

# Bucle principal para mantener el sistema activo.
while True:
    print("\n--- SISTEMA DE RESERVAS ---")
    print("1. Consultar disponibilidad")
    print("2. Reservar habitación")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    # Uso de match-case para un menú más estructurado.
    match opcion:

        # ---------------------------------------------------------------------
        # CASO 1: CONSULTAR DISPONIBILIDAD
        # ---------------------------------------------------------------------
        case "1":
            print("\nHabitaciones disponibles actualmente:")
            # Usamos .items() para obtener tanto el nombre (tipo) como los datos.
            for tipo, datos in habitaciones.items():
                print(f"{tipo} - Precio: ${datos['precio']} | Disponibles: {datos['disponibles']}")

        # ---------------------------------------------------------------------
        # CASO 2: RESERVAR HABITACIÓN
        # ---------------------------------------------------------------------
        case "2":
            # MEJORA: .strip().capitalize() hace que no importe si escriben en minúsculas.
            # Ejemplo: "suite" se convierte en "Suite", coincidiendo con el diccionario.
            tipo_habitacion = input(
                "Ingresa tipo de habitación (Individual/Doble/Suite): ").strip().capitalize()

            # Validación: ¿Existe el tipo de habitación en nuestro inventario?
            if tipo_habitacion not in habitaciones:
                print("Error: El tipo de habitación no existe.")
                continue

            # Verificación de stock:
            if habitaciones[tipo_habitacion]["disponibles"] == 0:
                print(f"Lo sentimos, no hay {tipo_habitacion} disponibles.")
                print("Te sugerimos las siguientes opciones con disponibilidad:")

                # Sugerencia automática: Recorremos el inventario buscando stocks > 0.
                for tipo, datos in habitaciones.items():
                    if datos["disponibles"] > 0:
                        print(f"- {tipo} (${datos['precio']} por noche)")
                continue

            # Validación de entrada numérica para las noches.
            while True:
                noches_texto = input("¿Cuántas noches se hospedará?: ")
                if noches_texto.isdigit():
                    noches = int(noches_texto)
                    if noches > 0:
                        break
                print("Error: Ingrese un número entero de noches.")

            # Validación de membresía.
            while True:
                respuesta = input("¿Es miembro frecuente? (SI/NO): ").upper()
                if respuesta == "SI":
                    miembro = True
                    break
                elif respuesta == "NO":
                    miembro = False
                    break
                else:
                    print("Por favor, responda únicamente SI o NO.")

            # Cálculos financieros iniciales.
            precio_noche = habitaciones[tipo_habitacion]["precio"]
            costo_sin_descuento = precio_noche * noches

            # -----------------------------------------------------------------
            # LÓGICA DE DESCUENTOS (Prioriza el mayor)
            # -----------------------------------------------------------------
            descuento_porcentaje = 0

            if noches >= 5:
                descuento_porcentaje = 0.15  # 15% por estancia larga.
            elif miembro:
                descuento_porcentaje = 0.10  # 10% por ser miembro.

            monto_descuento = costo_sin_descuento * descuento_porcentaje
            total_final = costo_sin_descuento - monto_descuento

            # Resumen previo a la confirmación.
            print("\n--- RESUMEN DE RESERVA ---")
            print(f"Habitación: {tipo_habitacion}")
            print(f"Noches: {noches}")
            print(f"Subtotal: ${costo_sin_descuento}")
            print(f"Descuento ({int(descuento_porcentaje*100)}%): -${monto_descuento}")
            print(f"Total a pagar: ${total_final}")

            # Confirmación final y actualización de inventario.
            while True:
                confirmar = input("\n¿Desea confirmar la reserva? (SI/NO): ").upper()
                if confirmar == "SI":
                    # Restamos una unidad del inventario real.
                    habitaciones[tipo_habitacion]["disponibles"] -= 1

                    print("\n¡RESERVA EXITOSA!")
                    print("Se ha generado su comprobante digital.")
                    break
                elif confirmar == "NO":
                    print("Operación cancelada. No se realizó ningún cargo.")
                    break
                else:
                    print("Opción inválida.")

        # ---------------------------------------------------------------------
        # CASO 3: SALIR
        # ---------------------------------------------------------------------
        case "3":
            print("Cerrando sistema de recepción. ¡Buen día!")
            break

        # CASO POR DEFECTO: Si el usuario ingresa algo distinto a 1, 2 o 3.
        case _:
            print("Opción no válida. Por favor, seleccione una opción del menú.")