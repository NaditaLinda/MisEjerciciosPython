# Pedimos la palabra y la pasamos a minúsculas
palabra = input("Introduce una palabra: ").lower()

# Definimos las vocales que queremos contar
vocales = "aeiou"

print(f"\nResultados para la palabra '{palabra}':")

for vocal in vocales:
    contador = palabra.count(vocal)
    print(f"La vocal '{vocal}' aparece {contador} veces.")