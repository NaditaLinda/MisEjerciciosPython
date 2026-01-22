def obtener_calificacion(nota):
    """Función auxiliar para clasificar la nota numérica."""
    if nota < 5:
        return "Suspenso"
    elif nota < 7:
        return "Aprobado"
    elif nota < 9:
        return "Notable"
    else:
        return "Sobresaliente"

def procesar_expediente(asignaturas):
    """
    Recibe un diccionario {asignatura: nota} y devuelve 
    otro con {ASIGNATURA: Calificación}.
    """
    expediente_transformado = {}
    
    for asignatura, nota in asignaturas.items():
        # Transformamos la clave a mayúsculas
        clave_mayuscula = asignatura.upper()
        
        # Transformamos la nota a calificación cualitativa
        calificacion = obtener_calificacion(nota)
        
        # Guardamos en el nuevo diccionario
        expediente_transformado[clave_mayuscula] = calificacion
            
    return expediente_transformado

# Ejemplo de uso:
notas_alumno = {"Matemáticas": 4.5, "Física": 6.5, "Programación": 9.2}
resultado = procesar_expediente(notas_alumno)

print("📋 Expediente Final:")
print(resultado)