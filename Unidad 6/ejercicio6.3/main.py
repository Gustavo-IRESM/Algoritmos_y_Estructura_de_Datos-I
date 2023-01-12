"""
###**Ejercicio 6.3**
Crear una clase de Peliculas:
+   Cuyo constructutor debe inicializar los atributos nombre, año, genero, nacionalidad, puntuacion
+   Se deben crear 4 metodos en la clase:
    + 1.  Presentar la pelicula: La pelicula {nombre} de {genero} del {año} obtuvo una puntuacion de {puntuacion}  
        y fue filmada en {nacionalidad}
    + 2. Retornar si el año de la pelicula es mayor o igual o menor al pasado por parametro
    + 3. Cambiar el genero de una pelicula
    + 4. Modificar puntuacion de la pelicula

El programa debe: gestorDePeliculas
-   Tener un menu con 7 opciones:
    + 1. Crear una pelicula y guardar su nombre (instancia) en una lista de peliculas.
    + 2. Verificar si la pelicula deseada existe en la lista de peliculas.
    + 3. Pedir a la lista de peliculas, todas las de un año.
    + 4. Presentar una pelicula de la lista
    + 5. Cambiar el genero de una pelicula
    + 6. Verificar el año de la pelicula
    + 7  Modificar puntuacion de la pelicula (entre 1 y 10)
    """
#import Pelicula as pl
import gestorDePeliculas as gp
import auxiliar as aux

gestor = gp.GestorDePeliculas() #Unicamente ara hacer uso de las funciones del gestor

while True:
    opcion = input(
    """
-----------Menu principal-----------
Por favor seleccione una opción:
    1. Crear pelicula
    2. Verificar si existe una pelicula
    3. Imprimir películas según año
    4. Mostrar datos de una pelicula
    5. Cambiar el género de una pelicula
    6. Verificar el año de la pelicula
    7  Modificar puntuacion de la pelicula
    0. Salir
    Opción: """
    )
    if (opcion == "1"):
        #Crear una pelicula y guardar su nombre (instancia) en una lista de peliculas.
        gestor.crear_peliculas()
        #aux.__spec__

    elif (opcion == "2"):
        #Verificar si la pelicula deseada existe en la lista de peliculas.
        existe_pelicula = gestor.existe_pelicula()
        if(existe_pelicula):
            print("Esa pelicula EXISTE.")
           
    elif (opcion == "3"):
        #Pedir a la lista de peliculas, todas las de un año.
        gestor.listar_peliculas()

    elif (opcion == "4"):
        #Presentar una pelicula de la lista
        gestor.mostrar_datos_pelicula()
    
    elif (opcion == "5"):
        #Cambiar el genero de una pelicula
        gestor.cambiar_genero()

    elif (opcion == "6"):
        #Verificar el año de la pelicula
        gestor.verificar_año_pelicula()
    
    elif (opcion == "7"):
        #Modificar puntuacion de la pelicula (entre 1 y 10)
        gestor.modificar_puntuacion()
    
    elif (opcion == "0"):
        break
    
    else:
        print("Opción incorrecta.")

