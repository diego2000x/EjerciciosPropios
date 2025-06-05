def saludar(persona):
    return print(f"Hola {persona} desde el def!")

saludar("Diego")

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    def info(self):
        return f"Su nombre es {self.nombre}, tiene {self.edad} años y es de {self.ciudad}."
    
Diego = Persona("Diego", 30, "Talca")
Javi = Persona("Javiera", 25, "Colin") 

print(Diego.info())
print(Javi.info())