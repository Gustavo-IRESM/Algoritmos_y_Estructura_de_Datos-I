def convAB(alfab_a, alfab_b):
    while True:
        palabra = input("\nIngrese la palabra a convertir: ")
        if(palabra.isalpha()):
            break
        else:
            print("La palabra sólo puede contener letras")

    palabra = palabra.lower()

    for i in palabra:
        indice = alfab_a.index(i)
        print(f"{i} = {alfab_b[indice]}")
    

