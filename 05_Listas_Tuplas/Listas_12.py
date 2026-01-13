# Definición de las matrices (listas de listas)
# Matriz A (2x3)
A = [[1, 2, 3], 
     [4, 5, 6]]

# Matriz B (3x2)
B = [[-1, 0], 
     [0, 1], 
     [1, 1]]

# Preparamos la matriz de resultado con ceros (tendrá tamaño 2x2)
# (Filas de A x Columnas de B)
resultado = [[0, 0], 
             [0, 0]]

# Lógica de la multiplicación (Triple bucle)
# Recorremos las filas de A
for i in range(len(A)):
    # Recorremos las columnas de B
    for j in range(len(B[0])):
        # Recorremos las filas de B (o columnas de A) para el producto escalar
        for k in range(len(B)):
            resultado[i][j] += A[i][k] * B[k][j]

# Mostramos el resultado de forma elegante
print("El producto de las matrices es:")
for fila in resultado:
    print(fila)