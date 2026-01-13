asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

repetir = []

for asignatura in asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}?: ").replace(",", "."))
    
    if nota < 5:
        repetir.append(asignatura)

print("\nTienes que repetir las siguientes asignaturas:")
for asignatura in repetir:
    print(asignatura)