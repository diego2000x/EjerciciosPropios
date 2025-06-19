numeros = []
suma = 0

while True:
    num = int(input("Ingrese numeros y se sumaran hasta que ingrese 0: "))
    if num == 0:
        break
    numeros.append(num)

for numero in numeros:
    suma = suma + numero

print(suma)