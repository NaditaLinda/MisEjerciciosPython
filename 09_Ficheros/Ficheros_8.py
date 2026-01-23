import csv

def leer_calificaciones(fichero):
    """Lee el CSV y devuelve una lista de diccionarios ordenada por apellidos."""
    lista_alumnos = []
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            # Usamos DictReader para que las cabeceras sean las claves automáticamente
            lector = csv.DictReader(f, delimiter=';')
            for fila in lector:
                # Convertimos datos a tipos numéricos para poder operar
                # Asumimos que los decimales vienen con coma
                alumno = {
                    'Apellidos': fila['Apellidos'],
                    'Nombre': fila['Nombre'],
                    'Asistencia': float(fila['Asistencia'].replace('%', '').replace(',', '.')),
                    'Parcial1': float(fila['Parcial1'].replace(',', '.')),
                    'Parcial2': float(fila['Parcial2'].replace(',', '.')),
                    'Practicas': float(fila['Practicas'].replace(',', '.'))
                }
                lista_alumnos.append(alumno)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {fichero}")
        return []

    # Ordenamos la lista por el campo 'Apellidos'
    return sorted(lista_alumnos, key=lambda x: x['Apellidos'])

def añadir_nota_final(lista_alumnos):
    """Calcula la nota final ponderada y la añade a cada diccionario."""
    for alumno in lista_alumnos:
        # Pesos: 30% Parcial1, 30% Parcial2, 40% Prácticas
        nota_final = (alumno['Parcial1'] * 0.3) + \
                     (alumno['Parcial2'] * 0.3) + \
                     (alumno['Practicas'] * 0.4)
        alumno['Nota Final'] = round(nota_final, 2)
    return lista_alumnos

def separar_aprobados_suspensos(lista_alumnos):
    """Divide a los alumnos en dos listas según los criterios de aprobado."""
    aprobados = []
    suspensos = []
    
    for alumno in lista_alumnos:
        # Criterios: Asistencia >= 75%, todos los exámenes >= 4, final >= 5
        asistencia_ok = alumno['Asistencia'] >= 75
        examenes_ok = alumno['Parcial1'] >= 4 and alumno['Parcial2'] >= 4 and alumno['Practicas'] >= 4
        nota_ok = alumno['Nota Final'] >= 5
        
        if asistencia_ok and examenes_ok and nota_ok:
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
            
    return aprobados, suspensos

# Ejemplo de uso:
alumnos = leer_calificaciones('calificaciones.csv')
alumnos_con_nota = añadir_nota_final(alumnos)
aptos, no_aptos = separar_aprobados_suspensos(alumnos_con_nota)

print(f"✅ Alumnos Aprobados ({len(aptos)}): {[a['Apellidos'] for a in aptos]}")
print(f"❌ Alumnos Suspensos ({len(no_aptos)}): {[a['Apellidos'] for a in no_aptos]}")