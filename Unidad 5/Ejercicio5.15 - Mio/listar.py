import varios

def listar_base(base):
    opcion = varios.menu_pelis_series()
    if(opcion =="1"):
        print(f"\n--------- P E L Í C U L A S ---------")
        for i in range(len(base.get("peliculas"))):
            print(f"{i} - {base.get('peliculas')[i].capitalize()}")
    elif(opcion =="2"):
        print(f"\n--------- S E R I E S ---------")
        for i in range(len(base.get("series"))):
            print(f"{i} - {base.get('series')[i].capitalize()}")
    else:
        return

def listar_algunas(base):
    opcion = varios.menu_pelis_series()
    if(opcion == 0):
        return

    try:
        desde = int(input("Ingrese el ID desde donde quiere listar: "))
        hasta = int(input("Ingrese el ID hasta donde quiere listar: "))
        if(desde > hasta):
            print("El valor de hasta debe ser mayor que el de desde")
        elif((desde < 0) or (hasta < 0)):
            print("Desde y hasta deben ser mayores o iguales a 0")
        else:
            if(opcion =="1"):
                print(f"\n--------- P E L Í C U L A S ---------")
                #for i in range(len(base.get("peliculas"))):
                for i in range(desde, hasta + 1):
                    print(f"{i} - {base.get('peliculas')[i].capitalize()}")
            else:
                print(f"\n--------- S E R I E S ---------")
                #for i in range(len(base.get("series"))):
                for i in range(desde, hasta + 1):
                    print(f"{i} - {base.get('series')[i].capitalize()}")

    except:
        print("Error en los parámetros desde/hasta")
        