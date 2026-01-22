def convertir_notas_a_calificaciones(notas):
    """
    Recibe una lista de notas numéricas y devuelve una lista 
    con las calificaciones cualitativas correspondientes.
    """
    calificaciones = []
    
    for nota in notas:
        if nota < 5:
            calificaciones.append("Suspenso")
        elif nota < 7:
            calificaciones.append("Aprobado")
        elif nota < 9:
            calificaciones.append("Notable")
        else:
            calificaciones.append("Sobresaliente")
            
    return calificaciones

# Ejemplo de uso:
mis_notas = [4.5, 6.2, 7.5, 9.8, 5.0]
resultado = convertir_notas_a_calificaciones(mis_notas)

print(f"Notas: {mis_notas}")
print(f"Calificaciones: {resultado}")