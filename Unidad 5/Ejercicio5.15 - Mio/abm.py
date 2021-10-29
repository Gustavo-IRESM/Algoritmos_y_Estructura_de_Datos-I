import varios

def agregar(base):
    print("Indique si desea agregar películas o series:")
    opcion = varios.menu_pelis_series()
    if(opcion == "0"):
        return base
    else:
        print("\nIngrese el nombre de la", end=" ")
        if(opcion == "1"):
            pelicula = input("película: ")
            if(pelicula in base.get("peliculas")):
                print("Esa película ya existe en la base.")
            else:
                base.get("peliculas").append(pelicula) 
        
        if(opcion == "2"):
            serie = input("serie: ")

            if(serie in base.get("series")):
                print("Esa serie ya existe en la base.")
            else:
                base.get("series").append(serie)
        
        return base

