import pandas as pd

def gestionar_ventas():
    # Entrada de datos
    try:
        inicio = int(input("Introduce el año inicial: ").strip())
        fin = int(input("Introduce el año final: ").strip())
        
        ventas = {}
        
        for año in range(inicio, fin + 1):
            venta = float(input(f"Introduce las ventas para el año {año}: ".strip().replace(',', '.')))
            ventas[año] = venta

        # Creación de la Serie
        serie_ventas = pd.Series(ventas)

        # Procesamiento (Aplicación del descuento del 10%)
        # Multiplicamos por 0.9 para obtener el valor tras restar el 10%
        serie_descuento = serie_ventas * 0.9

        # Mostrar resultados
        print("\n--- Ventas Originales ---")
        print(serie_ventas)
        
        print("\n--- Ventas con Descuento (10%) ---")
        print(serie_descuento)

    except ValueError:
        print("Error: Por favor, introduce números válidos para los años y las ventas.")

if __name__ == "__main__":
    gestionar_ventas()