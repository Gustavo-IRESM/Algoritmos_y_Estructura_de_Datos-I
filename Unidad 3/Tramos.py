'''
El programa debe:
+ Pedir al usuario una cantidad de tramos de un viaje
+ Pedir al usuario la duración en minutos de cada tramo
+ Calcular el tiempo total de viaje
+ No deben generar errores
'''
while True:
    try:
        cantTramos = int(input("Ingrese la cantidad de tramos: ") or 0)
        duracion = 0

        for i in range(cantTramos):
            duracion += int(input(f"Ingrese la duración del tramo {i+1}: ") or 0)

        print(f"El tiempo total del viaje son {duracion} minutos.")
        break

    except:
        print("Debe ingresar un número.")
