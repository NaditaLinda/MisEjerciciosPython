contrasena_maestra = input("Define la contraseña que quieres guardar: ")

intento = ""

while intento != contrasena_maestra:
    intento = input("Introduce la contraseña para acceder: ")
    
    if intento != contrasena_maestra:
        print("❌ Contraseña incorrecta. Prueba de nuevo.")

print("✅ ¡Acceso concedido! Bienvenido al sistema.")