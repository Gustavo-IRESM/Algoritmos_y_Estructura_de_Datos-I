#-------------- Valido el código del producto --------------
def cod_producto(productos):
    while True:
        try:
            cod_prod = int(input("\nCódigo del producto (0 para salir): "))
            
            if(cod_prod < 0):
                #El código es negativo
                print("Código incorrecto.")
            
            elif(cod_prod == 0):
                #Se ingresó 0 para salir del menú
                #Retorno -1 porque el 0 corresponde al primer elemento de la lista
                return -1
            
            else:
                #Se ingresó un código de producto válido. Lo busco
                if(cod_prod in productos[0]):
                    indice = productos[0].index(cod_prod)
                    #El producto EXISTE. Retorno el índice del producto en el listado
                    return indice
                else:
                    print("El producto no existe.")
                    #El producto NO existe. Retorno -1
                    return -2
        except:
            print("El código del producto sólo puede contener números.")