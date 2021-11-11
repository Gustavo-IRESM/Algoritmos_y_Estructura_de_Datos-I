#fichero = open("d:\Users\Administrador\Documents\Analista\1er año\Algoritmos y Estructura de Datos I\Unidad 7\ejemplo.txt","r")
#print(fichero.read())
#fichero.close()

#import os
#print(path+"\\ejemplo.txt")##\\ por caracteres especiales
#absFilePath = os.path.abspath(__doc__)
#path, filename = os.path.split(absFilePath)
#print(path+"\\ejemplo.txt")##\\ por caracteres especiales


import os
#path actual
#path = os.path.abspath(os.path.dirname(__file__))#probar este 1°
#path = os.path.abspath(os.path.dirname('__file__'))#probar este 2°
#path = os.path.dirname(os.path.abspath("__file__"))#probar este 3°
path_archivo = path+"\\archivo.txt"
print(f"\nEl path es: {path}\\archivo.txt\n")##\\ por caracteres especiales
