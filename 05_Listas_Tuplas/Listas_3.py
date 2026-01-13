# Definimos la lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Creamos una lista vacía para almacenar las notas
notas = []

# Primero preguntamos las notas
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}?: ")
    # Añadimos la nota a nuestra lista de notas
    notas.append(nota)

# Después mostramos los resultados
# Usamos range(len(...)) para tener un índice que sirva para ambas listas
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")