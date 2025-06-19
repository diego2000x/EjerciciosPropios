import random
import time

class Pokemon:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    
    def saludar(self, enemigo):
        print(f"{self.nombre} se ha unido a la batalla!")
        print(f"{enemigo.nombre} se ha unido a la batalla!")
    
    def atacar(self, enemigo):
        ataque = self.ataque+random.randrange(-2,3)
        print(f"{self.nombre} hizo {ataque} puntos de daño a {enemigo.nombre}.")
        enemigo.vida = enemigo.vida - ataque
        if enemigo.vida < 0:
            enemigo.vida = 0
        print(f"La vida restante de {enemigo.nombre} es {enemigo.vida}.")

    def batalla(self, enemigo):
        self.saludar(enemigo)
        
        while self.vida > 0 and enemigo.vida > 0:
            
            if self.vida > 0:
                time.sleep(3)
                self.atacar(enemigo)
                if enemigo.vida <= 0:
                    print(f"{enemigo.nombre} ha sido derrotado!")
                    break
            if enemigo.vida > 0:
                time.sleep(3)
                enemigo.atacar(self)
                if self.vida <= 0:
                    print(f"{self.nombre} ha sido derrotado!")
                    break
        if self.vida > 0:
            print(f"{self.nombre} ha ganado la batalla!")
        elif enemigo.vida > 0:
            print(f"{enemigo.nombre} ha ganado la batalla!")
            

pikachu = Pokemon("Pikachu", 100, 10)
charmander = Pokemon("Charmander", 90, 12)

pikachu.batalla(charmander)

