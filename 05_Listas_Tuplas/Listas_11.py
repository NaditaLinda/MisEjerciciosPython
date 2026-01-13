# Almacenamos los vectores en listas
vector_a = [1, 2, 3]
vector_b = [-1, 0, 2]

# Variable para acumular la suma
producto_escalar = 0

# Calculamos el producto recorriendo los índices
# Ambos vectores tienen la misma longitud (3)
for i in range(len(vector_a)):
    # Multiplicamos componentes y sumamos al acumulador
    producto_escalar += vector_a[i] * vector_b[i]

# Mostramos el resultado
print(f"El producto escalar de {vector_a} y {vector_b} es: {producto_escalar}")