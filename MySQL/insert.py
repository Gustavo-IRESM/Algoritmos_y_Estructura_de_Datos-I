import mysql.connector

conexion=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="bd1")
cursor=conexion.cursor()
sql="insert into articulos(descripcion, precio) values (%s,%s)"
datos=("naranjas", 23.50)
cursor.execute(sql, datos)
datos=("peras", 34)
cursor.execute(sql, datos)
datos=("bananas", 25)
cursor.execute(sql, datos)
conexion.commit()
conexion.close()