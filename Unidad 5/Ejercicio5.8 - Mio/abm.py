import listados as list
import varios

#-------------- Agregar stock --------------
def agregar_stock(productos):
    while True:
        print("\nAgregar stock:")
        
        #Muestro el listado de productos
        list.consultar_stock(productos)
        
        #Llamo a la función para ingresar y validar el código del producto
        indice_prod = varios.cod_producto(productos)
        
        if(indice_prod == -1):
            #Salgo
            return productos
        
        elif(indice_prod >= 0):
            #El producto existe. Modifico el stock
            while True:
                try:
                    stock = int(input("Ingrese la cantidad a sumar al stock: "))
                    if(stock > 0):
                        #El stock ingresado es válido. Lo cambio
                        productos[3][indice_prod] += stock
                        break
                    else:
                        #El precio ingresado es negativo.
                        print("El stock a ingresar debe ser mayor que cero")
                except:
                    #El precio ingresado NO es válido.
                    print("El stock ingresado no es válido.")
        
        elif(indice_prod == -2):
            #El producto NO existe
            pass
            

#-------------- Cambiar precio --------------
def cambiar_precio(productos):
    while True:
        print("\nCambiar precio:")
        
        #Muestro el listado de productos
        list.consultar_stock(productos)
        
        #Llamo a la función para ingresar y validar el código del producto
        indice_prod = varios.cod_producto(productos)
        
        if(indice_prod == -1):
            #Salgo
            return productos
        
        elif(indice_prod >= 0):
            #El producto existe. Modifico el precio
            while True:
                try:
                    precio = float(input("Ingrese el precio nuevo: "))
                    if(precio > 0):
                        #El precio ingresado es válido. Lo cambio
                        productos[2][indice_prod] = precio
                        break
                    else:
                        #El precio ingresado es negativo.
                        print("El precio debe ser mayor que cero")
                except:
                    #El precio ingresado NO es válido.
                    print("El precio ingresado no es válido.")
        
        elif(indice_prod == -2):
            #El producto NO existe
            pass
