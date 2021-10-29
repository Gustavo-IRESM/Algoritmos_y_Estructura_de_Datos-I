import variables as vr

def imprimir_matriz(matriz):
      
  print(f"C - Producto - Pr - Stock")
  for i in range(len(matriz)-1):
    print(f"{matriz[0][i]} - {matriz[1][i]} - {matriz[2][i]} - {matriz[3][i]}")

def imprimir_matriz2(matriz):
  print(f"--------------PRODUCTOS--------------")
  print(f"C \t PRODUCTO \t Pr$ \tStock")
  for i in range(len(matriz)-1):
    if i !=0:
      print("")
    for j in range(len(matriz)):
      print(f"{matriz[j][i]}",end='\t')
  print("") 

def imprimir_codigo_producto(matriz):
  print(f"--------------PRODUCTOS--------------")
  print(f"C \t PRODUCTO")
  for i in range(len(matriz)-1):
    if i !=0:
      print("")
    for j in range(2):
      print(f"{matriz[j][i]}",end='\t')
  print("") 
