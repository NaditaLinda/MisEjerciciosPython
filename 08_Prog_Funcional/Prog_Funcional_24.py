# Datos: Playas con longitud (m), urbanización y protección
playas_galicia = [
    {"nombre": "Rodas (Cíes)", "longitud": 1300, "urbanizacion": "Nula", "proteccion": "Máxima"},
    {"nombre": "Samil (Vigo)", "longitud": 1150, "urbanizacion": "Alta", "proteccion": "Baja"},
    {"nombre": "Melide (Ons)", "longitud": 250, "urbanizacion": "Nula", "proteccion": "Alta"},
    {"nombre": "Riazor (A Coruña)", "longitud": 610, "urbanizacion": "Alta", "proteccion": "Mínima"},
    {"nombre": "Carnota", "longitud": 7000, "urbanizacion": "Baja", "proteccion": "Alta"}
]

# Definición del criterio "Playa Salvaje" (Lambda)
# Condición: Urbanización en ['Nula', 'Baja'] Y Protección en ['Alta', 'Máxima']
es_salvaje = lambda p: p["urbanizacion"] in ["Nula", "Baja"] and \
                       p["proteccion"] in ["Alta", "Máxima"]

# Aplicación del filtro
playas_seleccionadas = list(filter(es_salvaje, playas_galicia))

# Visualización
print("Playas que conservan su estado salvaje:")
for playa in playas_seleccionadas:
    print(f"-> {playa['nombre']} ({playa['longitud']}m) - Protección: {playa['proteccion']}")