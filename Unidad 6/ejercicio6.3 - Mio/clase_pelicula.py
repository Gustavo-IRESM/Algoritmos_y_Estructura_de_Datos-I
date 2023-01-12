class Peliculas:
    def __init__(self, nombre, año, genero, nacionalidad, puntuacion):
        self.nombre = nombre
        self.año = año
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.puntuacion = puntuacion

    #-------------- Mostrar datos de una película --------------
    def presentar_pelicula(self):
        print(f"""La pelicula {self.nombre}, del año {self.año}, de nacionalidad {self.nacionalidad} es del genero {self.genero} y tiene una puntuación de {self.puntuacion}""")
    
    #-------------- Chequear año de la peliícula --------------
    def chequear_año(self,año):
        if(self.año > año):
            print("El año de la película es mayor")
            return
        elif(self.año == año):
            print("El año de la película es el mismo")
            return
        elif(self.año < año):
            print("El año de la película es menor")
            return
    
    #-------------- Cambio de género --------------
    def cambiar_genero(self,genero_nuevo):
        print(f"cambie de genero {self.genero} al genero {genero_nuevo}")
        self.genero = genero_nuevo

    #-------------- Cambiar puntuación --------------
    def cambiar_puntuacion(self,nueva_puntuacion):
        self.puntuacion = nueva_puntuacion
        print(f"La nueva puntuacion de la pelicula es {self.puntuacion}")
