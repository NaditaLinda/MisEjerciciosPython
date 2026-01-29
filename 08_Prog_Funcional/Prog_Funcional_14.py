# Datos de entrada (Lista de diccionarios)
rios_galicia = [
    {"nombre": "Miño", "longitud": 315, "caudal": 340},
    {"nombre": "Sil", "longitud": 234, "caudal": 184},
    {"nombre": "Ulla", "longitud": 132, "caudal": 79},
    {"nombre": "Tambre", "longitud": 125, "caudal": 54},
    {"nombre": "Eume", "longitud": 80, "caudal": 15}
]

# Definición del umbral (fórmula: longitud * caudal > 10000)
# Esta fórmula es un ejemplo para determinar si es "caudaloso"
es_caudaloso = lambda r: (r["nombre"], (r["longitud"] * r["caudal"]) > 10000)

# 3. Transformación de la lista
resultado = list(map(es_caudaloso, rios_galicia))

# Visualización del resultado
for rio in resultado:
    print(f"Río: {rio[0]} | ¿Es caudaloso?: {rio[1]}")