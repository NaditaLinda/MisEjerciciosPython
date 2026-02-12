import matplotlib.pyplot as plt

def generar_grafico_notas():
    # Recolección de datos
    asignaturas = ['Matemáticas', 'Física', 'Química', 'Programación', 'Lengua']
    notas = []

    print("Introduce las notas para cada asignatura:")
    for asignatura in asignaturas:
        nota = float(input(f"{asignatura}: ").replace(',', '.'))
        notas.append(nota)
    # Generación del gráfico de barras
    colores = ['skyblue', 'salmon', 'lightgreen', 'orange', 'plum']
    plt.bar(asignaturas, notas, color=colores, edgecolor='black')

    # Características del gráfico
    plt.title('Calificaciones del curso', fontsize=15, fontweight='bold')
    plt.xlabel('Asignaturas', fontsize=12)
    plt.ylabel('Notas', fontsize=12)
    plt.ylim(0, 10) # Queremos que el eje Y 'Notas' vaya de 0 a 10

    # Añado una línea horizontal en el 5 (para destacar aprobados)
    plt.axhline(y=5, color='red', linestyle='--', label='Aprobado')
    plt.legend()

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    generar_grafico_notas()

