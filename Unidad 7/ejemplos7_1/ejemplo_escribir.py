import os

#path actual
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
print(f"\nPath: {path}\n")##\\ por caracteres especiales

try:
    fichero = open(path+"\\archivo2.txt", 'w')
    fichero.write("Contenido a escribir por Gustavo")
    fichero.close()
except:
    print("\nNo existe el archivo")