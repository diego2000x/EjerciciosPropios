def menu():
    try:
        selector = int(input("Que quieres hacer? 1. Sumar 2. Restar 3. Salir "))
        if selector == 1:
            sumar()
        elif selector == 2:
            restar()
        elif selector == 3:
            salir()
        else:
            print("Datos ingresados invalidos.")
    except ValueError:
        print("Por favor ingrese un numero valido.")


def sumar():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el numero a sumarle: "))
    resultado = a+b
    print(f"El resultado es {resultado}.")

def restar():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el numero a restarle: "))
    resultado = a-b
    print(f"El resultado es {resultado}.")

def salir():
    quit()

while True:
    menu()