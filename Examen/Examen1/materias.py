#-------------- Listado de alumnos --------------
def lista_materias(materias):
    print("\nMateria")
    print("-------")

    #Recorro la lista e imprimo las materias
    for i in materias:
        print(i)

#-------------- Agregar materia --------------
def agregar_materias(materias):
    while   True:
        lista_materias(materias)
        nueva_materia = input("\nIngrese el nombre de la nueva materia: ")
    
        #El nombre de la materia debe tener al menos un caracter y puede contener números (Análisis 1, por ejemplo)
        if(len(nueva_materia) < 1):
            print("Nombre incorrecto.")
        elif(nueva_materia in materias):
            print("Esa materia ya existe.")
        else:
            materias.append(nueva_materia)
            return materias