import variables_globales as vg
import abm
#-------------- Consultar stock --------------
def consultar_stock():
    print("\nConsultar stock", end="")
    tipo = abm.tipo_mercaderia()
    if(tipo == 0):    #Salgo del menú
        return

    if(tipo == vg.FRUTA):
        print("\nFruta disponible")     #Muestro el stock de frutas
        print(vg.frutas)
    else:
        print("\nVerdura disponible")   #Muestro el stock de verduras
        print(vg.verduras)