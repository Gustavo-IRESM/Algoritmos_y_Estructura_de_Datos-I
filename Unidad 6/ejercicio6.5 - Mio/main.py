'''
Ejercicio 6.5
Crear una clase padre Computadoras:
    + Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO)
    + Crear metodos para esta clase de:
        + 1. Presentarse (id_modelo,listaPerifericos,SO)
        + 2. Indicar tipo de Computadora (Clases heredadas)
        + 3. Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO

Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
    + 1. Escritorio
    + 2. Notebbok

Crear clase GestorComputadora que cuente con las siguientes funciones para un menu
    + 1. Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
    + 2. Listar Computadoras (presentandolos), indicando tipo.
    + 3. Cambiar SO de una Computadora, verificando una lista de SO disponibles
    - 4. Listar perifericos
'''

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

