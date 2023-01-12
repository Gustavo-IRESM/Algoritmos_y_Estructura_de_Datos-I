#-------------- Listado de alumnos --------------
def lista_alumnos(alumnos):
    print("\nUsuario\t\tEdad\t\tmail")
    print("-------\t\t----\t\t----")

    #Recorro la lista e imprimo los alumnos con sus respectivos datos
    for fila in range(len(alumnos[0])):
        for columna in range(len(alumnos)):
            print(f"{alumnos[columna][fila]}", end="\t\t")
        print()

#-------------- Agrego un alumno --------------
def agregar_alumno(alumnos):
    while True:
        lista_alumnos(alumnos)
        nombre = input("\nIngrese el nombre del nuevo alumno: ")
        
        #Controlo si el nombre ingresado ya existe
        if(nombre in alumnos[0]):
            print("Ese alumno ya EXISTE en la lista")
        else:
            break
    
    #Ingresar edad
    edad = validar_edad()

    while True:
        mail = input("\nIngrese el mail del alumno: ")
        #Controlo si el mail tiene @ y si la dirección tiene al menos 3 caracteres
        if("@" in mail and len(mail) >= 3):
            alumnos[0].append(nombre)
            alumnos[1].append(edad)
            alumnos[2].append(mail)
            return alumnos
        else:
            print("Mail incorrecto.")

#-------------- Modifico la edad de un alumno --------------
def editar_edad(alumnos):
    while True:
        lista_alumnos(alumnos)
        nombre = input("\nIngrese el nombre del alumno cuya edad se quiere modificar: ")
        
        if(nombre in alumnos[0]):
            #Alumno existe. Busco la posición en la lista
            indice = alumnos[0].index(nombre)
            #El alumno existe. Valido la edad y la cambio
            alumnos[1][indice] = validar_edad()
            return alumnos
        else:
            #No existe el alumno en la lista
            print("Ese alumno NO existe.")

#-------------- Valido la edad --------------
def validar_edad():
    while True:
        try:
            edad = int(input("\nIngrese la edad: "))
            
            #No puede ser una edad negativa ni igual a cero
            if(edad <= 0):
                print("La edad debe ser mayor a cero.")
            elif(edad < 10 or edad > 18):
                print("La edad debe estar entre 10 y 18 años.")
            else:
                #La edad ingresada es correcta.
                return edad
        except:
            #La edad no es un número
            print("Edad incorrecta.")