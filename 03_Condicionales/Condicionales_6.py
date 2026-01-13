# Entrada de datos
nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M para mujer, H para hombre)? ")

# Normalización para evitar errores con mayúsculas/minúsculas
# Usamos .upper() para asegurarnos de comparar siempre en mayúsculas
nombre_u = nombre.upper()
sexo_u = sexo.upper()

# Lógica de asignación de grupo
# Grupo A: (Mujer AND < M) OR (Hombre AND > N)
if (sexo_u == "M" and nombre_u < "M") or (sexo_u == "H" and nombre_u > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Tu nombre es {nombre}, tu sexo es {sexo} y perteneces al grupo: {grupo}")