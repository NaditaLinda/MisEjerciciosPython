import pandas as pd
import numpy as np
from datetime import datetime

# --- PREPARACIÓN Y LIMPIEZA DE DATOS ---

# Generar un DataFrame con los datos de los cuatro ficheros
ficheros = ['emisiones-2016.csv', 'emisiones-2017.csv', 'emisiones-2018.csv', 'emisiones-2019.csv']
# Usamos un separador ';' ya que es el estándar en los datos abiertos de Madrid
df = pd.concat([pd.read_csv(f, sep=';') for f in ficheros])

# Filtrar las columnas necesarias
columnas_dias = [f'D{str(i).zfill(2)}' for i in range(1, 32)]
columnas_mantener = ['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + columnas_dias
df = df[columnas_mantener]

# Reestructurar el DataFrame (Melt)
# Pasamos de formato "ancho" (un día por columna) a formato "largo" (una fila por día)
df = df.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], 
             var_name='DIA', value_name='VALOR')

# Limpiar la columna DIA (quitar la 'D' y convertir a entero)
df['DIA'] = df['DIA'].str.strip('D').astype(int)

# Crear la columna de fecha
# Concatenamos y convertimos a datetime. errors='coerce' pondrá NaT en fechas inválidas (ej. 30 de febrero)
df['FECHA'] = pd.to_datetime(df[['ANO', 'MES', 'DIA']].rename(columns={'ANO': 'year', 'MES': 'month', 'DIA': 'day'}), 
                             errors='coerce')

# Eliminar filas con fechas no válidas y ordenar
df = df[df['FECHA'].notna()]
df = df.sort_values(['ESTACION', 'FECHA'])

# --- INFORMACIÓN GENERAL ---

print("Estaciones disponibles:", df['ESTACION'].unique())
print("Contaminantes disponibles:", df['MAGNITUD'].unique())

# --- FUNCIONES DE ANÁLISIS ---

def emisiones_rango(estacion, contaminante, fecha_inicio, fecha_fin):
    #Devuelve las emisiones de un contaminante en una estación y rango de fechas.
    criterio = (df['ESTACION'] == estacion) & \
               (df['MAGNITUD'] == contaminante) & \
               (df['FECHA'] >= fecha_inicio) & \
               (df['FECHA'] <= fecha_fin)
    return df[criterio].set_index('FECHA')['VALOR']

def resumen_por_estacion(estacion, contaminante):
    #Resumen descriptivo para una estación y contaminante concreto.
    return df[(df['ESTACION'] == estacion) & (df['MAGNITUD'] == contaminante)]['VALOR'].describe()

def media_mensual_total(contaminante, ano):
    #Emisiones medias mensuales de un contaminante y año para todas las estaciones.
    return df[(df['MAGNITUD'] == contaminante) & (df['ANO'] == ano)].groupby('MES')['VALOR'].mean()

def medias_mensuales_estacion(estacion):
    #DataFrame con medias mensuales de todos los contaminantes en una estación.
    return df[df['ESTACION'] == estacion].groupby(['MES', 'MAGNITUD'])['VALOR'].mean().unstack()

# --- RESÚMENES DESCRIPTIVOS ---

# Resumen general por contaminante
print("\n--- Resumen descriptivo por contaminante ---")
print(df.groupby('MAGNITUD')['VALOR'].describe())

# Resumen por "Distritos" (en estos archivos la estación suele representar el distrito)
print("\n--- Resumen descriptivo por Estación (Distrito) y Contaminante ---")
print(df.groupby(['ESTACION', 'MAGNITUD'])['VALOR'].describe())