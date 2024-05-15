import random

loops = 1

numbers = []

histories = {   1 : "En un día soleado, [person_name] decidió ir de excursión a [place]" +
                "Mientras caminaba, se encontró con un [animal] que parecía perdido." +
                "Decidió ayudarlo y juntos llegaron a la cima de la montaña. Allí, encontraron un antiguo [object] que parecía tener poderes mágicos." +
                "De repente, el [animal] habló y le pidió a [person_name] que usara el [object] para salvar su hogar de la destrucción. Sin dudarlo, [person_name] aceptó el desafío y junto con el [animal], emprendió una misión para proteger su tierra.",

                2 : "En el corazón del [place], [person_name] descubrió un bosque encantado donde " +
                "los árboles susurraban secretos y los [animal] parloteaban entre sí." +
                "Guiado por la curiosidad, [person_name] encontró un misterioso [object] que brillaba con una luz mágica" +
                ". Al tocarlo, fue transportado a una dimensión paralela donde conoció a [person_name2], un guardián del bosque." +
                "Juntos, descubrieron el secreto oculto detrás del [object] y se unieron para proteger el bosque de las fuerzas oscuras que amenazaban con destruirlo.",
                
                3: "En un viaje de buceo a [place], [person_name] se encontró con un grupo de juguetones [animal] que lo llevaron a un antiguo naufragio." +
                "Allí, descubrió un antiguo [object] que parecía ser la clave de un antiguo tesoro perdido. Antes de que pudiera investigar más, [person_name2], un explorador submarino, apareció en escena." +
                "Juntos, se embarcaron en una emocionante búsqueda del tesoro, enfrentándose a peligrosas criaturas marinas y resolviendo enigmas antiguos.",

                4: "[person_name] recibió una invitación para pasar la noche en la misteriosa mansión de [place]. Al llegar, fue recibido por un inquietante [animal] que parecía ser el guardián de la casa." +
                "Mientras exploraba los oscuros pasillos, [person_name] encontró un antiguo [object] que desencadenó una serie de eventos extraños. " +
                "Pronto, se dio cuenta de que la mansión estaba embrujada y necesitaba la ayuda de [person_name2], un experto en lo paranormal, para desentrañar el misterio y liberar a los espíritus atrapados.",

                5 : "Un experimento científico en [place] salió mal y transportó a [person_name] y a un curioso [animal] a través del tiempo. Se encontraron en una era antigua donde descubrieron un enigmático [object] que parecía ser la clave para volver a casa." +
                "Mientras intentaban reparar el dispositivo, se toparon con [person_name2], un inventor brillante del pasado que les ofreció su ayuda." +
                "Juntos, trabajaron para resolver el enigma del [object] y regresar al presente antes de que fuera demasiado tarde."}

while(loops <= 5):
    person_name = input("Ingrese un nombre")
    action = input("Ingrese una Accion")
    place = input("Ingrese un lugar")
    animal = input("Ingrese un animal")
    object = input("Ingrese un objeto")
    action2 = input("Ingrese una accion")
    person_name2 = input("Ingrese un nombre")

    number = random.randint(1,5)
    if(numbers not in number):
        numbers = number
        history = histories[number]
        history.replace("[person_name]", person_name)

print(history)
    




