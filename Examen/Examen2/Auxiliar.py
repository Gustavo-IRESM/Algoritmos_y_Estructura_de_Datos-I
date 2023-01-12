import os

#--------------- Función para ingresar un número int ---------------
def ingresar_numero_entero(mensaje, min, max):
    while True:
        try:
            numero = int(input(f"\n{mensaje}"))
            #El valor del número debe estar entre min y max
            if ((numero >= min) and (numero <= max)):
                return numero
            else:
                print(f"\nEl valor debe estar entre {min} y {max}")
        except:
            print("\nDebe ingresar un número válido.")

#--------------- Función para ingresar un número float ---------------
def ingresar_numero_float(mensaje, min, max):
    while True:
        try:
            numero = float(input("f\n{mensaje}"))
            #El valor del número debe estar entre min y max
            if ((numero >= min) and (numero <= max)):
                return numero
            else:
                print(f"\nEl valor debe estar entre {min} y {max}")
        except:
            print("\nDebe ingresar un número válido.")

#--------------- Función para ver si existe un archivo antes de abrirlo ---------------
def existe_archivo(path_archivo):
    if os.path.isfile(path_archivo):
        #print('\nEl archivo existe.\n')
        return True
    else:
        #print('\nEl no archivo existe.\n')
        return False