#-------------- Pregunto si es fruta o verdura --------------
def tipo_mercaderia():
    while True:
        tipo = input('''
        1 - Fruta
        2 - Verdura
        0 - Salir
        Indique si es fruta o verdura: ''')
        
        if(tipo == "0" or tipo == "1" or tipo == "2"):
            break
        else:
            print("Opción incorrecta.")
    
    return tipo