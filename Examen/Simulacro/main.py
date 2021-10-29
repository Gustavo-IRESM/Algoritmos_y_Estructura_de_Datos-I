
import variables_globales as vg
import abm
import listados as list


#------------------------------------------------
#-              Programa principal              -
#------------------------------------------------

abm.agregar_mercaderia()
#list.consultar_stock()
#abm.eliminar_mercaderia()

while True:
    break
    opcion = input('''
    MENÚ
    ----
    1 - Agregar fruta o verdura
    2 - Consultar el stock
    3 - Eliminar un elemento
    0 - Salir
    Seleccione una opción: ''')

    if(opcion == "1"):
        abm.agregar_mercaderia()
    elif(opcion == "2"):
        list.consultar_stock()
    elif(opcion == "3"):
        abm.eliminar_mercaderia()
    elif(opcion == "0"):
        break