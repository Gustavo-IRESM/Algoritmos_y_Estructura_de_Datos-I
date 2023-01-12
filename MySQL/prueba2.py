import mysql.connector

conexion =mysql.connector.connect(host="localhost", user="root", password="", database="bd1")
cursor=conexion.cursor()
cursor.execute("show tables")
for tabla in cursor:
    print (tabla)
conexion.close()