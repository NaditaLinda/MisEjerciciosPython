def guardar_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("Error: El número debe estar entre 1 y 10.")
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

    nombre_fichero = f"tabla-{n}.txt"

    # Escritura en el fichero
    # 'with' asegura que el archivo se cierre automáticamente al terminar
    with open(nombre_fichero, "w") as fichero:
        for i in range(1, 11):
            linea = f"{n} x {i} = {n * i}\n"
            fichero.write(linea)

    print(f"\n¡Éxito! La tabla del {n} se ha guardado en el archivo: {nombre_fichero}")

# Ejecutar la función
if __name__ == "__main__":
    guardar_tabla_multiplicar()