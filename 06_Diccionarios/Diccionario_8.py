entrada = input("Introduce las palabras (español:inglés) separadas por comas: ")
traductor = {}

for par in entrada.split(','):
    if ":" in par:
        clave, valor = par.split(':')
        # Guarda la clave en minúsculas para que la búsqueda sea uniforme
        traductor[clave.strip().lower()] = valor.strip()

frase = input("\nIntroduce una frase en español: ")

# Elimino las comas de la frase completa antes de procesarla
frase_sin_comas = frase.replace(",", "")

palabras = frase_sin_comas.split()
frase_traducida = []

for palabra in palabras:
    # Convierte cada palabra a minúsculas para buscarla en el diccionario
    traduccion = traductor.get(palabra.lower(), palabra)
    frase_traducida.append(traduccion)

print("\nFrase traducida (limpia de comas e ignorando mayúsculas):")
print(" ".join(frase_traducida))