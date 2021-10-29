def existe_letra(alfab_a, alfab_b):
    while True:
        alfabeto = input("\nSeleccione el alfabeto A o B: ")
        alfabeto = alfabeto.lower()
        if(alfabeto == "a" or alfabeto == "b"):
            break
        else:
            print("Debe seleccionar A o B.")
    
    while True:
        letra = input("\nIngrese la letra a buscar: ")
        if(alfabeto == "a"):
            if(len(letra) > 1):
                print("Para el alfabeto A debe ingresar solo una letra")
            else:
                if(letra.isalpha()):
                    letra = letra.lower()
                    if(letra in alfab_a):
                        existe = True
                        break
                    else:
                        existe = False
                        break
                else:
                    print("Debe ingresar una letra.\nNo se permiten números ni caracteres especiales.")
        elif(alfabeto == "b"):
            if("." in letra) or ("-" in letra):
                if(letra in alfab_b):
                    existe = True
                    break
                else:
                    existe = False
                    break
            else:
                print("Las letras del alfabeto B sólo pueden tener '.' '-' o una combinación de los mismos.")
    
    if (existe):
        #existe = True -> la letra EXISTE
        print("Esa letra EXISTE en el alfabeto.")
        return
    else:
        #existe = False -> la letra NO existe
        print("Esa letra NO existe en el alfabeto.")
        return
        
    
    