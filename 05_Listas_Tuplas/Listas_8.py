palabra = input("Introduce una palabra: ")

# pasamos la palabra a minúsculas
palabra = palabra.lower()

# Usamos la técnica de 'slicing' [:: -1] para crear la versión invertida de la palabra
palabra_invertida = palabra[::-1]

# Comparamos y mostramos el resultado
if palabra == palabra_invertida:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")