import matplotlib.pyplot as plt
import pandas as pd

def generar_tarta_ventas(serie_ventas, titulo):
    """
    Recibe una serie de pandas con ventas trimestrales y un título.
    Genera un diagrama de sectores y lo guarda como PNG.
    """
    # Definir la figura
    plt.figure(figsize=(8, 6))

    # Creo el diagrama de sectores usando autopct='%1.2f%%' para 2 decimales
    plt.pie(serie_ventas, labels=serie_ventas.index, autopct='%1.2f%%', 
            startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99'])
    
    # Agregar título y ajuste circular
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.axis('equal')

    # Guardamos la figura como PNG
    nombre_archivo = f"{titulo}.png"
    plt.savefig(nombre_archivo)
    print(f"Archivo guardado correctamente como: {nombre_archivo}")

    # MOstrar la figura
    plt.show()

# Ejemplo de uso
ventas_q1 = pd.Series([1500.80, 1280.30, 1840.70], index = ['Enero', 'Febrero', 'Marzo'])
generar_tarta_ventas(ventas_q1, 'Ventas_Primer_trimestre')

