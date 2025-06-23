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
    "Bulbasour": {
        "Vida": 22,
        "Ataque": 8,
        "Tipo" : "Planta"
    }
}

def mostrarPokemon():
    for i in Pokemon:
        print(f"{i}")

mostrarPokemon()