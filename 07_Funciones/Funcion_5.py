import math

# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)

# Función para calcular el volumen del cilindro
def calcular_volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro usando la función del área del círculo."""
    area_base = calcular_area_circulo(radio)
    return area_base * altura

# Ejemplo de uso:
r = 5
h = 10
print(f"Área del círculo (r={r}): {calcular_area_circulo(r):.2f}")
print(f"Volumen del cilindro (r={r}, h={h}): {calcular_volumen_cilindro(r, h):.2f}")