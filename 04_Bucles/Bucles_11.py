palabra = input("Introduce una palabra: ")

print("Las letras al revés son:")

for i in range(len(palabra) - 1, -1, -1):
    print(palabra[i])