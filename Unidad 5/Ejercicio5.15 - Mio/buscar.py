import varios

def buscar_titulos(base):
    titulo = input("Ingrese el título que desea buscar: ")
    if (titulo in base.values("peliculas")):
        print("Es una película")
    if (titulo in base.values("series")):
        print("Es una serie")