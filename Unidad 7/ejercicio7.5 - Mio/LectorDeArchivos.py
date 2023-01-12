#https://decodigo.com/python-verificar-si-existen-archivos-y-carpetas

import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°

class lector_de_archivos:
    def leer_archivo(self):
        print()
        self.existe_archivo()
        
        fichero = open(path_archivo, 'r')
        print(fichero.read())
        fichero.close()
        
    #--------------- ---------------
    def contar_comas(self):
        print()
        self.existe_archivo()
        fichero = open(path_archivo, 'r')

        cont = 0  
        caracter = fichero.readline(1)
        while caracter != "":
            if (caracter == ","):
                cont+=1
            caracter = fichero.readline(1)
            
        fichero.close()
        print(f"El texto tiene {cont} comas")

    #--------------- ---------------
    def contar_palabras(self):
        self.existe_archivo()
        fichero = open(path_archivo, 'r')
        palabras = fichero.read()
        lista_palabras = palabras.split()
        print(f"\n{lista_palabras}")
        print(f"El archivo tiene {len(lista_palabras)} palabras")
        fichero.close()

    #--------------- ---------------
    def quitar_palabras(self):
        self.existe_archivo()
        fichero = open(path_archivo, 'r')
        palabras = fichero.read()
        lista_palabras = palabras.split()
        
        palabra_eliminar = input("\nIngrese la palabra a eliminar: ")
        existe_palabra = False

        for i in lista_palabras:
            if(i != palabra_eliminar):
                print(i)
            else:
                existe_palabra = True
        
        if(not existe_palabra):
            print("\nEsa palabra NO existe en el archivo.")

        fichero.close()
        pass

    #--------------- Función para ver si existe un archivo antes de abrirlo ---------------
    def existe_archivo(self):
        path = os.path.abspath(os.path.dirname(__file__))
        archivo = "archivo.txt"
        global path_archivo
        path_archivo = path + "\\" + archivo

        if (not os.path.isfile(path_archivo)):
            #El archivo NO existe -> lo creo
            #print("El archivo NO existe")
            fichero = open(path_archivo, 'w')
            fichero.close()