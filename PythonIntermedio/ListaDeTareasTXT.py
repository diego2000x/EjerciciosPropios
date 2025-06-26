tareas = []
contador = 0
salir = False

try:
    with open("ListaTareas.txt","r") as archivo:
        tareas = archivo.read().splitlines()
except:
    pass

def agregarTarea():
    tarea = input("Ingrese la tarea: ")
    tareas.append(tarea)
    print("Tarea guardada.\n")

def verTareas():
    global contador
    print("Tareas guardadas: ")
    for tarea in tareas:
        contador += 1
        print(f"{contador}. {tarea}")
    print("")
    contador = 0

def borrarTarea(x):
    tareas.remove(x)
    print(f"Tarea {x} eliminada.\n")

def eliminarTarea():
    global contador
    print("Tareas guardadas: ")
    for tarea in tareas:
        contador += 1
        print(f"{contador}. {tarea}")
    print("")
    contador = 0
    borrar = input("Que tarea desea borrar?")
    borrarTarea(borrar)
    

def salir():
    global salir
    with open("ListaTareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea+ "\n")
    salir = True

def menu():
    print("Bienvenido, que quieres hacer?")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    selector= int(input("=>"))
    if selector == 1:
        agregarTarea()
    elif selector == 2:
        verTareas()
    elif selector == 3:
        eliminarTarea()
    elif selector == 4:
        salir()
    else:
        print("Intente nuevamente.")

while True:
    menu()
    if salir == True:
        print("Hasta luego!")
        break