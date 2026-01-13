import math 

def calculadora_cientifica():
    print("---Calculadora Científica Iterativa---")

    # Entrada de datos
    try:
        limite = int(input("Introduce un número entero (límite de la tabla):"))
        print("\nFunciones disponibles: seno, coseno, tangente, exponencial y logaritmo")
        operacion=input("¿Qué función deseas aplicar?").lower().strip()

        # Diccionario de funciones para mapear la entrada del usuario
        funciones = {
            "seno" : math.sin,
            "coseno" : math.cos,
            "tangente" : math.tan,
            "exponencial" : math.exp,
            "logaritmo" : math.log
        }
        
        # Validación y procesamiento
        if operacion in funciones:
            func_seleccionada = funciones[operacion]

            # Encabezado de la tabla
            print(f"\n{'Número (n)':<12} | {operacion.capitalize() + '(n)':<15}")
            print("-" * 30)

            # Bucle para generar los resultados
            for i in range(1, limite + 1):
                resultado = func_seleccionada(i)
                # Doy formato con 4 decimales para mayor claridad
                print(f"{i:<12} | {resultado:<15.4f}")
        else:
            print("Error: la función introducida no es válida.")
    
    except ValueError:
        print("Error: Por favor introduce un número entero válido.")

# Ejecuto la función
if __name__ == "__main__":
    calculadora_cientifica()

                  


