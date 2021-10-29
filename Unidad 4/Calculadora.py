def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

while True:
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            break
        except:
            print ("Número incorrecto.")
        
    operacion = input('''Menú:
        + Suma
        - Resta
        * Multiplicación
        / División
        0 Salir
        Operación a realizar:''')

    if(operacion == "+"):
        print(f"{num1} + {num2} = {suma(num1,num2)}")
    elif(operacion == "-"):
        print(f"{num1} - {num2} = {resta(num1,num2)}")
    elif(operacion == "*"):
        print(f"{num1} * {num2} = {multiplicacion(num1,num2)}")
    elif(operacion == "/"):
        if(num2 == 0):
            print("Error, no se puede dividir un número por 0")
        else:
            print(f"{num1} / {num2} = {division(num1,num2)}")
