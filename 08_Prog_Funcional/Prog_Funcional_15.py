# Datos de entrada: Especies con (Nombre, Población, Nivel de Protección 1-5)
especies = [
    {"nombre": "Lince Ibérico", "poblacion": 1100, "proteccion": 5},
    {"nombre": "Oso Pardo", "poblacion": 400, "proteccion": 4},
    {"nombre": "Lobo Ibérico", "poblacion": 2500, "proteccion": 3},
    {"nombre": "Águila Imperial", "poblacion": 500, "proteccion": 5},
    {"nombre": "Ardilla Roja", "poblacion": 50000, "proteccion": 1}
]

# Lógica de clasificación (Lambda)
# Calculamos un "Riesgo" combinando protección y población.
# A mayor nivel de protección y menor población -> Mayor prioridad.
# Fórmula: (Nivel * 1000) / Población
calcular_prioridad = lambda e: (
    e["nombre"],
    "CRÍTICA" if (e["proteccion"] * 1000 / e["poblacion"]) > 5 else "ESTABLE"
)

# Transformación
clasificacion = list(map(calcular_prioridad, especies))

# Resultado
print("Clasificación de Especies para Conservación:")
for nombre, estado in clasificacion:
    print(f"- {nombre}: Estado {estado}")