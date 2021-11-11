
import Empleado as em
import Animal as an
import Auxiliar as aux

lista_empleados = []
lista_animales = []
lista_animales_cuidar = []
#tipo_animales = ["Felino","Mamífero","Anfibio","Reptil","Ave","Insecto","Crustáceo"]

class GestorZoologico:
    def __init__(self):
        pass

    #---------- 1. Crear animal ----------    
    def crear_animal(self):
        '''
        lista_animales.append(an.Animal("perro","mamifero","1/1/2010","gustavo"))
        lista_animales.append(an.AnimalesAcuaticos("gato","felino","9/1/2010","laura"))
        lista_animales.append(an.AnimalesEnjaulados("loro","ave","8/1/2010","bautista"))
        lista_animales.append(an.AnimalesSueltos("sapo","reptil","7/1/2010","vera"))
        '''

        if(len(lista_empleados) == 0):
            print("\nIngresar al menos un encargado antes de cargar un animal.")
            return
        
        #----- Controlo si ese animal ya existe
        while True:
            animal_existe = False
            nombre = input("\nNombre del animal: ")
            #tipo_animal = self.tipo_animal()
            for i in lista_animales:
                #if(nombre == i.nombre and tipo_animal == i.tipo_animal):
                if(nombre == i.nombre):
                    animal_existe = True
                    break
            
            if(animal_existe):
                print("\nEse animal ya EXISTE")
            else:
                break

        tipo_animal = self.tipo_animal()
        fecha_nac = input("\nFecha de nacimiento dd/mm/aaaa: ")
        legajo_cuidador = self.buscar_empleado()


        if(tipo_animal == "1"):
            lista_animales.append(an.Animal(nombre, tipo_animal, fecha_nac, legajo_cuidador))
        elif(tipo_animal == "2"):
            lista_animales.append(an.AnimalesEnjaulados(nombre, tipo_animal, fecha_nac, legajo_cuidador))
        elif(tipo_animal == "3"):
            lista_animales.append(an.AnimalesSueltos(nombre, tipo_animal, fecha_nac, legajo_cuidador))
        elif(tipo_animal == "4"):
            lista_animales.append(an.AnimalesAcuaticos(nombre, tipo_animal, fecha_nac, legajo_cuidador))
        

    #---------- 2. Crear empleado ----------    
    def crear_empleado(self):
        '''
        lista_empleados.append(em.Empleado(123,"Gustavo","Distel"))
        lista_empleados.append(em.Empleado(456,"Laura","Denipotti"))
        lista_empleados.append(em.Empleado(789,"Vera","Distel"))
        lista_empleados.append(em.Empleado(147,"Bautista","Distel"))
        
        
        lista_empleados.append(em.Empleado(123,"Gustavo","Distel",["perro","gato"]))
        lista_empleados.append(em.Empleado(456,"Laura","Denipotti",["loro"]))
        lista_empleados.append(em.Empleado(789,"Vera","Distel",["sapo"]))
        lista_empleados.append(em.Empleado(147,"Bautista","Distel",["perro"]))
        '''

        existe_legajo = False
        legajo = aux.ingresar_numero_entero("Nro de legajo: ",1,9999)

        for i in lista_empleados:
            if (legajo == i.get_legajo()):
                existe_legajo = True
                break

        if(existe_legajo):
            print("Ya existe ese número de legajo.")
            return
        else:
            #----- El legajo NO existe, cargo los demás parámetros -----
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")

            #lista_empleados.append(em.Empleado(legajo, nombre, apellido))

            #----- Si hay animales en la lista, le asigno uno para cuidar -----
            '''
            if(len(lista_animales) > 0):
                print("\nANIMAL A CUIDAR:")
                print("----------------", end="")

                animal_a_cuidar = self.buscar_animal()
                lista_animales_cuidar.append(animal_a_cuidar.nombre)
            #else:
                #No hay animales en la lista, lo cargo en blanco
            '''

            #lista_empleados.append(em.Empleado(legajo, nombre, apellido, lista_animales_cuidar))
            lista_empleados.append(em.Empleado(legajo, nombre, apellido, []))
            
        
    #---------- 3. Asignar animal a un empleado ----------
    def asignar_cuidador(self):
        #print()     #Separador
        animal = self.buscar_animal()

        print(f"\nASIGNAR CUIDADOR AL ANIMAL {animal.nombre}", end="")
        legajo_cuidador = self.buscar_empleado()
        
        print(f"Animal: {animal.nombre} - Cuidador: {legajo_cuidador}")

        for cuidador in lista_empleados:
            if(cuidador.legajo == legajo_cuidador):
                print(f"{cuidador.legajo} = {legajo_cuidador}")
                cuidador.asignar_animales(animal.nombre)
                #pass

    #---------- 4. Cambiar de encargado a un animal ----------
    def cambiar_cuidador(self):
        print("""
CAMBIAR CUIDADOR
-----------------
Seleccione el animal al cual desea cambiarle el cuidador""")
        nombre_animal = self.buscar_animal()

        print("\nNUEVO CUIDADOR.", end="")
        legajo_cuidador = self.buscar_empleado()
        
        #----- Busco el animal -----
        for i in lista_animales:
            if(i.nombre == nombre_animal.nombre):
                i.set_empleado(legajo_cuidador)

    #---------- 5. Imprimir lista de animales ----------
    def imprimir_animales(self):
        print()     #Separador
        for animal in lista_animales:
            animal.presentarse()

    #---------- 6. Imprimir lista de empleados ----------
    def imprimir_empleados(self):
        print()     #Separador
        for empleado in lista_empleados:
            empleado.presentarse()

    #---------- Especifico tipo de animal ----------
    def tipo_animal(self):
        while True:
            opcion = input("""
    MENU TIPO ANIMAL
    ----------------
        1. Animal genérico
        2. Animal en jaula
        3. Animal suelto
        4. Animal acuático
        Seleccione una opción: """)
		
            if(opcion >= "1" and opcion <= "4"):
                return opcion
            else:
                print("Opción incorrecta.")
            
            
            
            
            
            '''
            contador = 1
            print("\nTIPO ANIMAL")
            print("-----------")
            for i in tipo_animales:
                print(f"{contador} - {i}")
                contador += 1

            opcion = aux.ingresar_numero_entero("Seleccione una opción: ",1,len(tipo_animales))

            return tipo_animales[opcion-1]
            '''

    #---------- Buscar una animal por nombre----------
    def buscar_animal(self):
        print() #Separador

        while True:
            self.imprimir_animales()
            nombre_animal = input("Ingrese el nombre del animal: ")
            for i in lista_animales:
                if(i.nombre == nombre_animal):
                    return i
            
            print("Ese animal no existe.")

    #---------- Buscar un empleado por número de legajo ----------
    def buscar_empleado(self):
        print() #Separador

        while True:
            self.imprimir_empleados()
            legajo = aux.ingresar_numero_entero("Nro de legajo: ",1,9999)
            for i in lista_empleados:
                if(i.legajo == legajo):
                    #return i
                    return legajo
            
            print("Ese legajo no existe:")