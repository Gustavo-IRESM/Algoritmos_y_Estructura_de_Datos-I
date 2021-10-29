class Pelicula:
    #constructor
    def __init__(self,nombre,año,genero,nacionalidad,puntuacion):
        self.nombre = nombre #unico
        self.año = año
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.puntuacion = puntuacion

    #---------- Presento la película pasada por parámetro ----------
    def presentar_pelicula(self):
        print(f"La pelicula {self.nombre} de {self.genero} del {self.año} obtuvo una puntuacion de {self.puntuacion} y fue filmada en {self.nacionalidad}")

    #---------- Retornar si el año de la pelicula es mayor, igual o menor al pasado por parametro----------
    def mayor_menor_igual(self,año_comparar):

        if (self.año > año_comparar):
            print("El año de la pelicula es mayor.")
        elif (self.año == año_comparar):
            print("El año de la pelicula es igual.")
        else:
            print("El año de la pelicula es menor.")

    #---------- Cambiar género de una película ----------
    def cambiar_genero(self,nuevo_genero):
        self.genero = nuevo_genero
        print(f"\nEl nuevo genero de la pelicula es {self.genero}")

    #---------- Cambiar puntuación de una película ----------
    def cambiar_puntuacion(self,nueva_puntuacion):
        self.puntuacion = nueva_puntuacion
        print(f"La nueva puntuacion de la pelicula es {self.puntuacion}")