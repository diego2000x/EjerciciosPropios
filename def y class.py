def saludar(persona):
    print(f"Hola {persona} desde el def!")

saludar("Diego")

class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
        
    def info(self):
        return f"Su nombre es {self.nombre}, tiene {self.edad} años y es de {self.ciudad}. "
    
    def gerundio(self):
        if self.ciudad == "Colin":
            return f"{self.nombre} es Colinense"
        if self.ciudad == "Talca":
            return f"{self.nombre} es Talquino"
    
diego = Persona("Diego", 30, "Talca")
javi = Persona("Javiera", 25, "Colin") 

print(diego.info()+ diego.gerundio())
print(javi.info()+ javi.gerundio())