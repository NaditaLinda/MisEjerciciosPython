import matplotlib.pyplot as plt
import pandas as pd

def visualizar_finanzas(df):
    """
    Recibe un dataframe con columnas 'Ingresos' y 'Gastos'.
    Genera un gráfico de líneas comparartivo.
    """

    plt.figure(figsize=(10, 5))

    # Configuramos las 2 líneas usando 'meses' para el eje X
    plt.plot(df.index, df['Ingresos'], marker='o', label='Ingresos', color='green', linewidth=2)
    plt.plot(df.index, df['Gastos'], marker='s', label='Gastos', color='red', linewidth=2)

    #A Añadimos requisitos estéticos y técnicos
    plt.title('Evolución de ingresos y gastos', fontsize=14, fontweight='bold')
    plt.xlabel('Meses', fontsize=12)
    plt.ylabel('Gastos (€)', fontsize=12)

    # El eje debe empezar en 0
    plt.ylim(bottom=0)

    # Añado leyenda y rejilla para mejorar la lectura
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    #Mostrar resultado
    plt.show()

# --- Ejemplo de uso ---
datos = {
    'Ingresos': [12000, 15000, 13000, 17000, 16000, 19000],
    'Gastos': [10000, 11000, 12500, 12000, 13000, 14000]
}
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']

df_empresa = pd.DataFrame(datos, index=meses)
visualizar_finanzas(df_empresa)
