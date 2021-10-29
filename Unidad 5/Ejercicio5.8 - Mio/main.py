'''
##**Ejercicio 5.8 (Programa de ventas)**
El programa debe:
*   Simular un programa que venda 3 productos
Codigo      Nombre     Precio Stock
    1     & producto1  & 300   & 5
    2     & producto2  & 400   & 4
    3     & producto3  & 500   & 7

*   El menu debe mostrar los productos a comprar. ->LISTO
*   Luego se debe contar con un menu de si se pagara en efectivo o tarjeta credito o debito -> LISTO
*   Contar con 7 funciones disponibles en el menu:
  1.  Ver menu de productos (Formato: codigo - producto) ->LISTO
  2.  Pagar con tarjeta credito (Se debe cobrar 10% mas y se debe descontar el stock) -> LISTO
  3.  Pagar con tarjeta debito (se debe descontar el stock)
  4.  Pagar con efectivo (Se debe cobrar 10% menos y se debe descontar el stock)
  5.  Consultar productos y stock
  6.  Agregar stock a los productos
  7.  Cambiar el precio a los productos
  
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

base_productos = [[1,2,3],["producto1","producto2","producto3"],[300,400,500],[5,4,7]]

#------------------------------------------------
#-              Programa principal              -
#------------------------------------------------

import listados as list
import ventas
import abm

while True:
    
    opcion = input('''
    MENÚ
    ----
    1 - Menú de productos
    2 - Vender un producto
    3 - Consultar productos y stock
    4 - Agregar stock
    5 - Cambiar precios
    0 - Salir
    Seleccione una opción: ''')

    if(opcion == "1"):
        list.menu_productos(base_productos)
    elif(opcion == "2"):
        ventas.vender(base_productos)
    elif(opcion == "3"):
        list.consultar_stock(base_productos)
    elif(opcion == "4"):
        abm.agregar_stock(base_productos)
    elif(opcion == "5"):
        abm.cambiar_precio(base_productos)
    elif(opcion == "0"):
        break
    else:
        print("Opción inválida.")

