import csv, operator
'''
with open("Alumnos.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        print(row)
'''


# Leer el archivo 'datos.csv' con reader() y 
# realizar algunas operaciones básicas: 

csvarchivo = open('Alumnos.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
reg = next(entrada)  # Leer registro (lista)
print(reg)  # Mostrar registro

for row in entrada:
    print(row)

#Carrera, Materia, Año = next(entrada)  # Leer campos
#print(Carrera, Materia, Año)  # Mostrar campos

#del Carrera, Materia, Año, entrada  # Borrar objetos
csvarchivo.close()  # Cerrar archivo
del csvarchivo  # Borrar objeto