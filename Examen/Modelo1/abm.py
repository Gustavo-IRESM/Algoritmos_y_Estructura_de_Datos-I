import variables_globales as vg

#-------------- Agregar frutas o verduras --------------
def agregar_mercaderia():
    while True:
        print("\nAgregar mercadería", end="")
        tipo = tipo_mercaderia()
        if(tipo == "0"):    #Salgo del menú
            return

        mercaderia = nombre_mercaderia()
        existe = existe_mercaderia(mercaderia)
        if(existe == vg.NO_EXISTE):
            #No existe esa mercadería
            if(tipo == vg.FRUTA):
                vg.frutas.append(mercaderia)   #Agrego la fruta a la lista
            elif(tipo == vg.VERDURA):
                vg.verduras.append(mercaderia) #Agrego la verdura a la lista
        else:
            #Existe esa mercadería
            print("Ya existe esa mercaderia.")

#-------------- Eliminar frutas o verduras --------------
def eliminar_mercaderia():
    print("\nEliminar mercadería", end="")

    mercaderia = nombre_mercaderia()
    if(mercaderia == 0):    #Salgo del menú
        return

    existe = existe_mercaderia(mercaderia)
    if(existe == vg.FRUTA):
        vg.frutas.remove(mercaderia)   #Elimino la fruta de la lista
    elif(existe == vg.VERDURA):
        vg.verduras.remove(mercaderia) #Elimino la verdura de la lista
    elif(existe == vg.NO_EXISTE):
        print("No existe esa mercadería")


#-------------- Pregunto si es fruta o verdura --------------
def tipo_mercaderia():
    while True:
        tipo = input('''
        1 - Fruta
        2 - Verdura
        0 - Salir
        Indique si es fruta o verdura: ''')
        
        if(tipo == "0" or tipo == vg.FRUTA or tipo == vg.VERDURA):
            break
        else:
            print("Opción incorrecta.")
    
    return tipo

#-------------- Controlo si ya existe esa mercadería --------------
def existe_mercaderia(nombre_mercaderia):
    if(nombre_mercaderia in vg.frutas):
        return vg.FRUTA        #Existe y es una fruta
    elif(nombre_mercaderia in vg.verduras):
        return vg.VERDURA      #Existe y es una verdura
    else:
        return vg.NO_EXISTE    #No existe

#-------------- Ingreso nombre de la mercadería --------------
def nombre_mercaderia():
    while True:
        nombre = input("\nIngrese nombre de la mercadería: ")
        if(nombre == "0" or nombre.isalpha()):  #El 0 es para salir del menú
            return nombre
        else:
            print("\nAtención: el nombre de la merdacería no puede contener números ni espacios.")
