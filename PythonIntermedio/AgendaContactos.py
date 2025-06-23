#Numero Cookie: +56 9 5981 8845
#Numero Mio: +56 9 8189 8266

contactos = {} #Diccionario
opciones= ["Agregar contacto", "Ver contactos", "Buscar contacto", "Eliminar contacto", "Salir"]
selector = 0

def agregarContacto():
    nombre = input("Ingrese el nombre de su contacto: ").title()
    numero = int(input("Ingrese el numero de su contacto: "))

    contactos[nombre] = numero

    print(f"El contacto {nombre} ha sido guardado.")

def verContactos():
    for contacto, numero in contactos.items():
        print(f"Nombre: {contacto} Numero: {numero}")

def buscarContacto():
    nombre = input("Ingrese el nombre de su contacto: ").title()
    print(f"El numero de su contacto {nombre} es {contactos[nombre]}")

def eliminarContacto():
    print("Que contacto desea eliminar? ")
    for contacto, numero in contactos.items():
        print(f"Nombre: {contacto}, Numero: {numero}.")
    nombre = input("=>").title()
    if nombre in contactos:
        del contactos[nombre]
    else:
        print("No se encontro ese contacto.")

def salir():
    quit()

def menu():
    print("Que deseas hacer?")
    for i, opcion in enumerate(opciones,1):
        print(f"{i}. {opcion}")
    selector = int(input("=> "))
    if selector == 1:
        agregarContacto()
    elif selector == 2:
        verContactos()
    elif selector == 3:
        buscarContacto()
    elif selector == 4:
        eliminarContacto()
    elif selector == 5:
        salir()
    else:
        print("Opcion invalida.")

while True:
    menu()