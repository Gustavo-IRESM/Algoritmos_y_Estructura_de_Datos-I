"""##**Ejercicio 5.7 (Estadisiticas)**
El programa debe:
*   Simular un programa que calcule estadisticas
*   Pedir al usuario una serie de numeros enteros el 1 al 10 (verificar) y guardarlos en una lista, 
hasta que el usuario ingrese "fin"
*   Luego mostrar un menu con 4 opciones
  1.  Calcular promedio
  2.  Verificar cuantos numeros son menores que el numero indicado por el usuario
  3.  Verificar cuantos numeros son mayores o igual que el numero indicado por el usuario
  4.  Verificar si un numero que desee el usuario esta en la lista
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio"""

def pedido_numeros():
    lista_numeros = []
    contador=1
    while True:
        entrada = input(f"ingrese el {contador}° numero (entre el 1 y 10) o fin: ")
        if entrada == "fin":
            break
        else:
            try:
                if int(entrada)>0 and int(entrada)<=10:
                    lista_numeros.append(int(entrada))
                    contador+=1
                else:
                    print("Dato incorrecto!")
            except:
                print("Dato incorrecto!")
    
    return lista_numeros

def promedios(lista_principal):
    suma_total = sum(lista_principal)
    total_numero = len(lista_principal)
    return round(suma_total/total_numero,2)

# Verifica cuantos numero de la lista son menores que el numero indicado por el usuario
def cant_numeros_menores(lista_principal):
    while True:
        try:
            numero_comparar = int(input("indique el numero a comparar"))
            break
        except:
            print("Por favor ingrese un numero")
    contador =0
    for i in lista_principal:
        if i < numero_comparar:
            contador+=1
    
    return contador

#Verificar si un numero que desee el usuario esta en la lista
def numero_en_lista(lista_principal):
    while True:
        try:
            numero_comparar = int(input("Indique el numero a buscar: "))
            break
        except:
            print("Dato Incorrecto!")
    
    if numero_comparar in lista_principal:
        contador=True
    else:
        contador=False
    
    return contador

lista_principal = pedido_numeros()
print(lista_principal)
print(f"El promedio de la lista es: {promedios(lista_principal)}")