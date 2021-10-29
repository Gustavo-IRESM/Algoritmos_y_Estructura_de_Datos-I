def ingresar_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except:
            print("\nDebe ingresar un número válido.")


def ingresar_numero_float(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except:
            print("\nDebe ingresar un número válido.")