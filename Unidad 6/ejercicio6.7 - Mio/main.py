"""
+ Simular un programa de gestion de animales de un zoologico, que cuente con dos clases Animales y Empleados
+ La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento, encargado_cuidar (LEGAJO de objeto empleado))
+ Crear 3 clases que hereden de animal segun su sector del zoologico)
    + Animales en jaulas.
    + Animales sueltos.
    + Animales en el agua

+ La Clase Empleados tiene los atributos (legajo, nombre, apellido, lista_animales_a_cuidar(clase animal))
	+ Un empleado puede cuidar animales de diferentes sectores

+ Contar con 6 funciones disponibles en el menu. Estas funciones deben estar incluidas en una clase llamada GestorZoologico:
	+ Crear instancias de animales (se puede elegir entre los tres sectores) y guardarlos en una lista. 
		+ Los animales al crearlos en el sistema tienen q contar si o si con un encargado.
		+ Chequear por nombre si el animal ya existe
	+ Crear instancia de Empleados y guardarlos en una lista (Los empleados se les pueden asignar animales luego)
	- Asignar a un empleado un animal a cuidar
	+ Cambiar de encargado un animal
	+ Imprmir lista de animales (con toda su información)
	+ Imprimir lista de Empleados (con toda su información)

+ Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
+ Gestionar posibles errores
+ Estructurar el programa a criterio propio
"""


import GestorZoo as gz
import Auxiliar as aux

gestor = gz.GestorZoologico()

while True:
    opcion = input(
    """
MENU PRINCIPAL
--------------
    1. Crear animal
    2. Crear empleado
    3. Asignar animal a un empleado
    4. Cambiar de encargado a un animal
    5. Imprimir lista de animales
    6. Imprimir lista de empleados
    0. Salir
    Seleccione una opción: """
    )
    if (opcion == "1"):
        #Crear animal
        gestor.crear_animal()

    elif (opcion == "2"):
        #Crear empleado
        gestor.crear_empleado()
           
    elif (opcion == "3"):
        #Asignar animal a un empleado
        gestor.asignar_cuidador()
        pass

    elif (opcion == "4"):
        #Cambiar de encargado a un animal
        gestor.cambiar_cuidador()
        pass
    
    elif (opcion == "5"):
        #Imprimir lista de animales
        gestor.imprimir_animales()

    elif (opcion == "6"):
        #Imprimir lista de empleados
        gestor.imprimir_empleados()

    elif (opcion == "0"):
        break
    
    else:
        print("Opción incorrecta.")
