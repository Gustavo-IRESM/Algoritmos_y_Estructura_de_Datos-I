'''
##**Ejercicio 5.2**
Crear una funcion que debe:

*    Pedir al usuario una palabra o una frase
*    Indicar si esta se trata de un palindromo (reconocer, neuquen, amor a roma)
*    No deben aparecer y se deben tener en cuenta todos los posibles errores
'''

def polindromo(palabra):
    lista = list(palabra)
    lista1 = lista.copy()
    lista1.reverse()
    if(lista == lista1):
        print("Es un políndromo\n")
    else:
        print("NO es un políndromo\n")

while True:
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    palabra= input("Ingrese una palabra o frase: ")
    #if(palabra.isalpha()):
    if(numeros in palabra):
        polindromo(palabra)
    else:
        print("La palabra no puede tener espacios, ni números, ni caracteres especiales")