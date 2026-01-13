frase = input("Introduce una frase: ")
vocal_usuario = input("Introduce una vocal: ")

# Mapeo las vocales con y sin tilde
mapeo_tildes = {
    'a': 'á',
    'e': 'é',
    'i': 'í',
    'o': 'ó',
    'u': 'ú',
}

vocal_min = vocal_usuario.lower()
vocal_may = vocal_usuario.upper()

frase_modificada = frase.replace(vocal_min, vocal_may)

if vocal_min in mapeo_tildes:
    pareja_min = mapeo_tildes[vocal_min]
    pareja_may = pareja_min.upper()
    frase_modificada = frase_modificada.replace(pareja_min, pareja_may)

print("Resultado:", frase_modificada)