"""#### **Ejercicio 7.5 (FALTA)**
Crear una clase para leer archivos (lectorDeArchivos).

Crear funciones para:
    + Leer el archivo e imprimir todo su contenido
    + Encontrar la cantidad de comas en el archivo.
    + Contar la cantidad de palabras de 3 letras y guardarlas en un lista
    - Especificar una palabra a quitar e imprimir el contenido sin esta palabra"""

import LectorDeArchivos as lda

lector = lda.lector_de_archivos()

while True:
    opcion = input(
    """
    MENU PRINCIPAL
    --------------
    1. Leer e imprimir archivo
    2. Contar comas
    3. Contar palabras
    4. Quitar palabra
    0. Salir
    Seleccione una opcion: """
    )
    if (opcion=="1"):
        lector.leer_archivo()

    elif (opcion=="2"):
        lector.contar_comas()

    elif (opcion=="3"):
        lector.contar_palabras()

    elif (opcion=="4"):
        lector.quitar_palabras()

    elif (opcion=="0"):
        break
    else:
        print("\Opción correcta.")

