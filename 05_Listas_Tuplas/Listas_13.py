import math

entrada = input("Introduce los números de la muestra separados por comas: ")

# Convertimos la cadena en una lista de números (floats)
numeros = [float(n.replace(",", ".").strip()) for n in entrada.split(",")]

# Calculamos la Media
n = len(numeros)
media = sum(numeros) / n

# Cálculo de la Desviación Típica
# Sumatorio de (dato - media) al cuadrado
sumatorio_cuadrados = sum((x - media)**2 for x in numeros)
desviacion_tipica = math.sqrt(sumatorio_cuadrados / n)

print(f"\n--- Resultados ---")
print(f"Muestra: {numeros}")
print(f"Media: {media:.2f}")
print(f"Desviación típica: {desviacion_tipica:.2f}")