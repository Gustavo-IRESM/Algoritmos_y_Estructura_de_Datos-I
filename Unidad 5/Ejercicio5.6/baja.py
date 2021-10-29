#-------------- Eliminar frutas o verduras --------------
def eliminar_mercaderia():
    tipo = tipo_mercaderia()
    if(tipo == 0):
        return

    mercaderia = input("Ingrese nombre de la mercadería: ")
    if(tipo == "1"):
        if(mercaderia in frutas):
            frutas.remove(mercaderia)
        else:
            print("No existe esa mercadería")
    else:
        if(mercaderia in frutas):
            verduras.remove(mercaderia)
        else:
            print("No existe esa mercadería")