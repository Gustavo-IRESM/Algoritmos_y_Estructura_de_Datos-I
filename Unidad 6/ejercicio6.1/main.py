"""
###**Ejercicio 6.1**
Crear una clase de Persona:
*   Cuyo constructutor debe inicializar los atributos nombre, apellido, edad, ciudad_de_recidencia
*   Se deben crear dos metodos en la clase:
    1.  Presentarse que la persona indique: Soy {nombre} {apellido}, tengo {edad} años y vivo en 
        {ciudad de recidencia}
    2.  Indique segun la edad de la persona si esta es: Niño (0 a 14), Adolecente (14 a 22),
         Joven (22 a 30), mayor(30 a 50), mas mayor(50 a 120)

*    Menu:
    1. para crear personas
    2. Segun el nombre de persona indicar edad"""
import Persona as pn
import funciones_main as fn

while True:
    opcion = input(
    """
-----------Menu principal-----------
Por favor ingrese una opcion:
    1. Crear personas
    2. Verificar rango etario
    3. Listar personas
    4. Salir
    Opcion: """
    )
    if (opcion=="1"):
        fn.crear_personas() #cómo salta al archivo de funciones ?????
    elif (opcion=="2"):
        fn.consultar_rango()
    elif (opcion=="3"):
        fn.listar_personas()
    elif (opcion=="4"):
        break
    else:
        print("ninguna opcion correcta")
