"""
#### **Ejercicio 7.7**
- Crear una programa con cuatro opciones:
    + 1.  Crear un archivo en blanco, con el nombre que desee el usuario
    - 2.  Escribir datos en el archivo sin pisar los existentes
    - 3.  Borrar los datos del archivo
    - 4.  Leer linea a linea el archivo ( YA LO HICIMOS)
"""
import archivo as ar

while True:
    opcion = input(
    """
-----------Menu principal-----------
Seleccione una opcion:
    1.  Crear un archivo
    2.  Escribir datos
    3.  Borrar los datos del archivo
    4.  Leer Archivo
    5.  Salir
    Opcion: """
    )
    if (opcion=="1"):
        ar.crear_archivo()

    elif (opcion=="2"):
        ar.pedir_palabras()

    elif (opcion=="3"):
        ar.borrar_archivo()

    elif (opcion=="4"):
        ar.leer_fichero()

    elif (opcion=="5"):
        break
    else:
        print("\nNinguna opcion correcta.")