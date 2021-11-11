'''
Ejercicio 7.5
- Crear una clase para leer archivos (lectorDeArchivos).
- Crear funciones para:
    - Leer el archivo e imprimir todo su contenido
    - Encontrar la cantidad de comas en el archivo.
    - Contar la cantidad de palabras de 3 letras y guardarlas en un lista
    - Especificar una palabra a quitar e imprimir el contenido sin esta palabra
'''

import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°

print(f"\nPath: {path}\\archivo.txt \n")##\\ por caracteres especiales


class LectorDeArchivos:
    def leer_archivo(self):
        archivo = input("Ingrese el archivo a leer (con su formato):")
        path_archivo = path + "\\tabla.csv"
        path_archivo = path + "\\" + archivo
        try:
            fichero = open(path_archivo,'r')
            print(fichero.read())
            fichero.close()
        except:
            print("\nNo existe el archivo")

lector = LectorDeArchivos()
lector.leer_archivo()
