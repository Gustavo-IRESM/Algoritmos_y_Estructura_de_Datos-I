
'''
Ejercicio 5.6 (Programa de Inventario de verduleria)
Crear un prgrama que debe:
+ Contar con un stock de frutas y otro de verduras
+ El stock indica si venden o no esa fruta o verdura, no la cantidad) - dos listas que inician vacias
+   Contar con un menu y 3 funciones
     1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
     2. Consultar el stock de frutas o verduras
     3. Eliminar un elemento del stock
'''
#-------------- Agregar frutas o verduras --------------
def agregar_mercaderia():
    while True:
        print("\nAgregar mercadería", end="")
        tipo = tipo_mercaderia()
        if(tipo == "0"):    #Salgo del menú
            return

        mercaderia = nombre_mercaderia()
        existe = existe_mercaderia(mercaderia)
        if(existe == NO_EXISTE):
            #No existe esa mercadería
            if(tipo == FRUTA):
                frutas.append(mercaderia)   #Agrego la fruta a la lista
            elif(tipo == VERDURA):
                verduras.append(mercaderia) #Agrego la verdura a la lista
        else:
            #Existe esa mercadería
            print("Ya existe esa mercaderia.")

#-------------- Consultar stock --------------
def consultar_stock():
    print("\nConsultar stock", end="")
    tipo = tipo_mercaderia()
    if(tipo == 0):    #Salgo del menú
        return

    if(tipo == FRUTA):
        print("\nFruta disponible")     #Muestro el stock de frutas
        print(frutas)
    else:
        print("\nVerdura disponible")   #Muestro el stock de verduras
        print(verduras)

#-------------- Eliminar frutas o verduras --------------
def eliminar_mercaderia():
    print("\nEliminar mercadería", end="")

    mercaderia = nombre_mercaderia()
    if(mercaderia == 0):    #Salgo del menú
        return

    existe = existe_mercaderia(mercaderia)
    if(existe == FRUTA):
        frutas.remove(mercaderia)   #Elimino la fruta de la lista
    elif(existe == VERDURA):
        verduras.remove(mercaderia) #Elimino la verdura de la lista
    elif(existe == NO_EXISTE):
        print("No existe esa mercadería")

#-------------- Pregunto si es fruta o verdura --------------
def tipo_mercaderia():
    while True:
        tipo = input('''
        1 - Fruta
        2 - Verdura
        0 - Salir
        Indique si es fruta o verdura: ''')
        
        if(tipo == "0" or tipo == FRUTA or tipo == VERDURA):
            break
        else:
            print("Opción incorrecta.")
    
    return tipo

#-------------- Controlo si ya existe esa mercadería --------------
def existe_mercaderia(nombre_mercaderia):
    if(nombre_mercaderia in frutas):
        return FRUTA        #Existe y es una fruta
    elif(nombre_mercaderia in verduras):
        return VERDURA      #Existe y es una verdura
    else:
        return NO_EXISTE    #No existe

#-------------- Ingreso nombre de la mercadería --------------
def nombre_mercaderia():
    while True:
        nombre = input("\nIngrese nombre de la mercadería: ")
        if(nombre == "0" or nombre.isalpha()):  #El 0 es para salir del menú
            return nombre
        else:
            print("\nAtención: el nombre de la merdacería no puede contener números ni espacios.")

#------------------------------------------------
#-              Programa principal              -
#------------------------------------------------
frutas = []
verduras = []
NO_EXISTE = "0"   #La uso como constante para indicar que "0" = NO_EXISTE. Uso string para evitar el casteo
FRUTA = "1"       #La uso como constante para indicar que "1" = FRUTA. Uso string para evitar el casteo
VERDURA = "2"     #La uso como constante para indicar que "2" = VERDURA. Uso string para evitar el casteo

while True:
    opcion = input('''
    MENÚ
    ----
    1 - Agregar fruta o verdura
    2 - Consultar el stock
    3 - Eliminar un elemento
    0 - Salir
    Seleccione una opción: ''')

    if(opcion == "1"):
        agregar_mercaderia()
    elif(opcion == "2"):
        consultar_stock()
    elif(opcion == "3"):
        eliminar_mercaderia()
    elif(opcion == "0"):
        break