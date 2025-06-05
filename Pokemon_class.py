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

SaludarPokemon("Pikachu")
SaludarPokemon("Charmander")

pikachu = Pokemon("Pikachu", "electrico", 10)
charmander = Pokemon("Charmander", "fuego", 9)

print(pikachu.info())
print(charmander.info())

pikachu.atacar()
charmander.atacar()
pikachu.atacar()

print(f"{charmander.nombre} ha sido derrotado, {pikachu.nombre} ganó el combate!")

