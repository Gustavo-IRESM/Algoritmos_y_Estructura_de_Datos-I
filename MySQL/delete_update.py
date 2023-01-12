import mysql.connector

conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")
cursor=conexion.cursor()
cursor.execute("delete from articulos where codigo=1")
cursor.execute("update articulos set precio=50 where codigo=3")
conexion.commit()
cursor.execute("select codigo, descripcion, precio from articulos")
for fila in cursor:
    print(fila)
conexion.close()