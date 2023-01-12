"""
#### **Ejercicio 7.4**
Crear una programa para leer el un archivo.csv.
Crear funciones para:
*   obtener los titulos de cada columna (1° Fila)
*   Contar la cantidad de columnas 
*   Contar la cantidad de filas """
import os

from posixpath import split
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
path_tabla = path + "\\tabla.csv"
print(f"\nPath: {path}\\archivo.txt \n")##\\ por caracteres especiales

def leer_titulos():
    try:
        tabla = open(path_tabla,'r')
        titulos = tabla.readline()
        lista_titulos = titulos.split(',')
        print("Los titulos son: ",end="")
        cont=0
        for i in lista_titulos:
            print(i,end="-")
            cont+=1
        print(f"La cantidad de columnas son: {cont}")
        tabla.close()
    except:
        print("error")

def contar_filas():
    try:
        tabla = open(path_tabla,'r')
        cont = 0
        while True:
            linea = tabla.readline()
            print(linea, end="")
            if (linea == ""):
                break
            cont+=1
        print(f"\nLa cantidad de filas son: {cont}")
        tabla.close()
    except:
        print("error")

contar_filas()      
leer_titulos()