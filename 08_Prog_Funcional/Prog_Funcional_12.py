# Datos de entrada: (Nombre de la ría, diferencia en metros)
rias_marea = [
    ("Vigo", 3.2),
    ("Arousa", 2.8),
    ("Pontevedra", 3.5),
    ("Muros", 2.1),
    ("Ferrol", 3.8),
    ("Coruña", 2.9)
]

umbral = 3.0

# Con filter busco las rías que superan el umbral
# Con soted ordeno el resultado de mayor a menor marea
resultado = sorted(
    filter(lambda ria: ria[1] > umbral, rias_marea),
    key=lambda x: x[1],
    reverse=True
)

print(f"Rías con marea superior a {umbral}m (ordenadas):")
for nombre, altura in resultado:
    print(f"- {nombre}: {altura}m")