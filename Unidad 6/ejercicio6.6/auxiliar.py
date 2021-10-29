def ingresar_numero_entero(mensaje, min, max):
    while True:
        try:
            numero = int(input(mensaje))
            if ((numero >= min) and (numero <= max)):
                return numero
            else:
                print(f"El valor debe estar entre {min} y {max}")
        except:
            print("\nDebe ingresar un número válido.")


def ingresar_numero_float(mensaje, min, max):
    while True:
        try:
            numero = float(input(mensaje))
            if ((numero >= min) and (numero <= max)):
                return numero
            else:
                print(f"El valor debe estar entre {min} y {max}")
        except:
            print("\nDebe ingresar un número válido.")