import os

archivo = "prueba.txt"

while True:
    pelicula = input("\nNombre de la pelicula a cargar: ")
    path = os.path.abspath(os.path.dirname(__file__))

    fichero = open(path + "\\" + archivo, 'r+')

    fichero.write(pelicula  + "\n")

    print(fichero.read())

    fichero.close()
