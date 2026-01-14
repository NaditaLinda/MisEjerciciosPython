def leer_linea_especifica():
    try:
        n = int(input("Introduce el número de la tabla (1-10): "))
        m = int(input("Introduce la línea que quieres ver (1-10): "))
        
        if not (1 <= n <= 10 and 1 <= m <= 10):
            print("Error: Ambos números deben estar entre 1 y 10.")
            return 

        # Construcción del nombre y apertura
        nombre_fichero = f"tabla-{n}.txt"

        try:
            with open(nombre_fichero, "r", encoding="utf-8") as fichero:
                # Leemos todas las líneas y las guardamos en una lista
                lineas = fichero.readlines()
                
                # Acceso por índice (Arquitectura de Listas)
                # Como las listas en Python empiezan en 0, la línea 'm' es el índice 'm-1'
                print(f"\nLínea {m} del archivo {nombre_fichero}:")
                print(lineas[m - 1].strip()) # con .strip() quito el salto de línea extra

        except FileNotFoundError:
            print(f"Error: El fichero '{nombre_fichero}' no existe.")
        except IndexError:
            print(f"Error: El fichero no tiene {m} líneas.")

    except ValueError:
        print("Error: Debes introducir números enteros.")

# Ejecuto la función
if __name__ == "__main__":
    leer_linea_especifica()