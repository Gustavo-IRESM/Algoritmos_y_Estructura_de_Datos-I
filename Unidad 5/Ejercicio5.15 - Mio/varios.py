def menu_pelis_series():
    while True:
        opcion = input('''
        1 - Películas
        2 - Series
        0 - Salir
        Seleccione una opción: ''')
        if(opcion >= "0" and opcion <= "2"):
            return opcion
        else:
            print("Opcion incorrecta")