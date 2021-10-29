import baja
import alta

'''
##**Ejercicio 5.6 (Programa de Inventario de verduleria)**
Crear un prgrama que debe:
*   Contar con un stock de frutas y otro de verduras (El stock indica si venden o no esa fruta o verdura, no la cantidad) - dos 
    listas que inician vacias
*   Contar con un menu y 3 funciones
     1. Agregar frutas o verduras al correspondiente stock (verificando que que sean nuevas)
     2. Consultar el stock de frutas o verduras
     3. Eliminar un elemento del stock
'''

#-------------- Consultar stock --------------
def consultar_stock():
    tipo = tipo_mercaderia()
    if(tipo == 0):
        return

    if(tipo == "1"):
        print("\nFruta disponible")
        print(frutas)
    else:
        print("\nVerdura disponible")
        print(verduras)


#------------------------------------------------
#-              Programa principal              -
#------------------------------------------------
frutas = []
verduras = []
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
        alta.agregar_mercaderia()
    elif(opcion == "2"):
        consultar_stock()
    elif(opcion == "3"):
        baja.eliminar_mercaderia()
    elif(opcion == "0"):
        break