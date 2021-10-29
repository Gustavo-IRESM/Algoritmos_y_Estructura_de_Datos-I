#-------------- Menú de productos stock --------------
def menu_productos(productos):
    print("\nCódigo\tNombre")
    print("------\t------")

    for fila in range(len(productos[0])):
        print(f"{productos[0][fila]}\t{productos[1][fila]}")

#-------------- Consultar stock --------------
def consultar_stock(productos):
    print("Código\tNombre\t\tPrecio\tStock")
    print("------\t------\t\t------\t-----")

    for fila in range(len(productos[0])):
        for columna in range(len(productos)):
            print(f"{productos[columna][fila]}", end="\t")
        print()
    
