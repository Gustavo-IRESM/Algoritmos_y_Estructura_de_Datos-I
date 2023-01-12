'''
Crear la clase Vehículo que tiene los siguientes atributos:
    + marca
    + tipo de vehículo (moto, auto o camión),
    + tipo de combustible
    + velocidad máxima
    + kilometraje

Los métodos que debe implementar son:
    + Constructor
    + RealizarMantenimiento:
        + Para el caso de las motos el mantenimiento debe realizarse a los 20.000 kms
        + Para el caso de los autos el mantenimiento debe realizarse a los 60.000 kms
        + Para el caso de los camiones el mantenimiento debe realizarse a los 100.000 kms

Finalmente, se debe hacer un menú con una lista de vehículos que coleccione los 3 tipos de vehículos, con opciones de:
    + creación de vehículos
    + mostrar los datos de los vehículos
    + realizar el mantenimiento de los mismos.
'''

#--------------------------------------------------
#-               Programa principal               -
#--------------------------------------------------

#import vehiculos as veh
import funciones as func

while True:
    opcion = input(
    """
    M E N Ú
    -------
    1 - Cargar un vehículo
    2 - Mostrar vehículos
    3 - Realizar mantenimiento
    0 - Salir
    Seleccione una opción: """)

    #Cargar un vehículo
    if (opcion == "1"):
        func.cargar_vehiculo()

    # Mostrar los Vehiculos
    elif (opcion == "2"):
        #print("\nListado de vehículos:")
        func.listar_vehiculos()

    # Realizar mantenimiento a un Vehiculo
    elif (opcion == "3"):
        func.mantenimiento()

    elif (opcion == "0"):
        break
