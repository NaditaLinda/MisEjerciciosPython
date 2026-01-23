def leer_cotizaciones(nombre_fichero):
    """
    Lee un CSV de cotizaciones y devuelve un diccionario organizado por columnas.
    """
    columnas = {}
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as f:
            lineas = f.readlines()
            if not lineas:
                return {}

            # Proceso de la cabecera para crear las llaves del diccionario
            cabecera = lineas[0].strip().split(';')
            for nombre in cabecera:
                columnas[nombre] = []

            # Proceso los datos de cada fila
            for linea in lineas[1:]:
                valores = linea.strip().split(';')
                for i in range(len(cabecera)):
                    dato = valores[i]
                    # Convierto a float si es numérico (con manejo de coma decimal)
                    try:
                        # Reemplazamos puntos de millar por nada y comas por puntos
                        valor_limpio = float(dato.replace('.', '').replace(',', '.'))
                        columnas[cabecera[i]].append(valor_limpio)
                    except ValueError:
                        # Si no es un número (como el Nombre), se queda como string
                        columnas[cabecera[i]].append(dato)
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_fichero} no se encuentra.")
    
    return columnas

def generar_resumen(diccionario_columnas):
    """
    Calcula estadísticas, genera una tabla alineada en el archivo y la muestra en pantalla.
    """
    cabecera_formato = f"{'COLUMNA':<12} | {'MÍNIMO':>15} | {'MÁXIMO':>15} | {'MEDIA':>15}"
    separador = "-" * len(cabecera_formato)
    lineas_tabla = [cabecera_formato, separador]
    
    # Mostramos la cabecera por pantalla inmediatamente
    print(f"\n📊 RESUMEN DE COTIZACIONES:")
    print(separador)
    print(cabecera_formato)
    print(separador)

    for columna, valores in diccionario_columnas.items():
        # Filtramos solo los valores numéricos de la columna
        numeros = [v for v in valores if isinstance(v, (int, float))]
        
        if numeros:
            v_min = min(numeros)
            v_max = max(numeros)
            v_media = sum(numeros) / len(numeros)

            s_min = f"{v_min:.2f}".replace('.', ',')
            s_max = f"{v_max:.2f}".replace('.', ',')
            s_media = f"{v_media:.2f}".replace('.', ',')
            
            # Añadimos la fila al resumen (formateando con coma para el CSV resultante)
            fila = f"{columna:<12} | {s_min:>15} | {s_max:>15} | {s_media:>15}"
            lineas_tabla.append(fila)
            print(fila)

    # Escritura del archivo
    with open('resumen_cotizacion.csv', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lineas_tabla))
    
    print(separador)
    print("✅ Archivo 'resumen_cotizacion.csv' generado con la tabla alineada.")

# Ejemplo de ejecución:
datos = leer_cotizaciones('cotizacion.csv')
generar_resumen(datos)