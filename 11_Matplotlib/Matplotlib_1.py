import matplotlib.pyplot as plt

def generar_grafico_ventas():
    # Entrada de datos
    inicio = int(input("Introduce el año de inicio: "))
    fin = int(input("Introduce el año de fin: "))

    años = []
    ventas = []

    # Recolección de datos
    for año in range(inicio, fin + 1):
        venta=float(input(f"Introduce las ventas para el año {año}: ").replace(',', '.'))
        años.append(año)
        ventas.append(venta)
    
    # Generación del gráfico
    plt.plot(años, ventas, marker= 'o', linestyle='-', color='teal', label="Ventas anuales")

    # Estética del gráfico
    plt.title(f"Evolución de ventas ({inicio} - {fin})", fontsize=14)
    plt.xlabel("Año", fontsize=12)
    plt.ylabel("Ventas (€)", fontsize=12)
    plt.xticks(años) # Asegura que cada año tenga una marca en el eje x
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    generar_grafico_ventas()


