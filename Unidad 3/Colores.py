try:
    color1 = input("Primer color: ")
    color2 = input("Segundo color: ")
    color1 = color1.upper()
    color2 = color2.upper()
    
    if(color1 == 'ROJO'):
        if(color2 == 'AZUL'):
            print("Morado")
        else:   #Elegimos verde
            print("Amarillo")
    else:
        if(color2 == 'VERDE'):
            print("Cyan")
        else:
            print("Morado")
except:
    print("Se produjo un error")