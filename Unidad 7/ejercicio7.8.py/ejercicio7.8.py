'''
Ejercicio 7.8
- Crear una programa que cuente con 3 opciones:
 + Guardar en un archivo csv nombres de peliculas, verificando su existencia
 + Leer la base pelicula a pelicula
 + Leer las peliculas que cuenten con una palabra
'''

import GestorDePeliculas as gdp

gestor = gdp.Gestor_Peliculas()

while True:
    opcion = input(
    """
    MENU PRINCIPAL
    --------------
    1. Cargar película
    2. Listar películas
    3. Buscar película
    0. Salir
    Seleccione una opcion: """
    )
    if (opcion=="1"):
        gestor.cargar_pelicula()

    elif (opcion=="2"):
        gestor.listar_peliculas()

    elif (opcion=="3"):
        gestor.buscar_pelicula()

    elif (opcion=="0"):
        break
    else:
        print("\Opción correcta.")

