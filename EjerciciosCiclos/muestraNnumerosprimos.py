numeros = int(input("Ingrese un numero para ver cuantos numeros primos hay entre 0 y ese numero: "))

lista = range(0, (numeros+1))
listaPrimos = []

def isPrimo(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

for numero in lista:
    if isPrimo(numero) == True:
        listaPrimos.append(numero)

print(f"Los numeros primos son: {listaPrimos}")