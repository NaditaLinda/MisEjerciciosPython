def obtener_calificacion(nota):
    """Asocia una nota numérica con su descripción cualitativa."""
    if nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"

def filtrar_aprobados(expediente):
    """
    Recibe un diccionario {asignatura: nota} y devuelve un diccionario
    solo con los aprobados, con nombres en mayúsculas.
    """
    aprobados_transformados = {}
    
    for asignatura, nota in expediente.items():
        # Filtro: Solo procesamos si la nota es mayor o igual a 5
        if nota >= 5:
            # Transformación: Clave a mayúsculas y valor a calificación
            aprobados_transformados[asignatura.upper()] = obtener_calificacion(nota)
            
    return aprobados_transformados

# Ejemplo de uso:
mis_notas = {
    "Matemáticas": 4.0, 
    "Física": 7.5, 
    "Historia": 5.2, 
    "Programación": 9.8,
    "Inglés": 3.5
}

resultado = filtrar_aprobados(mis_notas)

print("🎓 Asignaturas Aprobadas:")
print(resultado)