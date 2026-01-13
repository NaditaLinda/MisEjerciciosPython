# Creamos la lista de números del 1 al 10
# Usamos list() y range() para no escribir uno a uno
numeros = list(range(1, 11))

# Invertimos la lista
numeros.reverse()

# Convertimos los números a texto y los unimos con comas
# Primero transformamos cada número en string para poder usar .join()
resultado = ", ".join(map(str, numeros))

# Mostramos por pantalla
print(resultado)