# Creamos la lista del abecedario usando el módulo string
import string
abecedario = list(string.ascii_lowercase)

# Creamos una nueva lista filtrando las posiciones
# Recordamos que en programación la primera posición es 0
resultado = []

for i in range(len(abecedario)):
    # Las "posiciones" para un humano suelen ser 1, 2, 3... 
    # Si la posición (i + 1) NO es múltiplo de 3, la guardamos
    if (i + 1) % 3 != 0:
        resultado.append(abecedario[i])

# Mostramos la lista resultante
print(resultado)