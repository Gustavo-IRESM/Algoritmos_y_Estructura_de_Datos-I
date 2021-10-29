'''
##**Ejercicio 5.9 (Empresa de Taxis)**
El programa debe:
*   Simular una empresa de taxis que cuente con tres Autos con sus respectivos cheferes
```
Taxis=[["auto_1","auto_2","auto_3"],["chofer_1","chofer_2","chofer_3"],[45,50,30]]
```
+  Cada auto cuenta con un chofer y no hace recorridos mayores a lo q se le indica
-   Contar con 6 funciones disponibles en el menu:
    + Preguntar al usuario el recorrido del viaje e indicar posibles autos y choferes
    + Modificar nombre chofer segun el nombre del auto.
        auto_1 -> "federico"
    - Modificar el recorrido segun el nombre del auto.
        auto_1 -> 60
    + Agregar nuevo auto a la empresa de Taxis, indicando auto, nombre chofer y recorrido maximo
    + Observar una lista de autos choferes y recorrido maximo con el siguiente formato:
    + Observar informacion de un chofer, verificando su existencia previamente

```
AUTO    -    CHOFER    -   RECORRIDO
auto_1  -   chofer_1   -   45
auto_2  -   chofer_1   -   50
```
    
*   Gestionar posibles errores
*   Estructurar el programa a criterio propio
'''

Taxis=[["auto_1","auto_2","auto_3","auto_4"],["chofer_1","chofer_2","chofer_3","chofer_4"],[10,30,50,45]]

#------------------------------------------------
def nuevo_viaje():
    while True:
        try:
            while True:
                distancia = float(input("Ingrese la distancia del viaje: "))
                if(distancia <= 0):
                    print("La distancia debe ser mayor que cero.")
                else:
                    print("Autos que podrían realizar el viaje:")
                    for columnas in range(len(Taxis[0])):
                        if(distancia <= Taxis[2][columnas]):
                            print(f"Auto: {Taxis[0][columnas]} - Chofer: {Taxis[1][columnas]}")
                    return
        except:
            print("Debe ingresar una distancia válida.")

#------------------------------------------------
def mod_nombre_chofer():
    listar_datos()
    
    while True:
        auto = input("Ingrese el auto: ")
        if(auto in Taxis[0]):
            indice = Taxis[0].index(auto)
            nombre_nuevo = input("Ingrese el nuevo nombre del chofer: ")
            Taxis[1][indice] = nombre_nuevo
            listar_datos()
            return
        else:
            print("Ese auto no existe. Vuelva a intentarlo")
    
#------------------------------------------------
def mod_recorrido():
    listar_datos()
    
    while True:
        auto = input("Ingrese el auto: ")
        if(auto in Taxis[0]):
            indice = Taxis[0].index(auto)
            while True:
                try:
                    nuevo_recorrido = float(input("Ingrese el nuevo recorrido: "))
                    if(nuevo_recorrido <= 0):
                        print("La distancia debe ser mayor que cero.")
                    else:
                        Taxis[2][indice] = nuevo_recorrido
                        listar_datos()
                        return
                except:
                    print("Debe ingresar una distancia válida.")
        else:
            print("Ese auto no existe. Vuelva a intentarlo.")

#------------------------------------------------
def listar_datos():
    print("\nAUTO \t CHOFER \t RECORRIDO")
    print("---- \t ------ \t ---------")
    for filas in range(len(Taxis[0])):
        for columnas in range(len(Taxis)):
            print(f"{Taxis[columnas][filas]}", end=" \t ")
        print()
    print()

#------------------------------------------------
def agregar_auto():
    auto = input("Ingrese el auto: ")
    chofer = input("Ingrese el chofer: ")
    
    while True:
        try:
            distancia = float(input("Ingrese la distancia: "))
            if(distancia <= 0):
                print("La distancia debe ser mayor que cero")
            else:
                #print(Taxis)
                Taxis[0].append(auto)
                Taxis[1].append(chofer)
                Taxis[2].append(distancia)
                listar_datos()
                return
        except:
            print("Debe ingresar una distancia válida")

#------------------------------------------------
def info_chofer():
    while True:
        auto = input("Ingrese el nombre del chofer: ")
        try:
            indice = Taxis[1].index(auto)
            if(indice >= 0):
                print("AUTO \t CHOFER \t RECORRIDO")
                print("---- \t ------ \t ---------")
                for i in range(len(Taxis)):
                    print(f"{Taxis[i][indice]}", end=" \t ")
                print()
                return
        except:
            print("Ese chofer no existe. Vuelva a intentarlo.") 


#------------------------------------------------
#-              Programa principal              -
#------------------------------------------------

while True:
    opcion = input('''
    MENÚ
    ----
    1 - Nuevo viaje
    2 - Modificar nombre chofer
    3 - Modificar recorrido
    4 - Agregar auto
    5 - Listar autos choferes y recorridos
    6 - Información de un chofer
    0 - Salir
    Seleccione una opción: ''')

    print()

    if(opcion == "1"):
        nuevo_viaje()
        pass
    elif(opcion == "2"):
        mod_nombre_chofer()
        pass
    elif(opcion == "3"):
        mod_recorrido()
        pass
    elif(opcion == "4"):
        agregar_auto()
        pass
    elif(opcion == "5"):
        listar_datos()
    elif(opcion == "6"):
        info_chofer()
        pass
    elif(opcion == "0"):
        break
