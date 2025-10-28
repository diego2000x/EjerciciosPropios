class Sucursal:
    def __init__(self, nombre, direccion, email):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email

    def gestionEmpleados(self):
        pass

    def gestionAutomoviles(self):
        pass

class Vehiculo:
    def __init__(self, patente, marca, modelo, year, precio, estado):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.precio = precio
        self.estado = estado

    def rentarAutomovil(self):
        pass

    def devolverAutomovil(self):
        pass

class Cliente:
    def __init__(self, run, nombre, apellido, direccion, telefono):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
    
    def registrarCliente(self):
        pass

    def actualizarDatos(self):
        pass

    def eliminarCliente(self):
        pass

    def verHistorialRentas(self):
        pass

    def infoCliente(self):
        pass

    def historialSiniestros(self):
        pass

    def registrarSiniestro(self):
        pass


class Empleado:
    def __init__ (self, codigo, run, password, nombre, apellido, cargo, sucursal):
        self.codigo = codigo
        self.run = run
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.sucursal = sucursal