password = "Torchic"
intentos = 3

def correcto():
    print("Contraseña correcta!")

while intentos > 0:
    entrada = input("Ingrese su contraseña: ")
    intentos -=1
    if entrada == password:
        correcto()
        break
    elif intentos == 0:
        print("Se acabaron tus intentos:(")
    else:
        print(f"Contraseña incorrecta, te quedan {intentos} intentos.")
        