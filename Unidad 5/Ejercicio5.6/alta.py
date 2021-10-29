import varios
#-------------- Agregar frutas o verduras --------------
def agregar_mercaderia():
    global frutas[]
    global verduras[]
    
    while True:
        print("\nAgregar mercadería", end="")
        tipo = varios.tipo_mercaderia()
        if(tipo == "0"):
            return

        mercaderia = input("\nNombre de la mercadería: ")
        if(tipo == "1"):
            if(mercaderia not in frutas):
                frutas.append(mercaderia)
            else:
                print("Ya existe esa mercaderia.")
        else:
            if(mercaderia not in verduras):
                verduras.append(mercaderia)
            else:
                print("Ya existe esa mercaderia.")