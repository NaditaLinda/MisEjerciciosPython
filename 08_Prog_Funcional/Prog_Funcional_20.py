# Datos de entrada: Distancia en km y Desnivel positivo en metros
rutas_courel = [
    {"nombre": "Devesa da Rogueira", "distancia": 14, "desnivel": 800},
    {"nombre": "Pico de Montouto", "distancia": 8, "desnivel": 450},
    {"nombre": "Fervenza de Vieiros", "distancia": 3, "desnivel": 150},
    {"nombre": "Val das Mouras", "distancia": 6, "desnivel": 200}
]

# Lógica de cálculo (Lambda)
# Aplicamos una fórmula donde el desnivel tiene un peso significativo:
# Dificultad = (Distancia * 0.5) + (Desnivel / 100)
calcular_esfuerzo = lambda r: {
    "ruta": r["nombre"],
    "puntos_dificultad": round((r["distancia"] * 0.5) + (r["desnivel"] / 100), 1)
}

# Transformación mediante map
indice_dificultad = list(map(calcular_esfuerzo, rutas_courel))

# Visualización de los resultados
print("Evaluación de rutas en O Courel:")
for item in indice_dificultad:
    print(f"-> {item['ruta']}: {item['puntos_dificultad']} puntos")