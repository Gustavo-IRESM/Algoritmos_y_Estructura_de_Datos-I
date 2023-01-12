import os

#---------- ----------
def crear_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    global path_archivo
    path_archivo = os.path.abspath(os.path.dirname(__file__))#probar este 1°
    global archivo 
    archivo = path_archivo + f"\\{nombre_archivo}.txt"
    
    try:
        fichero = open(archivo, 'w')
        fichero.close()
    except:
        print("\nNo existe el archivo")

#---------- ----------
def escribir_en_archivo(palabra):
    try:
        fichero = open(archivo,'a')
        fichero.write(palabra+"\n")
        fichero.close()
    except:
        print("\nNo existe el archivo")

#---------- ----------
def borrar_archivo():
    try:
        fichero = open(archivo, 'w')
        #fichero.read
        fichero.close()
    except:
        print("\nNo existe el archivo")

#---------- ----------
def pedir_palabras():
    while True:
        palabra = input("Ingrese una palabra: (exit->para salir) ")
        if(palabra =="exit"):
            break
        else:
            escribir_en_archivo(palabra)

#---------- ----------
def leer_fichero():
    try:
        fichero = open(archivo,'r')
        while True:
            linea = fichero.readline()
            if (linea == ""):
                break
            print(linea,end="")
        fichero.close()
    except:
        print("\nNo existe el archivo")