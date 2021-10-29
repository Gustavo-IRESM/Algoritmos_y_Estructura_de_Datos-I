"""
##**Ejercicio 5.3**
Crear una funcion que debe:

-    Pedir al usuario 5 materias (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
-    Verficiar que sea un nombre correcto (Matemática 1, Matemática 2). En este caso las materias tienen una sola palabra
-    Almacenar los nombres en una lista
-    Mostrar las materias en orden alfabetico
-    No deben aparecer y se deben tener en cuenta todos los posibles errores
"""
def ordenamiento_palabra():
    lista_materias = []
    for i in range(5):
        materia = input("Ingrese una materia: ")
        lista_materias.append(materia)
    lista_materias.sort()
    print (lista_materias)

ordenamiento_palabra()