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
import funciones_imprimir as fi
import variables as vr

base_productos = [[1,2,3],["producto1","producto2","producto3"],[300,400,500],[5,4,7]]

def forma_pago():
  while True:
    forma_pago = input("""Por favor ingrese su forma de pago:
      1. Credito
      2. Debito
      3. Efectivo
      Opcion: """)
    if forma_pago =="1":
      return "credito"
    elif forma_pago =="2":
      return "debito"
    elif forma_pago =="3":
      return "efectivo"
    else:
      print("Opcion incorrecta")

def pago_con_credito():
  #fi.imprimir_codigo_producto(base_productos)
  print(f"--------------PAGO CON CREDITO--------------")
  while True:
    print(f"Que producto desea vender:")
    for i in range(len(base_productos[1])):
      print(f"{base_productos[0][i]}  {base_productos[1][i]}")
    producto=input("--> ")
    if producto =="1":
      if(base_productos[3][0]>0):
        base_productos[3][0] = base_productos[3][0]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][0]*1.1}")
        return
      else:
        print("no hay stock")
    elif producto =="2":
      if(base_productos[3][1]>0):
        base_productos[3][1] = base_productos[3][1]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][1]*1.1}")
        return
      else:
        print("no hay stock")
    elif producto =="3":
      if(base_productos[3][2]>0):
        base_productos[3][2] = base_productos[3][2]-1 #resto stock
        print(f"El comprador debe pagar: {base_productos[2][2]*1.1}")
        return
      else:
        print("no hay stock")
    else:
      print("Opcion incorrecta")


fi.imprimir_matriz2(base_productos)
#fi.imprimir_codigo_producto(base_productos)
#forma_pago()
pago_con_credito()
fi.imprimir_matriz2(base_productos)

