'''
Crear clase GestorComputadora que cuente con las siguientes funciones para un menu
    - 1. Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
    - 2. Listar Computadoras (presentandolos), indicando tipo.
    - 3. Cambiar SO de una Computadora, verificando una lista de SO disponibles
    - 4. Listar perifericos
'''

import Compus as cp
import Auxiliar as aux

lista_compus = []
lista_tipos = ["Genérica","Escritorio","Notebook"]
lista_marca = ["Lenovo","Mac","Asus","Samsung","HP"]
lista_so = ["Linux", "Windows","Windows server","Ubuntu","Mac OS"]
lista_perifericos = ["Teclado","Mouse","Monitor","Parlantes","Impresora"]

class GestorDeCompus:
    def __init__(self):
        pass

    #--------------- ---------------
    def crear_compu(self):
        '''
        pc_1 = cp.Compus(1,["Teclado","Mouse"],"Linux")
        pc_2 = cp.Escritorio(2,["Teclado","Parlantes"],"Windows","HP")
        pc_3 = cp.Notebook(3,["Parlantes","Mouse inalámbrico"],"Ubuntu","Lenovo")
        lista_compus.append(pc_1)
        lista_compus.append(pc_2)
        lista_compus.append(pc_3)
        '''
        while True:
            print("\nTipos")
            print("-----")
            for id in range (len(lista_tipos)):
                print(f"{id + 1} - {lista_tipos[id]}")

            tipo_compu = aux.ingresar_numero_entero("Ingrese el tipo de compu (0 para salir): ",0,len(lista_tipos))
            if(tipo_compu == 0):
                return
            else:
                break

        if(tipo_compu == 2 or tipo_compu == 3):
            #--------------- MARCA ---------------
            while True:
                print("\nMarcas")
                print("------")
                for id in range (len(lista_marca)):
                    print(f"{id + 1} - {lista_marca[id]}")

                id_marca = aux.ingresar_numero_entero("Ingrese la marca: ",0,len(lista_marca)) - 1
                break
        #else:
            #print("Año no válido.")
            #break

        #--------------- PERIFÉRICOS ---------------
        nuevos_perifericos = []
        while True:
            print("\nPerfifericos")
            print("------------")
            for id in range (len(lista_perifericos)):
                print(f"{id + 1} - {lista_perifericos[id]}")

            id_periferico = aux.ingresar_numero_entero("Ingrese los periféricos (0 para salir): ",0,len(lista_perifericos))
            if(id_periferico == 0):
                break
            else:
                id_periferico -= 1
                nuevos_perifericos.append(lista_perifericos[id_periferico])        
        
        #--------------- SISTEMA OPERATIVO ---------------

        id_so = self.seleccionar_so()
       
        #--------------- CREAR COMPU ---------------
        id_compu = len(lista_compus)
        if(tipo_compu == 1):
                nueva_compu = cp.Compus(id_compu,nuevos_perifericos,lista_so[id_so])
                lista_compus.append(nueva_compu)
        elif(tipo_compu == 2):
                nueva_compu = cp.Escritorio(id_compu,nuevos_perifericos,lista_so[id_so],lista_marca[id_marca])
                lista_compus.append(nueva_compu)
        elif(tipo_compu == 3):
            nueva_compu = cp.Notebook(id_compu,nuevos_perifericos,lista_so[id_so],lista_marca[id_marca])
            lista_compus.append(nueva_compu)
        else:
            print("Tipo de compu NO válido.")


    #--------------- ---------------
    def listar_compus(self):
        print("\nLISTADO DE COMPUTADORAS")
        print("-----------------------")
        for compu in lista_compus:
            compu.presentarse()
            compu.tipo_compu()

    #--------------- ---------------
    def cambiar_so(self):
        #Muestro las PCs que tengo cargadas
        self.listar_compus()
        id_compu = aux.ingresar_numero_entero("\nID de la compu que desea cambiar el S.O.: ",1,len(lista_compus))
        
        nuevo_so = self.seleccionar_so()
        for compu in lista_compus:
            if(id_compu == compu.id):
                compu.cambiar_so(lista_so[nuevo_so])
                return

    #--------------- ---------------
    def listar_perifericos(self):
        #Muestro las PCs que tengo cargadas
        self.listar_compus()
        id_compu = aux.ingresar_numero_entero("\nID de la compu para listar sus periféricos: ",1,len(lista_compus))

        for compu in lista_compus:
            if(id_compu == compu.id):
                print(f"Los perfiféricos de la compu son: {compu.listaPerifericos}")
                return

    #--------------- ---------------
    def seleccionar_so(self):
        print("\nSISTEMAS OPERATIVOS")
        print("-------------------")
        for id in range (len(lista_so)):
            print(f"{id + 1} - {lista_so[id]}")

        id_so = aux.ingresar_numero_entero("Seleccione el SO: ",0,len(lista_so)) - 1
        return id_so









    #---------- Verifico si existe el vehículo ----------
    def existe_compu(self):
        self.listar_compus()

        while True:
            if (patente == ""):
                patente = input("\nIngrese la patente: ").upper()

            for vehiculo in lista_compus:
                if(patente == vehiculo.patente):
                    #print(f"La patente del vehículo es {patente}")
                    #----- Existe -----
                    return vehiculo

            #----- NO existe -----
            print("Ese vehículo NO existe.")
            return False







'''




for i in lista:
    i.presentarse()
    i.tipo_compu()


'''