Pokemon = {
    "Pikachu": {
        "Vida": 20,
        "Ataque" : 10,
        "Tipo" : "Electrico"
    },
    "Charmander": {
        "Vida": 18,
        "Ataque": 12,
        "Tipo" : "Fuego"
    },
    "Bulbasaur": {
        "Vida": 22,
        "Ataque": 8,
        "Tipo" : "Planta"
    }
}

def mostrarPokemon():
    for i in Pokemon:
        print(f"{i}")

def buscarPokemon():
    consulta = input("Ingrese el pokemon que quiere consultar: ")
    if consulta in Pokemon:
        print(f"Las estadisticas de {consulta} son: ")
        print(Pokemon.get(consulta))
    else:
        print("No se encontro el pokemon.")

def menu():
    print("Bienvenido al diccionario Pokemon en python! Que quieres hacer?")
    print("1. Revisar Pokemon en el diccionario.")
    print("2. Consultar los datos de un Pokemon.")
    print("3. Salir.")
    selector = int(input("=> "))
    if selector == 1:
        mostrarPokemon()
    elif selector == 2:
        buscarPokemon()
    elif selector == 3:
        quit()

while True:
    menu()
