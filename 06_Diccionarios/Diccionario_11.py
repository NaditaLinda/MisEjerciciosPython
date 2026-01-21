# Defino la cadena de texto original
datos_raw = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

# Dividimos la cadena en líneas usando el carácter de salto de línea \n
lineas = datos_raw.split('\n')

# Extraemos la primera línea como cabecera y la dividimos por el separador ';'
cabecera = lineas[0].split(';')

# Inicializamos el diccionario principal
directorio_clientes = {}

# Procesamos el resto de las líneas (saltando la cabecera)
for i in range(1, len(lineas)):
    # Dividimos los valores de la línea actual
    valores = lineas[i].split(';')
    
    # El NIF es el primer elemento (índice 0)
    nif = valores[0]
    
    # Creamos el diccionario interno para los detalles del cliente
    # Mapeamos los nombres de la cabecera (desde el índice 1) con sus valores
    detalles = {}
    for j in range(1, len(cabecera)):
        detalles[cabecera[j]] = valores[j]
    
    # Añado la entrada al diccionario principal
    directorio_clientes[nif] = detalles

import pprint
pprint.pprint(directorio_clientes)