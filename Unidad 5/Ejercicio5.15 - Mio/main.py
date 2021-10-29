'''
El programa debe:

    + Simular una base de datos de peliculas y series con la capacidad de agregar, buscar, eliminar y filtrar peliculas y series.
    + Debe comenzar con las siguientes peliculas y series en un diccionario:
        base = {
            "peliculas" : ["El hombre araña", "Los vengadores" , "Los vengadores 2"],
            "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }
    + Contar con 5 funciones disponibles en el menu:
    + Mostrar por pantalla en formato vertical la lista de peliculas o series disponibles.
    + Agregar nuevas peliculas o series (que no esten) en la base.
    - Eliminar peliculas o series de la base.
    + Mostrar segun requiera el usuario la lista de peliculas desde un punto a otro (ej el usuario quiere ver de la 2° a la 4° una lista ).
    - Buscar peliculas o series que contengan una palabra requerida por el usuario. (ej. input("el"), se liste las peliculas que contengan la palabra "el").
'''

base_peliculas = {
    "peliculas" : ["el hombre araña", "los vengadores" , "los vengadores 2"],
    "series" : ["prision break", "la casa de papel" , "los simpsons"]
        }

#------------------------------------------------
#-              Programa principal              -
#------------------------------------------------

import abm
import buscar as bus
import listar as list
import varios

while True:
    opcion = input('''
    MENÚ
    ----
    1 - Listar películas o series
    2 - Agregar película o serie
    3 - Eliminar película o serie
    4 - Listar películas (desde/hasta)
    5 - Buscar películas o series
    0 - Salir
    Seleccione una opción: ''')

    if(opcion == "1"):
        list.listar_base(base_peliculas)
        #print(varios.menu_pelis_series())
    
    elif(opcion == "2"):
        base_peliculas = abm.agregar(base_peliculas)
    
    elif(opcion == "3"):
        pass
    
    elif(opcion == "4"):
        list.listar_algunas(base_peliculas)
    
    elif(opcion == "5"):
        bus.buscar_titulos(base_peliculas)

    elif(opcion == "0"):
        break
    
    else:
        print("Opción inválida.")