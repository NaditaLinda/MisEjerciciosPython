# Entrada de datos (uso float para permitir decimales)
renta = float(input("Introduce tu renta anual en €: "))

# Clasificación por tramos
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

# Resultados
print(f"Tu tipo impositivo es del {tipo}%.")