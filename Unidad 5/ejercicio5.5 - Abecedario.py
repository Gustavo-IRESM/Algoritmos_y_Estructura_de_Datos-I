'''
**Ejercicio 5.5**
Crear una funcion que debe:
+    Tener almacenado el abcedario en una lista
+    Pedir al usuario un numero (2 o 3) - VERIFICAR 
+    Elimina de la lista las letras que ocupen posiciones múltiplos de ese numero
+   Mostrar por pantalla la lista resultante.
+   No deben aparecer y se deben tener en cuenta todos los posibles errores
'''

def eliminar_letras(abc, numero):
    lista_resultante = []
    for i in range (len(abc)):
        #Si no es múltiplo del número indicado, se agrega a la lista resultante
        if((i+1)%numero != 0):
            lista_resultante.append(abc[i]) # Si es múltiplo de 2 = a c e g i k m ñ p r t v x z
                                            # Si es múltiplo de 3 = a b d e g h j k m n o p r s u v x y
    print(lista_resultante)


######################################
#         PROGRAMA PRINCIPAL         #
######################################
abecedario = list("abcdefghijklmnñopqrstuvwxyz")
while True:
    try:
        multiplo = int(input("\nIndique el número múltiplo (2 o 3): "))
        if(multiplo == 2 or multiplo == 3):
            eliminar_letras(abecedario, multiplo)
        else:
            print(f"El número {multiplo} no está dentro de las opciones.")
    except:
        print("Error, debe ingresar un número.")

