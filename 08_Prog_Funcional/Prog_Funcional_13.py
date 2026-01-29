# Datos iniciales: Árboles típicos de Galicia
bosque = [
    {"especie": "Carballo", "altura": 25, "edad": 80},   # Índice: 0.31
    {"especie": "Castiñeiro", "altura": 18, "edad": 30}, # Índice: 0.60
    {"especie": "Bidueiro", "altura": 15, "edad": 20},   # Índice: 0.75
    {"especie": "Sobreira", "altura": 12, "edad": 40},   # Índice: 0.30
    {"especie": "Amieiro", "altura": 14, "edad": 15}     # Índice: 0.93
]

umbral_madurez = 0.5

# Calculamos el índice de madurez para cada árbol usando map()
# Usamos {**arbol, ...} para crear un nuevo diccionario que incluya la clave 'madurez'
arboles_con_indice = map(
    lambda arbol: {**arbol, "madurez": arbol["altura"] / arbol["edad"]}, 
    bosque
)

# Filtramos los árboles que superan el umbral con filter()
arboles_maduros = filter(
    lambda arbol: arbol["madurez"] > umbral_madurez, 
    arboles_con_indice
)

# Convertimos el iterador final en una lista para visualizarlo
resultado = list(arboles_maduros)

# Mostrar resultados
print(f"Árboles con madurez forestal > {umbral_madurez}:")
for a in resultado:
    print(f"- {a['especie']}: Índice {a['madurez']:.2f} (H: {a['altura']}m, E: {a['edad']} años)")