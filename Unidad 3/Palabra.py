'''
El programa debe:
+   Pedir al usuario una palabra
+   Verificar que sea una palabra y no un numero
+   Mostrar por pantalla las letras una a una
+   No producir errores
'''
while True:
    while True:
        palabra = input("Ingrese una palabra: ")
        if(palabra.isalpha()):
            break
        else:
            print("La palabra contiene símbolos o números.")
    
    for i in palabra:
        print(i)
    break
