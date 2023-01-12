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
