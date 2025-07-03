import os
import time as t
import random


poke_disponibles = {
    "Pikachu": ["Pikachu", 20, 10, "Electrico"],
    "Charmander": ["Charmander", 18, 12, "Fuego"],
    "Bulbasaur" : ["Bulbasaur", 22, 9, "Planta"],
    "Squirtle" : ["Squirtle", 20, 10, "Agua"]
}

miPoke = ""
enemigo = ""
ganador= ""

def bienvenida():
    global miPoke, enemigo, jugador, oponente
    print("Bienvenido al combate Pokemon!")
    print("Con que Pokemon quieres luchar?")
    for nombre in poke_disponibles:
        print(nombre)
    while True:
        miPoke = input("=>").title()
        if miPoke in poke_disponibles:
            print(f"Has seleccionado a {miPoke}.")
            jugador = Pokemon(*poke_disponibles[miPoke])
            break
        else:
            print("Seleccion invalida, intentalo otra vez.")
    print("Contra quien quieres luchar?")
    for nombre in (poke_disponibles):
        print(nombre)
    while True:
        enemigo = input("=>").title()
        if enemigo in poke_disponibles:
            print(f"Has seleccionado a {enemigo}")
            oponente = Pokemon(*poke_disponibles[enemigo])
            break
        else:
            print("Seleccion invalida, intetalo de nuevo.")


class Pokemon:
    def __init__(self, nombre, vida, ataque, tipo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
    
    def estado(self):
        print(f"{self.nombre} tiene {self.vida} PS restantes.")
    
    debilidades = {
        "Fuego" : "Agua",
        "Agua" : "Planta",
        "Planta" : "Fuego"
    }
    
    def debilidad(self, enemigo):
        if Pokemon.debilidades.get(enemigo.tipo) == self.tipo:
            self.ataque = self.ataque*1.2
            
        
    def atacar(self, enemigo):
        ataque = round(self.ataque+random.randrange(-2,3))
        enemigo.vida = enemigo.vida - ataque
        print(f"{self.nombre} ha hecho {ataque} puntos de daño a {enemigo.nombre}.")
        t.sleep(1)
        if Pokemon.debilidades.get(enemigo.tipo) == self.tipo:
            print("Fue muy efectivo!")

    
    def batalla(self, enemigo):
        global ganador
        os.system("cls")
        print(f"{self.nombre} se ha unido a la batalla!")
        t.sleep(1)
        print(f"{enemigo.nombre} quiere combatir!")
        t.sleep(1)
        
        self.debilidad(enemigo)
        enemigo.debilidad(self)
        self.estado()
        t.sleep(1)
        enemigo.estado()
        t.sleep(1)
        while self.vida > 0 or enemigo.vida > 0:
            self.atacar(enemigo)
            if enemigo.vida <= 0:
                t.sleep(1)
                print(f"{enemigo.nombre} se ha quedado sin puntos de salud.")
                t.sleep(1)
                print(f"{self.nombre} ha ganado el combate!")
                ganador = f"{self.nombre} ha vencido a {enemigo.nombre}."
                break
            enemigo.estado()
            t.sleep(1)
            enemigo.atacar(self)
            if self.vida <= 0:
                t.sleep(1)
                print(f"{self.nombre} se ha quedado sin puntos de salud.")
                t.sleep(1)
                print(f"{enemigo.nombre} ha ganado el combate!")
                ganador = f"{enemigo.nombre} ha vencido a {self.nombre}."
                break
            self.estado()
            t.sleep(1)


bienvenida()

jugador.batalla(oponente)

with open("historial.txt", "a") as historial:
    historial.write(ganador+"\n")