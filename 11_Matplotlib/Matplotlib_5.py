import matplotlib.pyplot as plt
import pandas as pd

def generar_grafico_evolucion(serie_ventas, tipo_grafico):
    """
    Recibe una serie de pandas y un string con el tipo de gráfico.
    Genera el gráfico solicitado con el título oficial.
    """
    # Título común para todos
    titulo_oficial = "Evolución del número de ventas"

    # Lógica para la elección del tipo de gráfico
    if tipo_grafico == 'lineas':
        plt.plot(serie_ventas.index, serie_ventas.values, marker='o', color='blue')
        
    elif tipo_grafico == 'barras':
        plt.bar(serie_ventas.index, serie_ventas.values, color='orange')
    
    elif tipo_grafico == 'sectores':
        plt.pie(serie_ventas, labels=serie_ventas.index, autopct='%1.2f%%')
        plt.axis('equal') # El gráfico de sectores se ve circular, no ovalado.

    elif tipo_grafico == 'areas':
        plt.fill_between(serie_ventas.index, serie_ventas.values, color='lightgreen', alpha=0.5)
        plt.plot(serie_ventas.index, serie_ventas.values, color='green')

    else:
        print("Error: Tipo de gráfico no reconocido. Usa: lineas, barras, sectores o areas.")
        return
    
    # Configuración común a todos los gráficos
    plt.title(titulo_oficial, fontsize=14, fontweight='bold')
    plt.xlabel("Año")
    plt.ylabel("Ventas")

    # Mostrar el resultado
    plt.show()

# Ejemplo de uso
def solicitar_datos_usuario():
    """
    Función de interfaz que solicita los datos al usuario ppr consola
    """
    try:
        # Definir el rango de tiempo
        inicio = int(input("Introduce el año de inicio: "))
        fin = int(input("Introduce el año de finalizaciÓn: "))

        datos_ventas = {}

        # Capturar datos de ventas para cada año
        for anio in range(inicio, fin +1):
            venta = float(input(f"Ventas para el {anio}: ").replace(',', '.'))
            datos_ventas[anio] = venta
        
        # Elegir el tipo de gráfico que queremos usar
        print("\nTipos de gráfico disponibles: lineas, barras, sectores, areas")
        tipo = input("¿Qué tipo de gráfico prefieres?: ").lower().strip()

        # Convertir los datos a serie Pandas y llamar a la función para generar el gráfico
        serie_usuario = pd.Series(datos_ventas)
        generar_grafico_evolucion(serie_usuario, tipo)
    
    except ValueError:
        print("Error: Por favor introduce números válidos para los años y ventas.")

# Ejecución del programa
if __name__ == "__main__":
    solicitar_datos_usuario()

        