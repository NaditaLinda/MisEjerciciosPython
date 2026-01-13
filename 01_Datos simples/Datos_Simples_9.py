cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interés anual (en porcentaje)?: "))
años = int(input("¿Número de años?: "))

capital_final = cantidad * (1 + interes / 100) ** años

print(f"Capital obtenido en la inversión: {round(capital_final, 2)}")