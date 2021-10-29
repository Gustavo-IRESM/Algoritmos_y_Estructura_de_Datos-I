import Persona as pn
lista_personas = [] #!!!!!!!!!!!!!!!!11

def crear_personas():
    while True: #pide dni
        dni = input("Por favor ingrese el dni: ")
        if dni.isdigit():
            flag_agregar = True
            for persona in lista_personas:
                if dni == persona.dni:
                    print("ese dni ya existe")
                    flag_agregar = False
                    break
            if(flag_agregar): #significa que el dni es valido, puedo salir de su while
               break 
        else:
            print("El dni es numerico")
    #nombre
    while True:
        nombre = input("Por favor ingrese el nombre: ").capitalize()
        if not nombre.isalpha():
            print("un nombre no puede tener simbolos")
        else:
            break
    #apellido
    while True:
        apellido = input("Por favor ingrese el apellido: ").capitalize()
        if not apellido.isalpha():
            print("un apellido no puede tener simbolos")
        else:
            break
    #edad
    while True:
        try:
            edad = int(input("Por favor ingrese la edad: "))
            if edad<=0:
                print("la edad debe ser mayor a cero")
            else:
                break
        except:
            print("Error de argumentos")

    #residencia
    residencia = input("Por favor ingrese la residencia: ").capitalize()
    #nombre_instancia = dni+nombre   #?????????????

    #instanciando o creando un objeto de persona
    nombre_instancia = pn.Persona(dni,nombre,apellido,edad,residencia)
    #lista_personas.append(nombre_instancia)
    lista_personas.append(pn.Persona(dni,nombre,apellido,edad,residencia))

def listar_personas():
    for persona in lista_personas:
        persona.presentarse()   #?????????????

def consultar_rango():
    print("------ Lista de personas------")
    for persona in lista_personas:
        print(f"{persona.dni}\t{persona.nombre}\t{persona.apellido}\t{persona.edad}\t")
    while True: #pide dni
        dni_consultar = input("ingrese el dni a consultar")
        if dni_consultar.isdigit():
            for persona in lista_personas:  #no se puede buscar en la lista en vez de iterar ?????
                if dni_consultar == persona.dni:
                    persona.rango_edad()
                    return
        else:
            print("El dni es numerico")