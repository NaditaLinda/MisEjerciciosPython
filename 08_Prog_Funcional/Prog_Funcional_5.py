def mapear_longitudes_limpio(frase):
    """
    Recibe una frase, elimina las comas y devuelve un diccionario 
    con las palabras y su longitud real.
    """
    # Limpieza: eliminamos todas las comas de la cadena
    # Reemplazamos "," por una cadena vacía ""
    frase_limpia = frase.replace(",", "")
    
    # Dividimos la frase limpia en palabras
    palabras = frase_limpia.split()
    
    # Creamos el diccionario de frecuencias
    return {palabra: len(palabra) for palabra in palabras}

# Ejemplo de uso:
texto_con_comas = "Hola, esto es una prueba, con varias, comas"
resultado = mapear_longitudes_limpio(texto_con_comas)

print(f"Texto original: {texto_con_comas}")
print(f"Resultado: {resultado}")