import math

def calcular_modulo_vector(vector):
    """
    Calcula el módulo de un vector (lista de números).
    """
    if not vector:
        return 0
    
    # Sumamos los cuadrados de cada componente
    suma_cuadrados = sum(componente ** 2 for componente in vector)
    
    # Calculamos la raíz cuadrada del total
    modulo = math.sqrt(suma_cuadrados)
    
    return modulo

# Ejemplo de uso:
# Vector en 2D (3, 4) -> El módulo debería ser 5.0
vector_2d = [3, 4]
# Vector en 3D (1, 2, 2) -> El módulo debería ser 3.0
vector_3d = [1, 2, 2]

print(f"Módulo del vector 2D: {calcular_modulo_vector(vector_2d)}")
print(f"Módulo del vector 3D: {calcular_modulo_vector(vector_3d)}")