import clase_chofer as ch

lista_choferes = []
lista_autos = []

class gestorTaxis:

    def instancias_chofer(self):
        while True:
            dni = input("Ingrese el DNI del chofer: ")
            if(dni.isdigit() and len(dni) == 8):
                for chofer in lista_choferes:
                    if dni == chofer.get_dni():
                        print("Ese DNI ya existe.")
                break

            else:
                print("El DNI son sólo números y tienen que ser 8.")


        nombre = input("Ingrese el nombre del chofer: ").capitalize()
        apellido = input("Ingrese el apellido del chofer: ").capitalize()
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del chofer: ").capitalize()
        residencia = input("Ingrese la residencia del chofer: ").capitalize()

        lista_choferes.append(ch.Chofer(nombre, apellido, dni, fecha_nacimiento, residencia))
        
def crear_instancia_auto(self):
    if(len(lista_autos) == 0):
        print("Es necesario tener choferes ..!!")
        return
    
    while True:
        patente = input("Ingrese la patente: ")
        cont_let = 0
        cont_num = 0
        for i in patente:
            if(i.isdigit()):
                cont_num += 1
            elif(i.isalpha()):
                cont_let += 1
        if(cont_let >= 3 and cont_num >= 3):
            break
    
    modelo = input("Ingrese el modelo del auto: ")
    año = input("Ingrese el año del auto: ")
    marca = input("Ingrese la marca del auto: ")
    self.imprimir_info_choferes()



    def imprimir_info_choferes(self):
        for i in lista_choferes:
            i.imprimir_info()

    def imprimir_info_autos(self):
        for i in lista_autos:
            i.imprimir_info()

