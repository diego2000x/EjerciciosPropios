import os
import msvcrt #Importa opciones de Windows como presionar cualquier tecla para continuar.

def limpiarPantalla():
    os.system('cls')

def pressAnyKey():
    msvcrt.getch()

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
     
     def aparecio(self):
         print(f"Un {self.nombre} ha aparecido!")
     
     def atacar(self, enemigo):
         enemigo.hp -= self.ataque
         print(f"{self.nombre} atacó a {enemigo.nombre} quitandole {self.ataque} PS.")

     def batalla(self, enemigo):
         enemigo.aparecio()
         pressAnyKey()
         pelearOHuir = input("Quieres pelear con el? s/n: ").lower()
         if pelearOHuir == "s":
             limpiarPantalla()
             self.info()
             enemigo.info()
             pressAnyKey()
             limpiarPantalla()
             self.atacar(enemigo)
             pressAnyKey()
             enemigo.atacar(self)
             pressAnyKey()
             self.info()
             enemigo.info()

             if self.hp > 0 or enemigo.hp > 0:
                 pass

         else:
             print("Has huido.")


guerrero = entidad("Guerrero", 20, 5, 1)
slime = entidad("Slime", 10, 1, 1)
pajaro = entidad("Pajarraco", 12, 2, 1)
goblin = entidad("Goblin", 14, 4, 1)
orco = entidad("Orco", 20, 5, 1)

print(f"Bienvenido al calabozo {guerrero.nombre}!")
pressAnyKey()

guerrero.batalla(slime)

