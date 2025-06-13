numeros = []

for i in range (1,6):
    num = int(input("Ingrese un numero: "))
    numeros.append(num)

for numero in numeros:
    if numero < 0:
        print(f"{numero} es negativo.")