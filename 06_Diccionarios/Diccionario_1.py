divisas = {'Euro': '€', 'Dolar': '$', 'Yen': '¥'}

divisa_solicitada = input("Introduce una divisa (Euro, Dolar o Yen): ").title()

if divisa_solicitada in divisas:
    simbolo = divisas[divisa_solicitada]
    print(f"El símbolo de {divisa_solicitada} es: {simbolo}")
else:
    print("Error: La divisa no se encuentra en nuestra base de datos.")