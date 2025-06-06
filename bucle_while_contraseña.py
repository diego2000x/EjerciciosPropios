usuario = "Diego"
password = "Torchic"

passInput = input("Ingrese su contraseña: ")

while passInput != password:
    print(f"Contraseña incorrecta, intentelo de nuevo.")
    passInput = input("Ingrese su contraseña: ")

print(f"Contraseña correcta! Bienvenido {usuario}!")