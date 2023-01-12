import os


#------------------------------
def abrir_archivo(archivo):
    path = os.path.abspath(os.path.dirname(__file__))

    #print(f"\nPath: {path}\\archivo.txt \n")
    try:
        fichero = open(path + "\\" + archivo,"r")
        fichero.close()
        return True

    except:
        return False

#------------------------------
def abrir_archivo1(archivo):
    path = os.path.abspath(os.path.dirname(__file__))
    #if os.path.isfile(path + '\\' + archivo):
    if os.path.isfile(archivo):
        #print('El archivo existe.');
        return True
    else:
        #print('El no archivo existe.');
        return False


#------------------------------
#archivo_existe = abrir_archivo("archivo.txt")
archivo_existe = abrir_archivo1("archivo.txt")

if(archivo_existe):
    print("El archivo existe")
else:
    print("El archivo NO existe")