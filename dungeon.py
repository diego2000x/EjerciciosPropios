import os

def limpiarPantalla():
    os.system('cls')

limpiarPantalla()

class entidad:
    
     def __init__(self, nombre, hp, ataque, nivel):
        self.nombre = nombre
        self.hp = hp
        self.ataque = ataque
        self.nivel = nivel

     def info(self):
        print(f"{self.nombre} - LVL {self.nivel}")
        print(f"{self.hp} PS")

guerrero = entidad("Guerrero", 20, 5, 1)
slime = entidad("Slime", 10, 1, 1)
pajaro = entidad("Pajarraco", 12, 2, 1)
goblin = entidad("Goblin", 14, 4, 1)

print(f"Bienvenido al calabozo {guerrero.nombre}")

