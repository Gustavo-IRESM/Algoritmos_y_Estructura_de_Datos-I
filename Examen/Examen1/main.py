'''
************************************************************
 MATERIA: Algoritmos y Estructuras de Datos 1
 EXAMEN: 1° Examen
 APELLIDO Y NOMBRE: Distel, Gustavo
 DNI: 21.035.759
 CARRERA: Analista de Sistemas
 AÑO: 2021 
 Se envia mail con asunto: "[AYEDI 2021 - Apellido, Nombre - 1°Examen]"
 ************************************************************
 Items a evaluar:
 1. Requerimientos y comprension de consignas
 2. Estructura (modularización), legibilidad y comentarios del codigo.

¡Cualquier duda con el enunciado consultar al docente!
************************************************************
ENUNCIADO: "Programa de Gestión de alumnos y Materias"

Introduccion: 
    El siguiente programa consiste en un software de gestion de alumnos y gestion de materias
    de una institucion educativa.
    El programa debe permitir agregar y quitar alumnos al sistema junto con su informacion personal: 
    Nombre, Edad y mail.
    El programa debe permitir agregar Materias al sistema.

Requerimientos:
El programa debe:
*   Contar con un menu donde permita al usuario elegir entre las siguientes funciones:
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail)
    2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad - Mail)
       Verificando: Que el nombre_usuario no exista previamente, la edad entre 10 y 18 años y que el mail cuente con un @.
       (Ayuda: metodo in de list sirve tambien para strings)
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias)
    5. Agregar materias al sistema (verificando que no exista previamente)
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

base_alumnos = [["alumno1","alumno2","alumno3"],[10,12,17],["alumno1@gmail.com","alumno2@gmail.com","alumno3@gmail.com"]]
base_materias = ["materia1","materia2","materia3","materia4"]

#------------------------------------------------
#-              Programa principal              -
#------------------------------------------------

import alumnos as al
import materias as mat

while True:
    opcion = input('''
    MENÚ
    ----
    1 - Listado de alumnos
    2 - Agregar alumno
    3 - Editar edad alumno
    4 - Listado de materias
    5 - Agregar materia
    0 - Salir
    Seleccione una opción: ''')

    if(opcion == "1"):
        al.lista_alumnos(base_alumnos)
    
    elif(opcion == "2"):
        base_alumnos = al.agregar_alumno(base_alumnos)
    
    elif(opcion == "3"):
        base_alumnos = al.editar_edad(base_alumnos)
    
    elif(opcion == "4"):
        mat.lista_materias(base_materias)
    
    elif(opcion == "5"):
        base_materias = mat.agregar_materias(base_materias)

    elif(opcion == "0"):
        break
    
    else:
        print("Opción inválida.")

