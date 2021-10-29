import listados as list
import varios

#-------------- Vendo un producto --------------
def vender(productos):
    while True:
        print("\nVenta de productos.")
        
        #Muestro el listado de productos
        list.consultar_stock(productos)
        
        #Llamo a la función para ingresar y validar el código del producto
        indice_prod = varios.cod_producto(productos)
        
        if(indice_prod == -1):
            #Salgo
            return productos
        
        elif(indice_prod >= 0):
            #El producto existe. Lo vendo si hay stock
            if(productos[3][indice_prod] > 0):
                
                #Hay stock, lo vendo y descuento stock
                productos[3][indice_prod] -= 1
                precio_venta = productos[2][indice_prod]
                
                #Calculo el precio de venta según la forma de pago
                precio_venta *= (1 + forma_pago() / 100)
                print(f"Precio de venta $ {precio_venta}")
            else:
                #No hay stock. No lo puedo vender
                print("No hay stock.")
        
        elif(indice_prod == -2):
            #El producto NO existe
            pass

#-------------- Indico forma de pago --------------
def forma_pago():
    while True:
        opcion = input('''
        Medios de pago
        --------------
        1 - TC
        2 - TD
        3 - Efectivo
        Seleccione un medio de pago: ''')

        if(opcion == "1"):      #TC
            return 10
        elif(opcion == "2"):    #TD
            return 0
        elif(opcion == "3"):    #Efectivo
            return -10
        else:
            print("Opción inválida.")
