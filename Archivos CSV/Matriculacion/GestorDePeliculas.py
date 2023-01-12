#https://programacion.net/articulo/escribir_y_leer_ficheros_en_python_1446

import os

class Gestor_Peliculas:
    def __init__(self):
        pass

    #--------------- ---------------
    def cargar_pelicula(self):
        self.existe_archivo()
        
        nueva_pelicula = input("\nIngrese el nombre de la nueva película: ").capitalize()

        if(self.existe_pelicula(nueva_pelicula)):
            print("\nEsa película ya existe en la BD.")
        else:
            archivo = open(path_archivo, 'a')
            archivo.write(nueva_pelicula + "\n")
            #archivo.write(nueva_pelicula)
            archivo.close()
       
    #--------------- ---------------
    def listar_peliculas(self):
        self.existe_archivo()
        
        archivo = open(path_archivo, 'r')
        pelicula = archivo.readline()
        print()

        while(pelicula != ""):
            print(pelicula)
            pelicula = archivo.readline()
            
        archivo.close()

    #--------------- ---------------
    def buscar_pelicula(self):
        nombre_pelicula = input("\nIngrese el nombre de la película a buscar: ").capitalize()
    
        if(self.existe_pelicula(nombre_pelicula)):
            print("\nEsa película ya existe en la BD.")
        else:
            print("\nEsa película NO existe en la BD.")

    #--------------- ---------------
    def existe_pelicula(self, nombre_pelicula):
        self.existe_archivo()

        archivo = open(path_archivo, 'r')
        existe_pelicula = False
        pelicula = archivo.readline()

        while(pelicula != ""):
            if(pelicula == (nombre_pelicula + "\n")):
                existe_pelicula = True
                break
            pelicula = archivo.readline()
        
        archivo.close()
        
        if(existe_pelicula):
            return True
        else:
            return False

    
    #--------------- Función para ver si existe un archivo antes de abrirlo ---------------
    def existe_archivo(self):
        path = os.path.abspath(os.path.dirname(__file__))
        archivo = "inscriptos_TECNICATURA_SUPERIOR_EN_PERIODISMO.csv"
        global path_archivo
        path_archivo = path + "\\" + archivo

        if (not os.path.isfile(path_archivo)):
            #El archivo NO existe -> lo creo
            #print("El archivo NO existe")
            fichero = open(path_archivo, 'w')
            fichero.close()
