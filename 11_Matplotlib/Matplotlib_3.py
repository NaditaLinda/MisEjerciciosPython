import matplotlib.pyplot as plt
import pandas as pd

def generar_boxplot_notas(serie_notas):
    """
    Recibe una serie de pandas y genera un diagrama de cajas.
    """

    # Crear la figura
    plt.boxplot(serie_notas.dropna(), vert=True, patch_artist=True)
    plt.title('Distribución de notas', fontsize=14, fontweight='bold')

    # Personalizo los ejes para que se vea profesional
    plt.ylabel('Calificación (0-10)')
    plt.xticks([1], ['Clase A'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Mostrar el gráfico
    plt.show()

# Ejemplo de uso creando una serie de pandas con notas ficticias
notas_alumnos = pd.Series([2, 4, 5, 5, 6, 7, 7, 8, 9, 10, 1])

generar_boxplot_notas(notas_alumnos)
