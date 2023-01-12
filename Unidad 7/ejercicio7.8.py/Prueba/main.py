import os

fichero = "peliculas.txt"

path = os.path.abspath(os.path.dirname(__file__))
#path = os.path.abspath(os.path.dirname('__file__'))
#path = os.path.dirname(os.path.abspath("__file__"))

print(f"\n{path}\\{fichero}")

archivo = open(path + "\\" + fichero, 'r+')    #Abro el archivo y lo retorno como un objeto

#print(archivo.readline(3))
#print(archivo.readline())
if(("rambo 1" + "\n") == archivo.readline()):
    print("Anduvo")
else:
    print("NO anduvo")

#print(archivo.readline())
archivo.close()