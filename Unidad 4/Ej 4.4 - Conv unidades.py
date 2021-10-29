'''
El programa debe:
+   Contar con 4 funciones:
  +  Conversor de Grados Celcius a Fahrenheit(temperatura en °C).(buscar regla)
  +  Conversor de cm3 a litros (cantidad de cm3)
  +  Conversor de litros a cm3 (cantidad de litros)
  +  Pesos a Dolares (pesos)
-   Contar con un menu donde debe pedir al usuario que opcion realizar
-   Pedir los parametros y devolver el resultado al usuario
-   Gestionar posibles errores
'''

def celsius_fahrenheit(grados_celsius):
    print(grados_celsius, end=" ")
    if (grados_celsius == 1 ):
        print("grado Celsius equivale a", end=" ")
    else:
        print("grados Celsius equivalen a", end=" ")

    grados_fahrenheit = (grados_celsius * 9/5) + 32
    print(grados_fahrenheit, end=" ")
    if (grados_fahrenheit == 1 ):
        print("grado Fahrenheit")
    else:
        print("grados Fahrenheit")

#-------------------------------------

def cm3_litros(cm3):
    print(f"{cm3} cm3", end=" ")
    if(cm3 == 1):
        print("equivale a", end=" ")
    else:
        print("equivalen a", end=" ")

    litros = cm3 / 1000
    print(litros, end=" ")
    if(litros == 1):
        print("litro")
    else:
        print("litros")

#-------------------------------------

def litros_cm3(litros):
    print(litros, end=" ")
    if(litros == 1):
        print("litro equivale a", end=" ")
    else:
        print("litros equivalen a", end=" ")

    cm3 = litros * 1000
    print(f"{cm3} cm3")

#-------------------------------------

def pesos_dolares(pesos):
    while True:
        try:
            valor_dolar = float(input("Ingrese la cotización del dólar: "))
            if(valor_dolar < 0):
                print("La cotización del dólar no puede ser negativa")
            else:
                break
        except:
            print("Debe ingresar una cotización válida.")
  
    print(pesos, end=" ")
    if(pesos == 1):
        print("peso equivale a", end=" ")
    else:
        print("pesos equivalen a", end=" ")

    dolares = pesos / valor_dolar
    print(dolares, end=" ")
    if(dolares == 1):
        print("dólar")
    else:
        print("dólares")

#-------------------------------------

def ingresar_valor(unidad, opcion):
    while True:
        try:
            valor = float(input(f"Ingrese la cantidad de {unidad} a convertir: "))
            if (valor < 0 and opcion != "1"):
                print("No se permiten números negativos para esta conversión.")
            else:
                return valor                
        except:
            print("Debe ingresar un número.")
    
#-------------------------------------

while True:
    opcion = input('''
    Menú
    ----
        1 - Convertir de Grados Celcius a Fahrenheit
        2 - Convertir de cm3 a litros
        3 - Convertir de litros a cm3
        4 - Convertir de Pesos a Dolares
        0 - Salir
    Seleccione una opción: ''')

    if(opcion == "1"):
        celsius_fahrenheit(ingresar_valor("grados Celsius", opcion))
    elif(opcion == "2"):
        cm3_litros(ingresar_valor("cm3", opcion))
    elif(opcion == "3"):
        litros_cm3(ingresar_valor("litros", opcion))
    elif(opcion == "4"):
        pesos_dolares(ingresar_valor("pesos", opcion))
    elif(opcion == "0"):
        break

    print("\n-------------------------------------")
        