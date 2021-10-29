"""
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
+   Constructor debe incluir los atributos (patente,marca,año,origen)
-   Crear metodos para esta clase de:
    + 1.  Presentarse (patente,marca,año,origen)
    + 2.  Indicar tipos de vehiculo(Clases heredadas)
    - 3.  Metodos que luego modificarán las clases hijas. 
        - Acelerar
        - Retroceder
        + Obtener_velocidad_max
        + Setear_velocidad_max

Crear 3 clases que hereden de la clase padre Vehiculos, con un atributo en particular para cada una
1.   Particular
2.   PickUp
3.   Deportivo

Crear clase GestorAutos que cuente con las siguientes funciones para un menu
+ 1. Crear auto, indicando tipo de auto y guardar en una lista
+ 2. Listar autos (presentandolos), indicando tipo de Vehiculo.
+ 3. Cambiar velocidad de un Vehiculo
+ 4. Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
"""

#import Vehiculos as vh
import GestorAutos as ga
import Auxiliar as aux

gestor = ga.GestorDeAutos()

while True:
    opcion = input(
    """
Menu principal
--------------
Seleccione una opción:
    1. Crear auto
    2. Listar autos
    3. Cambiar velocidad
    4. Calcular tiempo de viaje
    0. Salir
    Opción: """
    )
    if (opcion == "1"):
        #Crear un auto.
        gestor.crear_auto()
        
    elif (opcion == "2"):
        #Listar autos.
        gestor.listar_autos()
           
    elif (opcion == "3"):
        #Cambiar velocidad
        gestor.cambiar_velocidad()

    elif (opcion == "4"):
        #Calcular tiempo de viaje
        gestor.calcular_tiempo()
    
    elif (opcion == "0"):
        break
    
    else:
        print("Opción incorrecta.")