# -----------------------------------------------------------------------------
# SISTEMA DE GESTIÓN DE TAREAS (TO-DO LIST)
# Este programa permite administrar tareas mediante una lista de diccionarios,
# incluyendo niveles de prioridad y estados de cumplimiento.
# -----------------------------------------------------------------------------

# Inicializamos una lista vacía que funcionará como nuestra base de datos temporal.
tareas = []

print("\n--- SISTEMA DE GESTIÓN DE TAREAS ---")

# -----------------------------------------------------------------------------
# BUCLE PRINCIPAL (MENÚ DE INTERACCIÓN)
# Mantiene el programa en ejecución hasta que el usuario decida salir.
# -----------------------------------------------------------------------------
while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar tareas pendientes")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # -------------------------------------------------------------------------
    # OPCIÓN 1: AGREGAR TAREA
    # Solicita datos al usuario, los valida y crea un nuevo diccionario de tarea.
    # -------------------------------------------------------------------------
    if opcion == "1":
        descripcion = input("Ingrese la descripción de la tarea: ").strip()

        # Validación: Evita que se guarden tareas sin texto.
        if descripcion == "":
            print("La descripción no puede estar vacía.")
            continue

        # Validación de Prioridad: Solo permite tres valores específicos.
        while True:
            prioridad = input("Ingrese la prioridad (Alta / Media / Baja): ").capitalize()
            if prioridad in ["Alta", "Media", "Baja"]:
                break
            else:
                print("Prioridad inválida. Use Alta, Media o Baja.")

        # Estructura de la tarea: un diccionario con 3 claves principales.
        tarea = {
            "descripcion": descripcion,
            "prioridad": prioridad,
            "completada": False  # Toda tarea nueva inicia como pendiente (False).
        }

        # Guardamos el diccionario dentro de nuestra lista 'tareas'.
        tareas.append(tarea)
        print("Tarea agregada correctamente.")

    # -------------------------------------------------------------------------
    # OPCIÓN 2: MARCAR TAREA COMO COMPLETADA
    # Muestra las tareas con su índice y cambia el estado de False a True.
    # -------------------------------------------------------------------------
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas registradas.")
            continue

        print("\nTareas:")
        # Recorremos la lista usando el índice (i) para que el usuario pueda elegir.
        for i in range(len(tareas)):
            # Operador ternario para mostrar un texto amigable según el valor booleano.
            estado = "Completada" if tareas[i]["completada"] else "Pendiente"
            print(f"{i + 1} - {tareas[i]['descripcion']} ({estado})")

        entrada = input("Seleccione el número de la tarea a completar: ")

        if entrada.isdigit():
            indice = int(entrada) - 1
            # Verificamos que el número ingresado exista en la lista.
            if 0 <= indice < len(tareas):
                tareas[indice]["completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("Número de tarea inválido.")
        else:
            print("Entrada inválida.")

    # -------------------------------------------------------------------------
    # OPCIÓN 3: MOSTRAR TAREAS PENDIENTES (ORDENADAS)
    # Filtra las tareas que no están completadas y las agrupa por importancia.
    # -------------------------------------------------------------------------
    elif opcion == "3":
        pendientes = False
        print("\nTareas pendientes (Alta → Media → Baja):")

        # Primero buscamos todas las 'Altas', luego 'Medias', luego 'Bajas'.
        for prioridad_actual in ["Alta", "Media", "Baja"]:
            for t in tareas:
                if t["prioridad"] == prioridad_actual and t["completada"] == False:
                    print(f"- {t['descripcion']} | Prioridad: {t['prioridad']}")
                    pendientes = True

        if not pendientes:
            print("No hay tareas pendientes.")

    # -------------------------------------------------------------------------
    # OPCIÓN 4: ELIMINAR TAREA (CON CONFIRMACIÓN)
    # Permite borrar un registro permanentemente después de confirmar.
    # -------------------------------------------------------------------------
    elif opcion == "4":
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")
            continue

        print("\nTareas:")
        for i in range(len(tareas)):
            print(f"{i + 1} - {tareas[i]['descripcion']}")

        entrada = input("Seleccione el número de la tarea a eliminar: ")

        if entrada.isdigit():
            indice = int(entrada) - 1
            if 0 <= indice < len(tareas):
                confirmar = input("¿Seguro que desea eliminar la tarea? (SI / NO): ").upper()
                if confirmar == "SI":
                    # .pop() elimina el elemento en la posición indicada.
                    tareas.pop(indice)
                    print("Tarea eliminada.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("Número inválido.")
        else:
            print("Entrada inválida.")

    # -------------------------------------------------------------------------
    # OPCIÓN 5: SALIR
    # Termina el bucle 'while' principal y cierra el programa.
    # -------------------------------------------------------------------------
    elif opcion == "5":
        print("Saliendo del sistema. Hasta pronto.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")