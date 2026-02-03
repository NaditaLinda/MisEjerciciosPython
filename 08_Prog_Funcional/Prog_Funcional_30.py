# Datos de entrada (Listas paralelas)
especies = ["Merluza", "Sardina", "Pulpo", "Xurelo", "Abadejo"]
pesos_capturados = [1500, 850, 420, 2200, 950]  # Peso en kg

# Umbral de sostenibilidad (ejemplo: 1000 kg)
LIMITE_SOSTENIBLE = 1000

# Proceso: Asociar y Filtrar
# zip une las listas en pares: [('Merluza', 1500), ('Sardina', 850)...]
# filter aplica la lambda para comprobar si el peso (x[1]) supera el límite
excesos = list(filter(lambda x: x[1] > LIMITE_SOSTENIBLE, zip(especies, pesos_capturados)))

# Visualización de resultados
print("ALERTA: Especies que exceden el límite sostenible:")
for especie, peso in excesos:
    print(f"- {especie}: {peso} kg (Exceso de {peso - LIMITE_SOSTENIBLE} kg)")