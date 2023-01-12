import mysql.connector

conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")
cursor=conexion.cursor()
cursor.execute("select codigo, descripcion, precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()