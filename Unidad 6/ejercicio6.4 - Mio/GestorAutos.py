'''
Crear clase GestorAutos que cuente con las siguientes funciones para un menu
1.   Crear auto, indicando tipo de auto y guardar en una lista
2.   Listar autos (presentandolos), indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
'''
import Vehiculos as vh
import Auxiliar as aux

lista_vehiculos = []

class GestorDeAutos:
    #def __init__(self) -> None:
    def __init__(self):
        pass

    #--------------- ---------------
    def crear_auto(self):
        
        '''
        lista_vehiculos.append(vh.Vehiculo("AA133PW","VW",2016,"Alemania"))
        lista_vehiculos.append(vh.Vehiculo("GDL114","VW",2006,"Argentina"))
        lista_vehiculos.append(vh.Vehiculo("UQP013","Fiat",1990,"Italia"))

        patente = input("\nIngrese la patente: ").upper()
        marca = input("Ingrese la marca: ").upper()
        
        #while True:
            #año = aux.ingresar_numero_entero("Ingrese el año origen:",0,2021)
            #if(año == 0 or año > 2021):
                #print("Año no válido.")
            #else:
                #break
        año = aux.ingresar_numero_entero("Ingrese el año origen:",0,2021)
        origen = input("Ingrese el país de origen: ").upper()
    
        lista_vehiculos.append(vh.Vehiculo(patente, marca, año, origen))
        '''

        while True:
            print("""
                Menú tipo de vehículo:
                ----------------------
                1. Particular
                2. PickUp
                3. Deportivo
                """)
            tipo_vehiculo = aux.ingresar_numero_entero("Indique el tipo de vehículo:",1,3)
            if(tipo_vehiculo == 1):
                lista_vehiculos.append(vh.Vehiculo_Particular("AA133PW","VW",2016,"Alemania",130))
                break
            elif(tipo_vehiculo == 2):
                lista_vehiculos.append(vh.Vehiculo_PickUp("GDL114","VW",2006,"Argentina",120))
                break
            elif(tipo_vehiculo == 3):
                lista_vehiculos.append(vh.Vehiculo_Deportivo("UQP013","Fiat",1990,"Italia",110))
                break
            else:
                print("Tipo de vehículo no válido.")
        

    #--------------- ---------------
    def listar_autos(self):
        for vehiculo in lista_vehiculos:
            vehiculo.presentarse()

    #--------------- ---------------
    def cambiar_velocidad(self):
        #Muestro los autos en la BD
        while True:
            vehiculo = self.existe_vehiculo()
            if(vehiculo):
                #Ingreso la nueva vel máx
                vehiculo.obtener_velocidad_max()
                nueva_vel_max = aux.ingresar_numero_entero("Ingrese la nueva vel máx: ",1,500)
                vehiculo.setear_velocidad_max(nueva_vel_max)
                break

    #--------------- ---------------
    def calcular_tiempo(self):
        while True:
            distancia = aux.ingresar_numero_entero("\nIngrese la distancia en KM del recorrido: ",0,1000)
            if(distancia <= 0):
                print("Valor de distancia incorrecto.")
            else:
                vehiculo = self.existe_vehiculo()
                if(vehiculo):
                    print("Tiempo del viaje: ", distancia / vehiculo.velocidad_max)

    #---------- Verifico si existe el vehículo ----------
    def existe_vehiculo(self,patente = ""):
        self.listar_autos()

        while True:
            if (patente == ""):
                patente = input("\nIngrese la patente: ").upper()

            for vehiculo in lista_vehiculos:
                if(patente == vehiculo.patente):
                    #print(f"La patente del vehículo es {patente}")
                    #----- Existe -----
                    return vehiculo

            #----- NO existe -----
            print("Ese vehículo NO existe.")
            return False

