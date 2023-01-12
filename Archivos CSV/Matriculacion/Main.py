#https://python-para-impacientes.blogspot.com/2015/05/operaciones-con-archivos-csv.html

import os
import csv, operator

CONST_DELIMITADOR = ';'
#CONST_ARCHIVO_ENTRADA = 'Alumnos.csv'
CONST_ARCHIVO_SALIDA = 'Matricular.csv'

#--------------- Función para ver si existe un archivo antes de abrirlo ---------------
def existe_archivo(archivo_entrada):

    if (not os.path.isfile(archivo_entrada)):
        #El archivo NO existe -> lo creo
        
        #print("El archivo NO existe")
        #fichero = open(archivo_entrada, 'w')
        #fichero.close()
        
        return False
    else:
        #print(f"El archivo {archivo} existe")
        return True


#--------------- ---------------
def formatear_archivo(path, archivo_ent, archivo_sal):
    archivo_entrada = path + "\\" + archivo_ent
    if(not existe_archivo(archivo_entrada)):
        print("El archivo NO existe")
        return

    #archivo_salida = path + "\\" + CONST_ARCHIVO_SALIDA
    archivo_salida = path + "\\" + archivo_sal

    with open(archivo_entrada) as csvarchivo:
        entrada = csv.DictReader(csvarchivo)

        csvsalida = open(archivo_salida, 'w', newline='')
        salida = csv.writer(csvsalida, delimiter=CONST_DELIMITADOR, 
                            quotechar='', 
                            quoting=csv.QUOTE_NONE)
        
        for reg in entrada:
            if(reg['Baja']=="S"):
                print(reg['Materia'],reg['Año'],reg['Periodo'],reg['Turno'],reg['Division'],reg['Alumno'],reg['Nro de documento'],reg['Baja'],reg['Fecha Baja'])
            else:
                salida.writerow([reg['Materia'],reg['Año'],reg['Periodo'],reg['Turno'],reg['Division'],reg['Alumno'],reg['Nro de documento'],reg['Baja'],reg['Fecha Baja']])

    del entrada, salida, reg
    csvsalida.close()
    del csvsalida

#--------------- Programa principal ---------------
path = os.path.abspath(os.path.dirname(__file__))

formatear_archivo(path, "inscriptos_TECNICATURA_SUPERIOR_EN_PERIODISMO.csv", "Matricular_TSP.csv")
formatear_archivo(path, "inscriptos_LICENCIATURA_EN_COMUNICACION_SOCIAL_(2015).csv", "Matricular_LIC.csv")
formatear_archivo(path, "inscriptos_TECNICATURA_SUPERIOR_EN_LOCUCIÓN.csv", "Matricular_TSL.csv")





#--------------- ---------------
'''def formatear_archivo():
    archivo = open(path_archivo, 'r')
    pelicula = archivo.readline()
    print()

    while(pelicula != ""):
        print(pelicula, end="")
        pelicula = archivo.readline()
        
    archivo.close()'''