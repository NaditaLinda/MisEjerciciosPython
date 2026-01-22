def contar_frecuencia(cadena):
    """
    Crea un diccionario con la frecuencia de cada palabra en una cadena.
    """
    palabras = cadena.split()
    frecuencias = {}
    
    for palabra in palabras:
        # Limpiamos la palabra (opcional: pasar a minúsculas)
        palabra = palabra.lower()
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
            
    return frecuencias

def palabra_mas_repetida(frecuencias):
    """
    Encuentra la palabra con mayor frecuencia en el diccionario.
    """
    mas_frecuente = ""
    maximo = 0
    
    for palabra, cuenta in frecuencias.items():
        if cuenta > maximo:
            maximo = cuenta
            mas_frecuente = palabra
            
    return (mas_frecuente, maximo)

# Ejemplo de uso:
texto = "Hola hola que tal tal tal estas"
dicc_frecuencias = contar_frecuencia(texto)
resultado = palabra_mas_repetida(dicc_frecuencias)

print(f"Diccionario de frecuencias: {dicc_frecuencias}")
print(f"Palabra más repetida: '{resultado[0]}' con {resultado[1]} apariciones.")