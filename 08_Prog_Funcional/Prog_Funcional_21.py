# Datos de entrada: Especies con peso (kg) y longitud (m)
especies_marinas = [
    {"especie": "Merluza", "peso": 4.5, "longitud": 0.85},
    {"especie": "Pulpo", "peso": 3.2, "longitud": 0.60},
    {"especie": "Sardina", "peso": 0.05, "longitud": 0.15},
    {"especie": "Rodaballo", "peso": 2.8, "longitud": 0.55}
]

# Función lambda para calcular el índice
# Fórmula: Peso / (Longitud^2)
calc_biomasa = lambda e: {
    "especie": e["especie"],
    "indice_biomasa": round(e["peso"] / (e["longitud"] ** 2), 2)
}

# Transformación de la lista mediante map
biomasa_relativa = list(map(calc_biomasa, especies_marinas))

# Visualización de resultados
print("Índice de Biomasa Relativo por Especie:")
for registro in biomasa_relativa:
    print(f"- {registro['especie']}: {registro['indice_biomasa']}")