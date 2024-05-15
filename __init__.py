from histories import validation, write_history, histories
from inputValues import play
from sys import exit

def case1():
    validation()
    print()
    play()

def case2():
    validation()
    print()
    write_history()

def case3():
    validation()
    print()
    histories()

def case4():
    print()
    print("Hasta pronto")
    exit()

options = {1: case1, 2: case2, 3: case3,4: case4}

def switch_case(case):
    return options.get(case, default_case)()

def default_case():
    print("Opción inválida")

if __name__ == "__main__":
    while True:
        print("¿Qué desea hacer?")
        print("1. Jugar")
        print("2. Escribir Historia")
        print("3. Ver historias")
        print("4. Salir")
        
        case = int(input())
        if case not in [1, 2, 3, 4]:
            print("Valor incorrecto, intente de nuevo.")
        else:
            switch_case(case)
