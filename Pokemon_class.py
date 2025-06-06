def SaludarPokemon(nombre):
    print(f"{nombre} se ha unido a la batalla!")

class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
    
    def info(self):
        return f"{self.nombre} es un Pokemon tipo {self.tipo}, de nivel {self.nivel}"
    
    def atacar(self):
        print(f"{self.nombre} ha realizado un ataque tipo {self.tipo}!")
    
    def subirNivel(self):
        self.nivel += 1
        print(f"{self.nombre} ha subido al nivel {self.nivel}")

    def batalla(self, enemigo):
        if self.nivel > enemigo.nivel:
            self.atacar()
            enemigo.atacar()
            print(f"{self.nombre} ha derrotado a {enemigo.nombre}!")
            self.subirNivel()
        elif self.nivel < enemigo.nivel:
            print(f"{self.nombre} ha sido derrotado por {enemigo.nombre}.")
        else:
            print("Es un empate!")

SaludarPokemon("Pikachu")
SaludarPokemon("Charmander")

pikachu = Pokemon("Pikachu", "electrico", 10)
charmander = Pokemon("Charmander", "fuego", 9)

print(pikachu.info())
print(charmander.info())

Pokemon.batalla(pikachu, charmander)



