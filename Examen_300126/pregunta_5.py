import pandas as pd
import os

# Preparación de la ruta y carga de datos
base_path = os.path.dirname(__file__)
df_titul = pd.read_csv(os.path.join(base_path, 'titularidad.csv'))
df_propietarios = pd.read_csv(os.path.join(base_path, 'propietarios.csv'))

# Usamos el diccionario de la Pregunta 3 para máxima velocidad
propietario_por_id = df_propietarios.set_index('id_propietario')['nombre_completo'].to_dict()

def propietarios_de_finca(id_finca):
    """
    Busca los dueños de una finca y devuelve sus nombres y porcentajes.
    """
    # Filtramos la tabla de titularidad por el ID de la finca
    filas_titularidad = df_titul[df_titul['id_finca'] == id_finca]
    
    # Si no hay registros, la finca no existe o no tiene dueños registrados
    if filas_titularidad.empty:
        return f"No se han encontrado propietarios para la finca {id_finca}."

    resultado = []

    # Recorremos las filas encontradas
    for _, fila in filas_titularidad.iterrows():
        id_p = fila['id_propietario']
        porcentaje = fila['porcentaje_propiedad']
        
        # Obtenemos el nombre usando el diccionario (Mapeo)
        nombre = propietario_por_id.get(id_p, "Propietario desconocido")
        
        resultado.append({
            "nombre": nombre,
            "porcentaje": f"{porcentaje}%"
        })
        
    return resultado

try:
    # Pedimos el ID (y lo convertimos a entero inmediatamente)
    entrada = input("🏠 Introduce el código de la finca que quieres consultar (Entre 1001 y 1030): ")
    id_busqueda = int(entrada)
    
    # Llamamos a la función
    resultado = propietarios_de_finca(id_busqueda)
    
    # Resultado con formato amigable
    if isinstance(resultado, list):
        print(f"\n📋 Resultado para la finca {id_busqueda}:")
        for prop in resultado:
            print(f"   - {prop['nombre']}: {prop['porcentaje']}")
    else:
        # Aquí entraría si la función devuelve el mensaje de "No encontrado"
        print(f"\n⚠️ {resultado}")

except ValueError:
    # Si el usuario escribe algo que no es un número
    print("❌ Error: Por favor, introduce solo números para el código de la finca.")
    
