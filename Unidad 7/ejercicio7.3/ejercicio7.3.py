'''
**Ejercicio 7.3**
Crear una funcion para leer el un archivo.txt.

Crear funciones para:
*   Contar la cantidad de letrar que tiene el archivo (letras no espacios ni puntos)
*   Contar la cantidad de palabras que tiene el archivo
'''

import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°

print(f"\nPath: {path}\\archivo.txt \n")##\\ por caracteres especiales

#------------------------------
def contar_letras_gustavo():
    try:
        fichero = open(path + "\\archivo.txt","r")
        cant_letras = 0
        letra = fichero.readline(1)

        while (letra !=""):
            letra = fichero.readline(1)
            
            if((letra >= "a" and letra <= "z") or (letra >= "A" and letra <= "Z")):
                cant_letras += 1

        fichero.close()
        print(f"La cantidad de letras es {cant_letras}")

    except:
        print("\nNo existe el archivo")

#------------------------------
def contar_letras():
    try:
        fichero = open(path + "\\archivo.txt","r")
        cant_letras = 0
        while True:
            letra = fichero.readline(1)
            if (letra == ""):
                break
            elif(letra != "." and letra != " "):
                cant_letras += 1
            
        fichero.close()
        print(f"La cant de letras son {cant_letras}")

    except:
        print("\nNo existe el archivo")

#------------------------------
contar_letras_gustavo()

contar_letras()