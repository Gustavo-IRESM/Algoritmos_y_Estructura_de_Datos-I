'''
El programa debe:
+ Pedir al usuario cantidad de personas
+ Pedir al usuario una a una la edad de las personas
+ Finalizado la carga de las edades debe imprimir por pantalla la edad mayor
+ no deben generar errores
'''
while True:
    try:
        while True:
            cantPersonas = int(input("Ingrese la cantidad de personas: "))
            if(cantPersonas <= 0):
                print("La cantidad de personas no puede ser cero ni menor que cero")
            else:
                break

        edadMayor = 0
        for i in range(cantPersonas):
            while True:
                edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
                if(edad <= 0):
                    print("La edad no puede ser cero ni menor que cero")
                else:
                    break

            if(edad > edadMayor):
                edadMayor = edad

        print(f"La edad mayor es {edadMayor}.")
        break

    except:
        print("El valor ingresado no es correcto.")
