'''
**Ejercicio 7.2**
Crear una funcion para leer el un archivo.txt.
*   pedir al usuario una palabra y encontrar la cantidad de veces que aparece esa palabra en el archivo
'''

import os
path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°

print(f"\nPath: {path}\\archivo.txt \n")##\\ por caracteres especiales

try:
    #fichero = open("d:\\python\\archivo.txt", "r")
    fichero = open(path + "\\archivo.txt", "r")

    palabras = fichero.read()
    print(palabras)
    lista_palabras = palabras.split()
    print(lista_palabras)
    palabra_a_contar = input("Ingrese la palabra a contar: ")
    
    contador = 0
    for i in lista_palabras:
        if i == palabra_a_contar:
            contador += 1
    print(f"La palabra {palabra_a_contar} está {contador} de veces en el texto")
except:
    print("\nNo existe el archivo")