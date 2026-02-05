"""
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las
siguientes columnas: nombre (nombre de la empresa), Final (precio de la acción al cierre 
de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo 
de la acción durante la jornada), volumen (Volumen al cierre de bolsa), Efectivo 
(capitalización al cierre en miles de euros). Construir una función que construya un 
DataFrame a partir de un fichero con el formato anterior y devuelva otro DataFrame con 
el mínimo, el máximo y la media de cada columna
"""

import pandas as pd

def procesar_cotizacion(fichero):
    df = pd.read_csv(fichero, sep=';', decimal=',')
    resultado = pd.DataFrame({
        'Mínimo' : [df['Mínimo'].min()],
        'Máximo' : [df['Máximo'].max()],
        'Media' : [df ['Final'].mean()]
    })

    return resultado

#Ejemplo de uso
fichero = "cotizacion.csv"
resultado = procesar_cotizacion(fichero)
print(resultado)

