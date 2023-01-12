#from Examen.Simulacro2.Libros import Libro
import Libros as li
import os
import Auxiliar as aux

lista_libros = []

class Gestor_Biblio:
    def __init__(self):
        pass

    #--------------- ---------------
    def crear_libro(self):
        
        '''
        lista_libros.append(li.Libro(1,"Nombre","Autor","No alquilado"))
        lista_libros.append(li.Libro_Niños(2, "Libro 2", "Autor 2","No alquilado",11))
        lista_libros.append(li.Libro_Idiomas(3, "Libro 3", "Autor 3","No alquilado","Español"))    
        '''
        
        if(len(lista_libros) == 0):
            #Si es el primer libro, el ID es 1
            Id = 1
        else:
            #Obtengo el último ID y le sumo 1
            Id = lista_libros[-1].Id + 1
        
        while True:
            nombre_libro = input("\nNombre del libro: ")
            if(nombre_libro != ""):
                break
        
        while True:
            autor = input("Nombre del autor: ")
            if(autor != ""):
                break
        
        while True:
            tipo_libro = input("""
        TIPO DE LIBRO:
        --------------
        1. Libro genérico
        2. Libro para niños
        3. Libro de idiomas
        Seleccione una opción: """)
            
            if(tipo_libro == "1"):
                lista_libros.append(li.Libro(Id, nombre_libro, autor))
                
                break
            elif(tipo_libro == "2"):
                lista_libros.append(li.Libro_Niños(Id=Id, nombre=nombre_libro, autor=autor))
                break
            elif(tipo_libro == "3"):
                idioma = self.seleccionar_idioma()
                lista_libros.append(li.Libro_Idiomas(Id=Id, nombre=nombre_libro, autor=autor, idioma_libro=idioma))
                break
            else:
                print("\nTipo de libro no válido.")
        
        #Grabo en archivo el libro creado
        self.loguear_libro(Id, nombre_libro, autor)

    #--------------- ---------------
    def listar_libros(self):
        #Imprimo la lista de libros
        print("\n")
        for libro in lista_libros:
            libro.presentarse()

    #--------------- ---------------
    def alquilar_libro(self):
        #Marco libro como alquilado
        libro = self.buscar_libro()
        libro.alquilar()

    #--------------- ---------------
    def devolver_libro(self):
        #Marco libro como devuelto
        libro = self.buscar_libro()
        libro.devolver()

    #--------------- ---------------
    def loguear_libro(self, Id, libro, autor):
        #Obtengo el path del archivo
        path = os.path.abspath(os.path.dirname(__file__))
        path_archivo = path + "\\libros.txt"
        
        try:
            #Grabo ID, nombre del libro y autor
            fichero = open(path_archivo, 'a')
            fichero.write(str(Id) + "-" + libro + "-" + autor + "\n")
            fichero.close()
        except:
            print("\nError con el archivo")

    #--------------- ---------------
    def seleccionar_idioma(self):
        idiomas = {
        "IN":"Ingles", 
        "AL": "Aleman",
        "CH": "Chino"
        }
        
        print("""
        IDIOMAS
        -------""")
        
        #Imprimo los idiomas disponibles
        for i in idiomas:
            print(f"\t{i}")

        opcion = input("Seleccione una opción: ").upper()
        
        #Obtengo del diccionario el idioma del libro
        idioma = idiomas.get(opcion,"Español")

        return idioma

    #--------------- ---------------
    def buscar_libro(self):
        print("""
    LIBROS DISPONIBLES
    ------------------""")

        #Imprimo la lista de libros para poder ver y seleccionar el ID correspondiente
        self.listar_libros()
        
        id_libro = aux.ingresar_numero_entero("Seleccione el ID del libro: ", 1, len(lista_libros))

        #El ID del libro si o si existe porque la función ingresar_numero_entero sólo me permite
        #ingresar números enteros dentro del rango de los IDs existentes
        for libro in lista_libros:
            if(id_libro == libro.Id):
                return libro
        