"""
#### **Ejercicio 7.1**
Crear una funcion para leer el un archivo.txt hasta encontrar un punto.
"""
import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°

print(f"\nPath: {path}\\archivo.txt \n")##\\ por caracteres especiales

def imprimir_hasta_punto_while():
    try:
        fichero = open(path + "\\archivo.txt", 'r')
        while True:
            caracter = fichero.readline(1)
            print(caracter,end="")
            if(caracter=="."):
                break
        fichero.close()
    except:
        print("\nNo existe el archivo")

def imprimir_hasta_punto_for():
    try:
        fichero = open(path + "\\archivo.txt", 'r')
        for c in fichero.readline():
            print(c,end="")
            if(c=="."):
                break
        fichero.close()
    except:
        print("\nNo existe el archivo")

imprimir_hasta_punto_while()
print("\n")

imprimir_hasta_punto_for()
print("\n")