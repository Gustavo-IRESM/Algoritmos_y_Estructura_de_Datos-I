'''
https://www.generacodice.com/es/articolo/870513/Parse+a+CSV+file+using+python+(to+make+a+decision+tree+later)+%5Bclosed%5D
https://stackoverflow.com/questions/3305926/python-csv-string-to-array
https://stackoverflow.com/questions/29178844/how-to-parse-a-string-using-a-csv-parser-in-python
https://docs.python.org/3/library/stdtypes.html#str.split
https://pybonacci.org/2020/06/01/trabajando-con-ficheros-csv-usando-el-modulo-csv-de-python/
https://www.analyticslane.com/2018/06/15/guardar-y-leer-archivos-csv-con-python/
https://python-para-impacientes.blogspot.com/2015/05/operaciones-con-archivos-csv.html
'''
with open("Alumnos.csv","r") as file:
    for line in file:
         #print(line.split(",")[13])
         if (line.split(",")[11] != "S"):
             apellido = line.split(",")[7].replace('"','')
             nombre = line.split(",")[8].replace('"','').lstrip()

             print(line.split(",")[1].replace('"',''),  #Materia
             line.split(",")[2],                        #Año
             line.split(",")[3],                        #Período
             line.split(",")[4],                        #Turno
             line.split(",")[5],                        #División
             #line.split(",")[6],                       #Legajo
             apellido + ",",
             nombre,
             #line.split(",")[9],                       #Palabra DNI
             line.split(",")[10])                       #DNI
