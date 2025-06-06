def saludar(persona):
    print(f"Hola {persona} desde el def!")

saludar("Diego")

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    def info(self):
        return f"Su nombre es {self.nombre}, tiene {self.edad} años y es de {self.ciudad}."
    
diego = Persona("Diego", 30, "Talca")
javi = Persona("Javiera", 25, "Colin") 

print(diego.info())
print(javi.info())