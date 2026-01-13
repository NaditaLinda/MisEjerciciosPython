email_usuario = input("Introduce tu correo electrónico: ")

nombre_usuario = email_usuario.split('@')[0]

nuevo_email = nombre_usuario + "@ceu.es"

print("Tu nuevo correo es:", nuevo_email)