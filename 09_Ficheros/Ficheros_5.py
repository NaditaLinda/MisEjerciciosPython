import urllib.request

def consultar_pib_eurostat():
    # Nueva URL de la API de Eurostat (SDMX 3.0)
    # Usamos format=tsv y compress=false para obtener el texto plano directamente
    url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/sdg_08_10/1.0?compress=false&format=tsv"
    
    pais_buscado = input("Introduce las iniciales del país (ej. ES, FR, DE, IT): ").strip().upper()

    try:
        # 1. Conexión y descarga
        print("Conectando con la nueva API de Eurostat...")
        with urllib.request.urlopen(url) as response:
            # Decodificamos el flujo de bytes a texto (UTF-8)
            contenido = response.read().decode('utf-8')
            lineas = contenido.split('\n')

        # 2. Procesamiento de la cabecera (Años)
        # La primera columna es "freq,unit,na_item,geo\TIME_PERIOD", el resto son los años
        cabecera = lineas[0].split('\t')
        años = [anio.strip() for anio in cabecera[1:]]

        encontrado = False
        
        # 3. Búsqueda y limpieza de datos
        for linea in lineas[1:]:
            if not linea.strip():
                continue
            
            columnas = linea.split('\t')
            # Extraemos los metadatos de la primera columna
            metadatos = columnas[0].split(',')
            # El código del país (geo) suele ser el último elemento del primer bloque
            codigo_pais = metadatos[-1].split('\\')[0].strip()

            if codigo_pais == pais_buscado:
                encontrado = True
                print(f"\n📊 PIB per cápita para {codigo_pais}:")
                print("-" * 35)
                
                valores = columnas[1:]
                # Iteramos sobre años y valores simultáneamente
                for i in range(len(años)):
                    # Limpiamos posibles 'flags' (letras al final del número)
                    valor_raw = valores[i].strip()
                    valor_limpio = valor_raw.split(' ')[0] # Ej: "32000 p" -> "32000"
                    
                    if valor_limpio == ":":
                        valor_limpio = "Dato no disponible"
                    
                    print(f"Año {años[i]}: {valor_limpio}")
                break

        if not encontrado:
            print(f"❌ No se encontró información para el código '{pais_buscado}'.")

    except Exception as e:
        print(f"⚠️ Error en la comunicación: {e}")

if __name__ == "__main__":
    consultar_pib_eurostat()