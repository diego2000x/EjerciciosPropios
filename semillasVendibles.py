import os

os.system('cls')

semillasBase = 0
semillaBonita = 0
semillaPremium = 0
espacios = 3

plantaBase = 0
plantaBonita = 0
plantaPremium = 0

crecimientoSemillas= 60 #Segundos

precioSemillaBonita = 100 #semilla base
precioSemillaPremium = 100 #semillas bonitas

def bienvenida():
    global semillasBase
    print("Como eres nuevo aqui, y necesitas empezar por algun lado, te dare tu primera semilla :D")
    semillasBase = 1

def saludo():
    print("Bienvenido al Jardin!")

def plantarSemilla():
    global semillasBase, plantaBase, espacios
    
    if semillasBase >= 1 and espacios >= 1:
        semillasBase = semillasBase -1
        plantaBase = plantaBase +1
        espacios -= 1
        print("Plantaste una semilla.")
        crecimiento()
        menu()
    else:
        print("No tienes una semilla :(")
        menu()

def crecimiento():
    pass

def info():
    print(f"Tienes {semillasBase} semillas simples, {plantaBase} plantas, {semillaBonita} semillas bonitas, {plantaBonita} plantas bonitas.")
    if plantaBase <= 1:
        print(f"Tienes {plantaBase} plantas que esta creciendo, faltan {crecimientoSemillas} segundos para que florezca.")
    menu()

def comprarSemillaBonita():
    global semillasBase, semillaBonita
    if semillasBase >= precioSemillaBonita:
        semillasBase= semillasBase - precioSemillaBonita
        semillaBonita= semillaBonita+1
    else:
        print("No tienes para comprar una semilla bonita :(")
    menu()

def salir():
    quit()

def menu():
    accion = int(input("Que deseas hacer? 1.Revisar tus cosas. 2.Plantar una semilla. 3.Comprar una semilla bonita. 4.Salir "))
    if accion == 1:
        info()
    elif accion ==2:
        plantarSemilla()
    elif accion == 3:
        comprarSemillaBonita()
    elif accion == 4:
        salir()

saludo()

bienvenida()

menu()










