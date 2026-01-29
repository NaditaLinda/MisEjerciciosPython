# Datos de entrada: Producción en kilogramos por ría
produccion_ria = [
    {"nombre": "Arousa", "kg": 25400},
    {"nombre": "Muros e Noia", "kg": 12800},
    {"nombre": "Vigo", "kg": 18900},
    {"nombre": "Pontevedra", "kg": 9500}
]

# Factor de sostenibilidad (ejemplo: 0.85 para ajustar a cuotas permitidas)
FACTOR_SOSTENIBILIDAD = 0.85

# Transformación: kg a toneladas y aplicación del factor
# Fórmula: (kg / 1000) * factor
transformar_a_toneladas = lambda dato: {
    "ria": dato["nombre"],
    "toneladas_sostenibles": round((dato["kg"] / 1000) * FACTOR_SOSTENIBILIDAD, 3)
}

# Ejecución del mapeo
produccion_final = list(map(transformar_a_toneladas, produccion_ria))

# Visualización de resultados
for registro in produccion_final:
    print(f"Ría: {registro['ria']} | Producción: {registro['toneladas_sostenibles']} t")