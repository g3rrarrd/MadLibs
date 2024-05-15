import random
from histories import read_histories

values = {}

def play():
    person_name = input("Ingrese un nombre: ")
    values["[person_name]"] = person_name
    action = input("Ingrese una Accion: ")
    values["[action]"] = action
    place = input("Ingrese un lugar: ")
    values["[place]"] = place
    animal = input("Ingrese un animal: ")
    values["[animal]"] = animal
    object = input("Ingrese un objeto: ")
    values["[object]"] = object
    action2 = input("Ingrese una accion: ")
    values["[action2]"] = action2
    person_name2 = input("Ingrese un nombre: ")
    values["[person_name2]"] = person_name2

    histories = read_histories()

    number = random.randint(1,len(histories))
    history = histories[number]
    for key in values.keys():
        history = history.replace(key, values.get(key))
        
    print()
    print(history)


    




