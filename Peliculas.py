# -----------------------------------------------------------------------------
# SISTEMA DE RECOMENDACIÓN DE PELÍCULAS: CINEGUIA BCS
# -----------------------------------------------------------------------------

# Base de datos de películas
peliculas = [
    {"titulo": "Diario de una pasión", "genero": "Drama", "duracion": 123, "calificacion": 4},
    {"titulo": "El increíble castillo vagabundo", "genero": "Animación", "duracion": 119, "calificacion": 5},
    {"titulo": "Shutter", "genero": "Terror", "duracion": 97, "calificacion": 4},
    {"titulo": "La hora de la desaparición", "genero": "Suspenso", "duracion": 95, "calificacion": 4},
    {"titulo": "A él no le gustas tanto", "genero": "Comedia", "duracion": 129, "calificacion": 4},
    {"titulo": "La razón de estar contigo", "genero": "Drama", "duracion": 100, "calificacion": 4},
    {"titulo": "Esposa de mentira", "genero": "Comedia", "duracion": 117, "calificacion": 4},
    {"titulo": "El día que la tierra explotó", "genero": "Ciencia ficción", "duracion": 110, "calificacion": 3},
    {"titulo": "El cadáver de la novia", "genero": "Animación", "duracion": 77, "calificacion": 5},
    {"titulo": "Mulán", "genero": "Animación", "duracion": 88, "calificacion": 4},
    {"titulo": "Parásitos", "genero": "Thriller", "duracion": 132, "calificacion": 5},
    {"titulo": "Forrest Gump", "genero": "Drama", "duracion": 142, "calificacion": 5},
    {"titulo": "El padrino", "genero": "Drama", "duracion": 175, "calificacion": 5},
    {"titulo": "Avatar", "genero": "Ciencia ficción", "duracion": 162, "calificacion": 4},
    {"titulo": "El silencio de los corderos", "genero": "Thriller", "duracion": 118, "calificacion": 5},
    {"titulo": "Buenos muchachos", "genero": "Drama", "duracion": 146, "calificacion": 5},
    {"titulo": "El código Da Vinci", "genero": "Suspenso", "duracion": 149, "calificacion": 4},
    {"titulo": "Sexto sentido", "genero": "Suspenso", "duracion": 107, "calificacion": 5},
    {"titulo": "Los juegos del hambre", "genero": "Acción", "duracion": 142, "calificacion": 4},
    {"titulo": "Coco", "genero": "Animación", "duracion": 105, "calificacion": 5},
    {"titulo": "Scrooge", "genero": "Animación", "duracion": 96, "calificacion": 4},
    {"titulo": "Horton", "genero": "Animación", "duracion": 86, "calificacion": 4},
    {"titulo": "Grinch", "genero": "Animación", "duracion": 85, "calificacion": 4},
    {"titulo": "Intensamente", "genero": "Animación", "duracion": 95, "calificacion": 5},
    {"titulo": "Zootopia", "genero": "Animación", "duracion": 108, "calificacion": 5},
    {"titulo": "Rey León", "genero": "Animación", "duracion": 88, "calificacion": 5},
    {"titulo": "Titanic", "genero": "Drama", "duracion": 195, "calificacion": 4},
    {"titulo": "Interestelar", "genero": "Ciencia ficción", "duracion": 169, "calificacion": 5},
    {"titulo": "El conjuro", "genero": "Terror", "duracion": 112, "calificacion": 4},
    {"titulo": "La isla siniestra", "genero": "Thriller", "duracion": 139, "calificacion": 4}
]

print("====================================================")
print("       BIENVENIDO AL CINEGUIA BCS")
print("====================================================")

# -----------------------------------------
# CAPTURA DE EDAD
# -----------------------------------------
while True:
    edad_texto = input("Ingresa tu edad: ")
    if edad_texto.isdigit() and int(edad_texto) > 0:
        edad = int(edad_texto)
        break
    print("Edad inválida.")

# -----------------------------------------
# PREFERENCIAS DEL USUARIO
# -----------------------------------------
genero_usuario = input("Ingresa el género que deseas ver: ").strip().capitalize()

while True:
    duracion_opcion = input("Duración deseada (Corta / Media / Larga): ").capitalize()
    if duracion_opcion in ["Corta", "Media", "Larga"]:
        break
    print("Opción inválida.")

# -----------------------------------------
# BÚSQUEDA POR TÍTULO
# -----------------------------------------
buscar_sn = input("¿Deseas buscar una película específica? (SI/NO): ").upper()

if buscar_sn == "SI":
    titulo_buscar = input("Ingresa el título: ").lower()
    encontrada = False

    for pelicula in peliculas:
        if pelicula["titulo"].lower() == titulo_buscar:
            print("Película encontrada:")
            print(pelicula["titulo"], "-", pelicula["genero"])
            encontrada = True
            break

    if not encontrada:
        print("No se encontró la película.")

# -----------------------------------------
# RECOMENDACIONES
# -----------------------------------------
print("\n--- GENERANDO RECOMENDACIONES ---")
recomendaciones = []

for pelicula in peliculas:

    # Filtro 1: Calificación mínima
    if pelicula["calificacion"] < 4:
        continue

    # Filtro 2: Restricción de edad para Thriller
    if pelicula["genero"] == "Thriller" and edad <= 18:
        continue

    # Filtro 3: Duración
    if duracion_opcion == "Corta" and pelicula["duracion"] >= 90:
        continue
    elif duracion_opcion == "Media" and not (90 <= pelicula["duracion"] <= 150):
        continue
    elif duracion_opcion == "Larga" and pelicula["duracion"] <= 150:
        continue

    # Filtro 4: Coincidencia de género
    # Se valida nuevamente la edad si el género es Thriller
    if pelicula["genero"] == genero_usuario:
        if pelicula["genero"] == "Thriller" and edad <= 18:
            continue
        recomendaciones.append(pelicula)

# -----------------------------------------
# RESULTADOS
# -----------------------------------------
if recomendaciones:
    print("Películas recomendadas:")
    for p in recomendaciones:
        print(f"- {p['titulo']} ({p['duracion']} min)")
else:
    print("No hubo coincidencias exactas.")
    print("Recomendaciones generales:")
    for p in peliculas:
        if p["calificacion"] == 5:
            print("-", p["titulo"])

print("\nFin del programa.")
