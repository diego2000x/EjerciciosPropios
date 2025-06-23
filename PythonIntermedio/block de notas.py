print("Bienvenido al block de notas!")

def escribirNota():
    nota = input("Escriba su nota a guardar: ")
    with open("notas.txt", "a") as archivo:
        archivo.write(nota+ "\n")

def leerNotas():
    with open("notas.txt", "r") as archivo:
        print(archivo.read())

def limpiarArchivo():
    with open("notas.txt", "w") as archivo:
        archivo.write("")

def menu():
    selector = int(input("Que desea hacer? 1. Escribir una nota. 2. Leer las notas. 3. Salir. 4. Limpiar TXT."))
    if selector == 1:
        escribirNota()
    elif selector == 2:
        leerNotas()
    elif selector == 3:
        quit()
    elif selector == 4:
        limpiarArchivo()
    else:
        print("Seleccion no valida \n")

while True:
    menu()