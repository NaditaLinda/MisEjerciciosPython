frase = input("Introduce una frase: ")
letra_objetivo = input("Introduce la letra que quieres buscar: ")

contador = 0

for caracter in frase:
    if caracter == letra_objetivo:
        contador += 1

print(f"La letra '{letra_objetivo}' aparece {contador} veces en la frase.")