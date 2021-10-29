import vehiculos as veh

base_vehiculos = []

def cargar_vehiculo():
    marca = input("\nIngrese la marca: ")
        
    while True:
        opcion = input("""
        Indique el tipo de vehículo:
        1 - Moto
        2 - Auto
        3 - Camión
        Seleccione una opción: """)

        if (opcion == "1"):
            tipo_vehiculo = "Moto"
            break
        elif (opcion == "2"):
            tipo_vehiculo = "Auto"
            break
        elif (opcion == "3"):
            tipo_vehiculo = "Camión"
            break
        else:
            print("Opción inválida")

    while True:
        opcion = input("""
        Indique el tipo de combustible:
        1 - Nafta
        2 - Gasoil
        3 - Gas
        Seleccione una opción: """)

        if (opcion == "1"):
            combustible = "Nafta"
            break
        elif (opcion == "2"):
            combustible = "Gasoil"
            break
        elif (opcion == "3"):
            combustible = "Gas"
            break
        else:
            print("Opción inválida")
        
    velmax = float(input("\nIngrese la velocidad máxima: "))
    kilometraje = float(input("\nIngrese los kilómetros que tiene el vehículo: "))
    base_vehiculos.append(veh.vehiculo(marca, tipo_vehiculo, combustible, velmax, kilometraje))

def listar_vehiculos():
    indice = 1
    print("\n\tMarca \t\t Tipo \t\t Combustible \t Vel máx \t Kilometraje")
    for i in base_vehiculos:
        print(f"{indice} - ",end="")
        i.datos_vehiculo()
        indice += 1

def mantenimiento():
    listar_vehiculos()
    id_vehiculo = int(input("\nIngrese el ID del vehículo a chequear: "))
    if(id_vehiculo > len(base_vehiculos) or id_vehiculo == 0):
        print("Ese ID no existe")
    else:
        base_vehiculos[id_vehiculo-1].ver_mantenimiento()
        
