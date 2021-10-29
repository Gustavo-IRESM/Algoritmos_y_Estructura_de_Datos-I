import Pelicula as pl
import auxiliar as aux

lista_peliculas = [] #empieza vacia

class GestorDePeliculas:
    def __init__(self):
        pass

#---------- Cargo el género de la película ----------
    def genero(self):
        while True:
            opcion = input("""
Menú género
-----------
    1 - Acción
    2 - Policial
    3 - Thriller
    4 - Suspenso
    5 - Romántica
    6 - Comedia
    7 - Documental
    Seleccione una opción: """)

            if opcion == "1":
                return "Acción"
            elif opcion == "2":
                return "Policial"
            elif opcion == "3":
                return "Thriller"
            elif opcion == "4":
                return "Suspenso"
            elif opcion == "5":
                return "Romántica"
            elif opcion == "6":
                return "Comedia"
            elif opcion == "7":
                return "Documental"

    #---------- Cargo una película ----------
    def crear_peliculas(self):
        lista_peliculas.append(pl.Pelicula("Rambo 3",1986,"Acción","USA",9))
        lista_peliculas.append(pl.Pelicula("Duro de matar",1996,"policial","Argentina",10))
        lista_peliculas.append(pl.Pelicula("Viaje a las estrellas",1995,"Thriller","Canadiense",6))
        lista_peliculas.append(pl.Pelicula("Tiburón",2012,"Documental","España",7))
        
        '''
        while True:
            nombre = input("\nIngrese el nombre de la pelicula: ").capitalize()
            if(self.existe_pelicula(nombre)):
                #La película existe
                print("Esta pelicula ya existe.")
                return
        
            año = aux.ingresar_numero_entero("Ingrese el año de la película (debe estar entre 1970-2021): ")
            if (año >= 1970 and año <= 2021):
                break
            else:
                print("Año no válido.")
        
        genero = self.genero()
        nacionalidad = input("Ingrese la nacionalidad: ").capitalize()
        while True:
            puntuacion = aux.ingresar_numero_entero("Ingrese la puntuación de la película (debe estar entre 1-10): ")
            if (puntuacion >= 1 and puntuacion <= 10):
                break
            else:
                print("Puntuación no válida.")
        
        lista_peliculas.append(pl.Pelicula(nombre,año,genero,nacionalidad,puntuacion))
        return
        '''

    #---------- Imprimo la lista de un año ----------
    #def listar_peliculas(self, año=0):
    def listar_peliculas(self, año):
        año = aux.ingresar_numero_entero("\nIngrese el año de la película (debe estar entre 1970-2021)\n0 para listar todas las películas: ")
        print("\nListado de películas:")
        print("---------------------")
        for peliculas in lista_peliculas:
            #Imprimo películas de un determinado año
            if(año == peliculas.año):
                print(peliculas.nombre)
            #Imprimo TODAS las películas
            elif(año == 0):
                print(peliculas.nombre)


    #---------- Verifico si la película existe ----------
    def existe_pelicula(self,nombre_pelicula = ""):
        while True:
            if (nombre_pelicula == ""):
                nombre_pelicula = input("\nIngrese el nombre de la pelicula: ").capitalize()

            for peliculas in lista_peliculas:
                if(nombre_pelicula == peliculas.nombre):
                    #----- Existe -----
                    return peliculas

            #----- NO existe -----
            print("Esa pelicula NO existe.")
            return False

    #---------- Imprimos los datos de una película ----------
    def mostrar_datos_pelicula(self):
        pelicula = self.existe_pelicula()
        
        #Si la película existe muestro los datos
        if(pelicula):
            print(f"""
            Datos de la película:
            ---------------------
            Nombre: {pelicula.nombre}
            Año: {pelicula.año}
            Género: {pelicula.genero}
            Nacionalidad: {pelicula.nacionalidad}
            Puntuación: {pelicula.puntuacion}
            """)
        
        #Ademas de mostrar los datos, presento la película
        pelicula.presentar_pelicula()

        return pelicula

    #---------- Cambiar género de una película ----------
    def cambiar_genero(self):
        pelicula = self.mostrar_datos_pelicula()
        print("Seleccione el nuevo género de la película")
        
        # Podría hacer estp ? Ventajas y desventajas ?
        #pelicula.genero = self.genero()
        
        nuevo_genero = self.genero()
        pelicula.cambiar_genero(nuevo_genero)

    #---------- Verificar año de una película ----------
    def verificar_año_pelicula(self):
        print("\nListado de películas:")
        print("---------------------")
        for pelicula in lista_peliculas:
            print (pelicula.nombre)
        
        while True:
            nombre_pelicula = self.existe_pelicula()
            if(nombre_pelicula):
                año = aux.ingresar_numero_entero("Ingrese el año estimado en que se filmó la película: ")
                nombre_pelicula.mayor_menor_igual(año)
                break

    #---------- Cambiar puntuación de una película ----------
    def modificar_puntuacion(self):
        pelicula = self.mostrar_datos_pelicula()
        
        nueva_puntuacion = aux.ingresar_numero_entero("Ingrese la nueva puntuación de la película: ")
        
        # Podría hacer estp ? Ventajas y desventajas ?
        pelicula.puntuacion = nueva_puntuacion
        
        #pelicula.cambiar_puntuacion(nueva_puntuacion)