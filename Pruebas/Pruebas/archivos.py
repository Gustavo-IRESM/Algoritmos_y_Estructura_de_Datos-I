import os

def abrir_archivo(archivo):
    path = os.path.abspath(os.path.dirname(__file__))
    #if os.path.isfile(path + '\\' + archivo):
    if os.path.isfile(archivo):
        #print('El archivo existe.')
        return True
    else:
        #print('El no archivo existe.')
        return False


abrir_archivo("libros.txt")