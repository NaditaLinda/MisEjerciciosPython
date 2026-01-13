interes = 0.04  
inversion_inicial = float(input("Introduce la cantidad depositada: "))

balance_año1 = inversion_inicial * (1 + interes)

balance_año2 = balance_año1 * (1 + interes)

balance_año3 = balance_año2 * (1 + interes)

print(f"Balance tras el primer año: {round(balance_año1, 2)}")
print(f"Balance tras el segundo año: {round(balance_año2, 2)}")
print(f"Balance tras el tercer año: {round(balance_año3, 2)}")