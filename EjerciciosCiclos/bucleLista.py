lista = []
entrada = ""

while entrada != "no":
    entrada = input("Nombra Pokemon, si no quieres nombrar mas escribe 'no' \n")
    if entrada != "no":
        lista.append(entrada)

print(lista)