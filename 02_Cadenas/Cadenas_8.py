entrada = input("Introduce el precio (ej. 15.95 o 15,95): ")

# Aquí reeemplzamos la coma "," por punto "." para que funcione el programa
precio_normalizado = entrada.replace(",", ".")

euros, centimos = precio_normalizado.split(".")

print(f"Euros: {euros}")
print(f"Céntimos: {centimos}")