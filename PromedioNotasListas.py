#crear una aplicacion que ingresa una cantidad indeterminada de notas,
#las guarda en una lista y calcula el promedio

lista= []
cantidadNotas= int(input("Ingrese la cantidad de notas a promediar: "))

for i in range(cantidadNotas):
    nota = float(input("Ingrese la nota: "))
    lista.append(nota)

def promedio(listaDeNotas):
    suma = 0
    for nota in listaDeNotas:
        suma = suma + nota
    promedio = suma/(len(listaDeNotas))
    return promedio

resultado = promedio(lista)

print(f"El promedio de las notas es {resultado}")
