"""
##**Ejercicio 5.10 (Conversión de alfabeto)**
El programa debe:
*   Simular la conversion de un alfabeto a otro: Por ejemplo el moorse 
    (NO ES ESTRICTAMENTE NECESARIO USAR ESTE ALFABETO, PUEDE SER INVENTADO)

```
 alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]
```

*   Contar con 6 funciones disponibles en el menu:
    + 1. Mostrar el alfabeto A
    + 2. Mostrar el alfabeto B
    - 3. Modificar una letra del Alfabeto A y el alfabeto B (debe ser la misma)
    + 4. Conversion de alfabeto A a alfabeto B: ejemplo **abc --> .--...-.-.**
    - 5. Conversion de alfabeto B a alfabeto A: ejemplo **.--...-.-. --> abc**
    - 6. Verificacion de existencia de una letra del alfabeto (debe seleccionar A o B)

*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
    """
alfabeto_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_b = ['.-' ,'-...' , '-.-.' ,'-..' ,'.', '..-.','--.', '....','..' ,'.---' , '-.-', '.-..','--' ,'-.' ,'---' ,'.--.','--.-' , '.-.' ,'...' ,'-','..-' ,'...-','.--','-..-' , '-.--' , '--..' ]

import mostrar_alfabeto_A as mos_alfab_A
import mostrar_alfabeto_B as mos_alfab_B
import modificar_letra as modletra
import convertir_AB as conv_AB
import convertir_BA as conv_BA
import verificar_existencia as verexist

#------------------------------------------------
#-              Programa principal              -
#------------------------------------------------

while True:
    opcion = input('''
    MENÚ
    ----
    1. Mostrar el alfabeto A
    2. Mostrar el alfabeto B
    3. Modificar una letra de
    l Alfabeto A y el alfabeto B
    4. Conversion de alfabeto A a alfabeto B
    5. Conversion de alfabeto B a alfabeto A
    6. Verificacion de existencia de una letra del alfabeto
    0 - Salir
    Seleccione una opción: ''')

    if(opcion == "1"):
        mos_alfab_A.mostrar_A(alfabeto_a, alfabeto_b)
    elif(opcion == "2"):
        mos_alfab_B.mostrar_B(alfabeto_a, alfabeto_b)
    elif(opcion == "3"):
        pass
    elif(opcion == "4"):
        conv_AB.convAB(alfabeto_a, alfabeto_b)
    elif(opcion == "5"):
        pass
    elif(opcion == "6"):
        verexist.existe_letra(alfabeto_a, alfabeto_b)
    elif(opcion == "0"):
        break