

import GestorCompus as gc
import Auxiliar as aux

gestor = gc.GestorDeCompus()

while True:
    opcion = input(
    """
MENU PRINCIPAL
--------------
    1. Crear compu
    2. Listar compus
    3. Cambiar SO
    4. Listar periféricos
    0. Salir
    Seleccione una opción: """
    )
    if (opcion == "1"):  
        #Crear una compu.
        gestor.crear_compu()

    elif (opcion == "2"):
        #Listar compus.
        gestor.listar_compus()
           
    elif (opcion == "3"):
        #Cambiar SO
        gestor.cambiar_so()

    elif (opcion == "4"):
        #Listar periféricos
        gestor.listar_perifericos()
    
    elif (opcion == "0"):
        break
    
    else:
        print("Opción incorrecta.")

