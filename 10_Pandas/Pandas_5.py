# Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
# una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

import pandas as pd

def calcular_balance(df, meses):
    df_filtrado = df[df["Mes"].isin(meses)]
    balance_total = df_filtrado["Ventas"].sum() - df_filtrado["Gastos"].sum()

    return balance_total

#Ejemplo de uso
datos = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [30500, 35600, 28300, 33900],
    "Gastos": [22000, 23400, 18100, 20700] 
}   
df = pd.DataFrame(datos)
meses_a_calcular = ["Enero", "Marzo"]
balance = calcular_balance(df, meses_a_calcular)
print(f"El balance total para los meses {meses_a_calcular} es: {balance}")


