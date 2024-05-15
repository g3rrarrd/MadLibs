
__file__ = "historias.txt"

histories = {
    1: "En un dia soleado, [person_name] decidio ir de excursion a [place]" +
       "Mientras caminaba, se encontro con un [animal] que parecia perdido." +
       "Decidio ayudarlo y juntos llegaron a la cima de la montana. Alli, encontraron un antiguo [object] que parecia tener poderes magicos." +
       "De repente, el [animal] hablo y le pidio a [person_name] que usara el [object] para salvar su hogar de la destruccion. Sin dudarlo, [person_name] acepto el desafio y junto con el [animal], emprendio una mision para proteger su tierra.",

    2: "En el corazon del [place], [person_name] descubrio un bosque encantado donde " +
       "los arboles susurraban secretos y los [animal] parloteaban entre si." +
       "Guiado por la curiosidad, [person_name] encontro un misterioso [object] que brillaba con una luz magica" +
       ". Al tocarlo, fue transportado a una dimension paralela donde conocio a [person_name2], un guardian del bosque." +
       "Juntos, descubrieron el secreto oculto detras del [object] y se unieron para proteger el bosque de las fuerzas oscuras que amenazaban con destruirlo.",

    3: "En un viaje de buceo a [place], [person_name] se encontro con un grupo de juguetones [animal] que lo llevaron a un antiguo naufragio." +
       "Alli, descubrio un antiguo [object] que parecia ser la clave de un antiguo tesoro perdido. Antes de que pudiera investigar mas, [person_name2], un explorador submarino, aparecio en escena." +
       "Juntos, se embarcaron en una emocionante busqueda del tesoro, enfrentandose a peligrosas criaturas marinas y resolviendo enigmas antiguos.",

    4: "[person_name] recibio una invitacion para pasar la noche en la misteriosa mansion de [place]. Al llegar, fue recibido por un inquietante [animal] que parecia ser el guardia de la casa." +
       "Mientras exploraba los oscuros pasillos, [person_name] encontro un antiguo [object] que desencadeno una serie de eventos extranos. " +
       "Pronto, se dio cuenta de que la mansion estaba embrujada y necesitaba la ayuda de [person_name2], un experto en lo paranormal, para desentranar el misterio y liberar a los espiritus atrapados.",

    5: "Un experimento cientifico en [place] salio mal y transporto a [person_name] y a un curioso [animal] a traves del tiempo. Se encontraron en una era antigua donde descubrieron un enigmatico [object] que parecia ser la clave para volver a casa." +
       "Mientras intentaban reparar el dispositivo, se toparon con [person_name2], un inventor brillante del pasado que les ofrecio su ayuda." +
       "Juntos, trabajaron para resolver el enigma del [object] y regresar al presente antes de que fuera demasiado tarde.",

    6: "En un remoto pueblo de [place], [person_name] se topo con una leyenda olvidada. Cuentan que un [animal] mitico protege un tesoro ancestral escondido en las profundidades de un antiguo templo." +
       "Decidido a desenterrar la verdad detras de la leyenda, [person_name] se aventuro en la selva junto con [person_name2], un arqueologo experto en civilizaciones antiguas." +
       "Descubrieron los secretos del templo y se enfrentaron a peligros mortales, pero al final, la verdad los sorprendio.",

    7: "En una expedicion a [place], [person_name] se encontró con un [animal] salvaje que lo guió a través de un laberinto natural." +
       "En el corazón del laberinto, encontraron un [object] antiguo que emanaba un extraño resplandor." +
       "Intrigados por su hallazgo, [person_name] y el [animal] decidieron llevar el objeto a [person_name2], un experto en reliquias antiguas." +
       "Pronto descubrieron que el [object] tenía poderes inimaginables que los envolvieron en una aventura que desafió los límites del tiempo y el espacio."
}


def validation():
    try:
        file = open(__file__, 'r')
        file.read()

        return True
    except FileNotFoundError:

        file = open(__file__, 'w')

        for key in histories.keys():
            file.write(histories.get(key))
            file.write("\n")

        file.close()
        
        return False


def write_history():
    print("La historia puede tener dos acciones, dos personajes, un animal, un lugar y un objeto, ")
    print("para personas debe ser [person_name] o [person_name2], acciones [action] o [action2], objetos [object],")
    print("lugar [place] y animal [animal]")

    print()
    print("Escriba su historia")
    write_history = input()

    validation()

    file = open(__file__, 'a')
    file.write(write_history)
    file.write("\n")

    file.close

def read_histories():
   
   read_histories = {}

   with open(__file__, 'r') as file:
    number = 1
    for line in file.readlines():
        read_histories[number] = line
        number += 1

    file.close()

    return read_histories  

def histories():
    with open(__file__, 'r') as file:
        for line in file.readlines():
            print(line)      
    file.close()