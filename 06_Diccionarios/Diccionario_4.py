meses = {
    '01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril',
    '05': 'mayo', '06': 'junio', '07': 'julio', '08': 'agosto',
    '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'
}

fecha = input("Introduce una fecha (dd/mm/aaaa): ")

partes = fecha.split('/')

dia_mostrar = int(partes[0])

mes_buscar = partes[1].zfill(2)

anio = partes[2]

if mes_buscar in meses:
    nombre_mes = meses[mes_buscar]
    print(f"{dia_mostrar} de {nombre_mes} de {anio}")
else:
    print("Mes no válido.")