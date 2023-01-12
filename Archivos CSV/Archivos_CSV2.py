#https://python-para-impacientes.blogspot.com/2015/05/operaciones-con-archivos-csv.html

import csv, operator
CONST_DELIMITADOR = ';'
#CONST_ARCHIVO_ENTRADA = 'Alumnos.csv'
CONST_ARCHIVO_ENTRADA = 'D:\Users\Administrador\Documents\Analista\1er año\Algoritmos y Estructura de Datos I\Archivos CSV\Matriculacion\inscriptos_LICENCIATURA_EN_COMUNICACION_SOCIAL_(2015).csv'
CONST_ARCHIVO_SALIDA = 'D:\Users\Administrador\Documents\Analista\1er año\Algoritmos y Estructura de Datos I\Archivos CSV\Matriculacion\Matricular.csv'


with open(CONST_ARCHIVO_ENTRADA) as csvarchivo:
    entrada = csv.DictReader(csvarchivo)

    csvsalida = open(CONST_ARCHIVO_SALIDA, 'w', newline='')
    salida = csv.writer(csvsalida, delimiter=CONST_DELIMITADOR, 
                        quotechar='', 
                        quoting=csv.QUOTE_NONE)
    
    for reg in entrada:
        print(reg['Materia'],reg['Año'],reg['Periodo'],reg['Turno'],reg['Division'],reg['Alumno'],reg['Nro de documento'],reg['Baja'],reg['Fecha Baja'])
        salida.writerow([reg['Materia'],reg['Año'],reg['Periodo'],reg['Turno'],reg['Division'],reg['Alumno'],reg['Nro de documento'],reg['Baja'],reg['Fecha Baja']])
        #if reg['provincia'] != 'Huelva':
            #salida.writerow([reg['nom'], reg['cons']])  # Escribir registro

del entrada, salida, reg
csvsalida.close()
del csvsalida