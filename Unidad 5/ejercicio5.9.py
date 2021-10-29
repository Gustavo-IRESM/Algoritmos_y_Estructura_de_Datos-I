'''
##**Ejercicio 5.9 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos cheferes
```
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
    *  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
*   Contar con 6 funciones disponibles en el menu:
    1. Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    2. Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    3. Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    4. Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo -> ULTIMO
    5. Observar una lista de autos choferes y recorrido maximo con el siguiente formato:
    6. Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -   45
auto_2  -   chofer_2   -   50
auto_3  -   chofer_3   -   50
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''
Taxis=[["auto_1","auto_2","auto_3"],["chofera","choferb","choferc"],[10,30,50]]
def listar():
    print("AUTO    -    CHOFER    -   RECORRIDO")
    for i in range(len(Taxis[0])):
        print(f"{Taxis[0][i]} - {Taxis[1][i]} - {Taxis[2][i]}")

def modificar_nombre_chofer():
    listar()
    while True:
        indicar_auto = input("Nombre del auto a modificar: ")
        if indicar_auto in Taxis[0]:
            Taxis[1][Taxis[0].index(indicar_auto)] = input("Nuevo nombre del chofer: ")
            listar()
            break
        else:
            print("no existe ese auto")

def nuevo_viaje():
    while True:
        try:
            while True:
                distancia = float(input("Ingrese la distancia del viaje:"))
                if(distancia <= 0):
                    print("La distancia debe ser mayor que cero")
                else:
                    print("Posibles autos que podrían realizar el viaje:")
                    for columnas in range(len(Taxis[2])):
                        if(distancia <= Taxis[2][columnas]):
                            print(f"Auto: {Taxis[0][columnas]} - Chofer: {Taxis[1][columnas]}")
                    return
        except:
            print("Debe ingresar una distancia válida")

def informacion_chofer():
    chofer = input("Por favor ingrese el nombre del chofer: ")
    if chofer.isalpha():
        if chofer in Taxis[1]:
            print (f"El chofer maneja el {Taxis[0][Taxis[1].index(chofer)]} y hace {Taxis[2][Taxis[1].index(chofer)]} kilómetros.")
        else:
            print("Este chofer no trabaja en esta empresa")

informacion_chofer()