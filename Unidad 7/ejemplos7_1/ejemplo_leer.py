import os

#path actual
absFilePath = os.path.abspath(__file__)
path, filename = os.path.split(absFilePath)
print(f"\nPath: {path}\n")##\\ por caracteres especiales

# Metodo read()
print("\n***** MÉTODO read() *****")

try:
    fichero = open(path+"\\archivo.txt", 'r')
    print(fichero.read())
    fichero.close()
except:
    print("\nNo existe el archivo")

# Metodo readline()
print("\n***** MÉTODO readline() *****")
try:
    fichero = open(path+"\\archivo.txt", 'r')
    linea = fichero.readline()
    while  linea != "":
        print(linea,end="")
        linea = fichero.readline()
    fichero.close()
    print("\n")
except:
    print("\nNo existe el archivo")