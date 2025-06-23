
while True:
    try:
        consulta = int(input("Ingrese un numero, no una letra: "))

        print(f"El numero ingresado es {consulta}.")
        break
    except ValueError:
        print("No ingresaste un numero, intentalo de nuevo.")