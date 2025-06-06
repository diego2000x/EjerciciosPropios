bosque = ["Pikachu", "Caterpie", "Weedle", "Bulbasaur"]
cueva = ["Zubat", "Geodude", "Graveler", "Diglet"]

while True:
    selector = int(input("Que pokemon hay en este habitat? 1.Bosque, 2.Cueva "))

    if selector == 1:
        print("En el bosque viven los siguientes Pokemon: ")
        for pokemon in bosque:
            print(f"-{pokemon}")
    elif selector == 2:
        print("En las cuevas viven los siguientes Pokemon: ")
        for pokemon in cueva:
            print(f"-{pokemon}")
    else:
        print("Opcion invalida, intenta nuevamente.")
    
    seguir = input("Quieres consultar otro habitat? s/n: ").lower()
    if seguir != "s":
        print("Hasta la proxima!")
        break 