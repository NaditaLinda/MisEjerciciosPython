import pandas as pd
import matplotlib.pyplot as plt

def graficar_cotizaciones_bancos(fichero):

    """
    Lee un .csv de cotizaciones y grafica el cierre de cada empresa
    """
    # Carga de datos
    df=pd.read_csv(fichero, sep=';', decimal=',')

    #Preparar el gráfico
    plt.figure(figsize=(10, 6))

    # Agrupo cada banco para dibujar 1 línea por cada uno
    for empresa, datos in df.groupby('Empresa'):
        plt.plot(datos['Cierre'].values, label=empresa)
    
    # Personalizo el gráfico
    plt.title('Evolución de las cotizaciones al cierre', fontsize=14)
    plt.xlabel('Sesiones / Tiempo', fontsize=12)
    plt.ylabel('Precio de cierre (€)', fontsize=12)
    plt.legend(title='Empresas', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.5) # Para cuadrícula de fondo
    plt.xticks(rotation=45)

    # Mostrar el gráfico
    plt.savefig('cotizaciones_bancos.png')
    print("Gráfico generado con éxito: 'cotizaciones_bancos.png'")

# Ejemplo de uso
graficar_cotizaciones_bancos('bancos.csv')

              