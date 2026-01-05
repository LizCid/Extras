# -----------------------------------------------------------------------------
# JUEGO DE ADIVINANZA DE NÚMEROS
# El objetivo es que el usuario adivine un número generado aleatoriamente
# por la computadora dentro de un rango y con un límite de intentos.
# -----------------------------------------------------------------------------

# Importamos la función 'randint' de la librería 'random' para generar números enteros
from random import randint

print("\nBienvenido al juego de adivinanza")
print("Adivina el número secreto entre 1 y 100")

# -----------------------------------------------------------------------------
# BUCLE PRINCIPAL (REINICIO DEL JUEGO)
# Este 'while True' permite que el juego vuelva a empezar si el usuario lo desea.
# -----------------------------------------------------------------------------
while True:

    # Generamos un nuevo número secreto al azar en cada partida
    numero_secreto = randint(1, 100)

    # Configuración de los límites del juego
    intentos_maximos = 5
    intentos = 0

    print("\nTienes un máximo de 5 intentos\n")

    # -------------------------------------------------------------------------
    # BUCLE DE INTENTOS
    # Se repite mientras el jugador no haya superado el límite de 5 intentos.
    # -------------------------------------------------------------------------
    while intentos < intentos_maximos:

        print("Intentos restantes:", intentos_maximos - intentos)

        # Capturamos la entrada del usuario y limpiamos espacios vacíos
        entrada = input("Ingresa tu número: ").strip()

        # Validación 1: Verificar que el campo no esté vacío
        if entrada == "":
            print("Error: no puedes dejar el campo vacío.\n")
            continue

        # Validación 2: Verificar que el texto ingresado sea realmente un número
        if not entrada.isdigit():
            print("Error: debes ingresar un número válido.\n")
            continue

        # Convertimos la entrada de texto a un número entero para poder comparar
        numero_usuario = int(entrada)

        # Validación 3: El número debe estar dentro del rango permitido (1 a 100)
        if numero_usuario < 1 or numero_usuario > 100:
            print("El número debe estar entre 1 y 100.\n")
            continue

        # Si el número es válido, sumamos uno a la cuenta de intentos realizados
        intentos += 1

        # Lógica de comparación y pistas
        if numero_usuario > numero_secreto:
            print("Más bajo\n")  # El número secreto es menor al ingresado

        elif numero_usuario < numero_secreto:
            print("Más alto\n")  # El número secreto es mayor al ingresado

        else:
            # Caso de acierto: Se felicita y se rompe el bucle de intentos con 'break'
            print("\nFelicidades, adivinaste el número en", intentos, "intentos.")
            break

    # -------------------------------------------------------------------------
    # CONDICIÓN DE DERROTA
    # Si al terminar el bucle no se acertó el número, revelamos el secreto.
    # -------------------------------------------------------------------------
    if intentos == intentos_maximos and numero_usuario != numero_secreto:
        print("\nSe acabaron los intentos.")
        print("El número secreto era:", numero_secreto)

    # -------------------------------------------------------------------------
    # VALIDACIÓN DE REINICIO
    # Un bucle pequeño para asegurar que el usuario solo responda SI o NO.
    # -------------------------------------------------------------------------
    while True:
        respuesta = input("\n¿Deseas jugar otra vez? (SI/NO): ").strip().upper()

        if respuesta == "SI":
            # Rompe este bucle interno para volver al inicio del bucle principal
            break
        elif respuesta == "NO":
            # Despide al usuario y cierra el programa completamente
            print("\nGracias por jugar.")
            exit()
        else:
            # Si escribe cualquier otra cosa, el programa vuelve a preguntar
            print("Respuesta inválida. Escribe SI o NO.")