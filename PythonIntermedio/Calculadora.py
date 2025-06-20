# Calculadora
selector = 0
opciones = ["Sumar", "Restar", "Multiplicar", "Dividir", "Salir"]

print("Bienvenido a la calculadora! \n")

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b

def salir():
    exit()

def menu():
    global selector, opciones
    print("Que quieres hacer?")
    
    for i, opcion in enumerate(opciones,1):
        print(f"{i}. {opcion}")

    selector = int(input("=>"))
    if selector == 5:
        salir()
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    print("El resultado es: ")
    if selector == 1:
        print(sumar(num1,num2))
    elif selector == 2:
        print(restar(num1,num2))
    elif selector == 3:
        print(multiplicar(num1,num2))
    elif selector == 4:
        if num2 != 0:
            print(dividir(num1,num2))
        else:
            print("No se puede dividir por 0.")

while True:
    menu()
    