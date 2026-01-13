# Recibo el dato y lo convierto a entero
numero = int (input("Introduce un número entero: "))

# Lógica usando el operador módulo (%)
if numero % 2 == 0:
    print(f"El número {numero} es PAR.")
else:
    print(f"El número {numero} es IMPAR.")