import random

intento = 0
numeros = []

for i in range(1,11):
    num = i
    numeros.append(num)

aleatorio = random.choice(numeros)

while intento != aleatorio:
    intento = int(input("Adivina el numero del 1 al 10: "))
    if intento != aleatorio:
        print("Fallaste :(")
    
print("Acertaste!")