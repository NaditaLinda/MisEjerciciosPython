peso=float(input("Introduce tu peso en kg:"))
altura=float(input("Introduce tu estatura en metros: "))

imc=peso/(altura**2)

print(f"Tu índice de masa corporal imc es: {round(imc, 2)}")
