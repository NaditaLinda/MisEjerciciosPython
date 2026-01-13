frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

# Procesamos y reemplazamos la vocal en minúscula por la mayúscula
frase_modificada = frase.replace(vocal.lower(), vocal.upper())

print("Resultado:", frase_modificada)