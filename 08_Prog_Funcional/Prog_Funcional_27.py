# Datos de entrada
rias = ["Vigo", "Pontevedra", "Arousa", "Muros", "Noia"]
mareas = [3.85, 3.40, 4.10, 3.20, 3.95]

# Configuración del umbral (metros)
UMBRAL = 3.5

# Relación y filtrado
# zip(rias, mareas) crea pares como ("Vigo", 3.85)
# la lambda recibe ese par (x) y comprueba el segundo elemento (x[1])
resultado = list(filter(lambda x: x[1] > UMBRAL, zip(rias, mareas)))

# Mostrar resultados
print(f"Rías con marea superior a {UMBRAL}m:")
for ria, marea in resultado:
    print(f"- {ria}: {marea}m")