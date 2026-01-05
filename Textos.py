# -------------------------------------------------
# ANALIZADOR DE TEXTO SIMPLE - Versión mejorada
# -------------------------------------------------

# Solicitar texto al usuario
texto = input("Ingresa un párrafo de texto: ")

# Validar texto vacío o solo espacios
if texto.strip() == "":
    print("El texto no puede estar vacío.")
else:

    # ---------------------------------------------
    # CONTADOR DE CARACTERES
    # ---------------------------------------------
    total_caracteres = len(texto)

    caracteres_sin_espacios = 0
    signos_exclamacion = 0

    for caracter in texto:
        if caracter != " ":
            caracteres_sin_espacios += 1
        if caracter == "!":
            signos_exclamacion += 1

    # ---------------------------------------------
    # PROCESAR PALABRAS
    # ---------------------------------------------
    palabras_originales = texto.split(" ")
    palabras = []

    for palabra in palabras_originales:
        palabra_limpia = palabra.strip(".,!?")
        if palabra_limpia != "":
            palabras.append(palabra_limpia)

    numero_palabras = len(palabras)

    # Palabra más larga y más corta
    palabra_larga = palabras[0]
    palabra_corta = palabras[0]

    for palabra in palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
        if len(palabra) < len(palabra_corta):
            palabra_corta = palabra

    # ---------------------------------------------
    # CONTAR ORACIONES
    # ---------------------------------------------
    oraciones = 0
    for caracter in texto:
        if caracter == "." or caracter == "!" or caracter == "?":
            oraciones += 1

    # ---------------------------------------------
    # BUSCAR UNA PALABRA
    # ---------------------------------------------
    buscar = input("Ingresa una palabra a buscar: ").strip().lower()
    contador_busqueda = 0

    for palabra in palabras:
        if palabra.lower() == buscar:
            contador_busqueda += 1

    # ---------------------------------------------
    # CLASIFICACIÓN DEL TEXTO
    # ---------------------------------------------
    if numero_palabras > 100:
        clasificacion = "Largo"
    elif numero_palabras >= 50:
        clasificacion = "Mediano"
    else:
        clasificacion = "Corto"

    # ---------------------------------------------
    # TEXTO EXPRESIVO
    # ---------------------------------------------
    porcentaje_exclamacion = (signos_exclamacion / total_caracteres) * 100

    # ---------------------------------------------
    # RESULTADOS
    # ---------------------------------------------
    print("\n--- RESULTADOS DEL ANÁLISIS ---")
    print("Total de caracteres (con espacios):", total_caracteres)
    print("Total de caracteres (sin espacios):", caracteres_sin_espacios)
    print("Número de palabras:", numero_palabras)
    print("Número de oraciones:", oraciones)
    print("Palabra más larga:", palabra_larga)
    print("Palabra más corta:", palabra_corta)
    print("La palabra", buscar, "aparece", contador_busqueda, "veces.")
    print("Clasificación del texto:", clasificacion)

    if porcentaje_exclamacion > 10:
        print("Texto muy expresivo.")
