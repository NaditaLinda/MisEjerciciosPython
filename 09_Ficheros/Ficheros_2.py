def leer_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10 para leer su tabla: "))
            if 1 <= n <= 10:
                break
            else:
                print("Error: El número debe estar entre 1 y 10.")
        except ValueError:
            print("Error: Debes introducir un número entero.")

    # Construcción del nombre del archivo
    nombre_fichero = f"tabla-{n}.txt"

    # Intento de lectura con manejo de errores de sistema
    try:
        # Abro en modo "r" (read - lectura)
        with open(nombre_fichero, "r", encoding="utf-8") as fichero:
            contenido = fichero.read()
            print(f"\nMostrando el contenido de: {nombre_fichero}")
            print("-" * 30)
            print(contenido)
            print("-" * 30)
            
    except FileNotFoundError:
        # Se ejecuta solo si el archivo no existe en la carpeta
        print(f"Error: El fichero '{nombre_fichero}' no existe. ¿Has generado la tabla antes?")

# Llamada a la función
if __name__ == "__main__":
    leer_tabla_multiplicar()