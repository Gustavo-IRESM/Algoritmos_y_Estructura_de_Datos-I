def ingresar_numero_entero(mensaje, min, max):
    while True:
        try:
            numero = int(input(f"\n{mensaje}"))
            #print(f"Mi número de legajo es {self.legajo}. Me llamo {self.nombre} {self.apellido}", end=". ")
            if ((numero >= min) and (numero <= max)):
                return numero
            else:
                print(f"\nEl valor debe estar entre {min} y {max}")
        except:
            print("\nDebe ingresar un número válido.")


def ingresar_numero_float(mensaje, min, max):
    while True:
        try:
            numero = float(input("f\n{mensaje}"))
            if ((numero >= min) and (numero <= max)):
                return numero
            else:
                print(f"\nl valor debe estar entre {min} y {max}")
        except:
            print("\nDebe ingresar un número válido.")