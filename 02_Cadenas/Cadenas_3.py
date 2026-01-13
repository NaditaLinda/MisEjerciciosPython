nombre = input("¿Cómo te llamas? ")

nombre_mayusculas = nombre.upper()
nombre_sin_espacios = nombre.replace(" ", "")
numero_letras = len(nombre_sin_espacios)

print(f"{nombre_mayusculas} tiene {numero_letras} letras (sin contar espacios)")