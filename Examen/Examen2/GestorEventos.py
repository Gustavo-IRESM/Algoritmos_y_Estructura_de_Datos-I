#from Examen.Simulacro2.Libros import Libro
import Evento as ev
import os
import Auxiliar as aux

lista_eventos = []

class Gestor_Evento:
    def __init__(self):
        pass

    #--------------- ---------------
    def crear_evento(self):

        #Si es el primer evento que cargo creo el archivo en formato w para pisarlo en caso que ya existiese
        if(len(lista_eventos) == 0):
            #Obtengo el path del archivo
            path = os.path.abspath(os.path.dirname(__file__))
            global path_archivo
            path_archivo = path + "\\lista_eventos.txt"
            fichero = open(path_archivo, 'w')
            fichero.close()        

        '''
        lista_eventos.append(ev.Evento("Fiesta", "21/09/2021", "8:00", "Costanera"))
        lista_eventos.append(ev.EventoLaboral("Informe semanal", "11/11/2021", "10:00", "Sala de reuniones", True))
        lista_eventos.append(ev.EventoPersonal("Partido", "17/08/2020", "21:00", "Estadio", "Gustavo"))    
        '''

        while True:
            nombre_evento = input("\nNombre del evento: ").capitalize()
            if(nombre_evento != ""):
                evento_existe = False
                for evento in lista_eventos:
                    if(nombre_evento == evento.nombre):
                        evento_existe = True
                        break
                if(evento_existe):
                    print("\nEse nombre de evento ya existe.")
                else:
                    break

        while True:
            fecha = input("Fecha del evento (formato dd/mm/aaaa): ")
            if(len(fecha) == 10):
                break
        
        hora = input("Hora del evento (formato hh:mm): ")

        lugar = input("Lugar del evento: ")

        while True:
            tipo_evento = input("""
        TIPO DE EVENTO:
        ---------------
        1. Genérico
        2. Personal
        3. Laboral
        Seleccione una opción: """)
            
            if(tipo_evento == "1"):
                lista_eventos.append(ev.Evento(nombre_evento, fecha, hora, lugar))
                tipo_evento = "Generico"
                break
            
            elif(tipo_evento == "2"):
                tipo_evento = "Personal"
                organizador = self.seleccionar_organizador()
                lista_eventos.append(ev.EventoPersonal(nombre_evento, fecha, hora, lugar, organizador))
                break
            
            elif(tipo_evento == "3"):
                
                while True:
                    obligatorio = input("Indique si el evento es obligaotorio (Si/No):").capitalize()
                    tipo_evento = "Laboral"
                    
                    if(obligatorio == "Si"):
                        obligatorio = True
                        break
                    elif(obligatorio == "No"):
                        obligatorio = False
                        break
                    else:
                        print("\nOpción incorrrecta")
                
                lista_eventos.append(ev.EventoLaboral(nombre_evento, fecha, hora, lugar, obligatorio))
                break
            else:
                print("\nTipo de evento NO válido.")
        
        #Grabo en archivo el evento creado
        self.loguear_evento(nombre_evento, fecha, hora, lugar, tipo_evento)
        
    #--------------- ---------------
    def listar_eventos(self):
        #Imprimo la lista de eventos desde el archivo
        if(aux.existe_archivo(path_archivo)):
            #Existe el archivo -> lo abro en modo r
            fichero = open(path_archivo, 'r')
            evento = fichero.read()
            while (evento != ""):
                print(evento)
                evento = fichero.read()

            fichero.close()

    #--------------- ---------------
    def cambiar_lugar_evento(self):
        #Imprimo la lista de eventos para poder ver y seleccionar el correspondiente
        print("""
    EVENTOS AGENDADOS
    -----------------""")
        for evento in lista_eventos:
            evento.info_evento()
        
        evento = self.buscar_evento()
        nuevo_lugar = input("\nIngrese el nuevo lugar del evento: ")
        evento.setear_lugar(nuevo_lugar)        
    
    #--------------- ---------------
    def loguear_evento(self, nombre, fecha, hora, lugar, tipo_evento):      
        #Grabo nombre, fecha, hora, lugar, tipo_evento
        fichero = open(path_archivo, 'a')
        fichero.write(nombre + "-" + fecha + "-" + hora + "-" + lugar + "-" + tipo_evento + "\n")
        fichero.close()
        
    #--------------- ---------------
    def seleccionar_organizador(self):
        organizadores = {
        "FA":"familia", 
        "AM": "amigos",
        "PR": "propio"}
        
        print("""
        ORGANIZADOR
        -----------""")
        
        #Imprimo los organizadores disponibles
        for i in organizadores:
            print(f"\t{i}")

        opcion = input("Seleccione una opción: ").upper()
        
        #Obtengo del diccionario el tipo de evento
        organizador = organizadores.get(opcion,"incognito")
        #print(f"\nORGANIZADOR: {organizador}\n")
        return organizador

    #--------------- ---------------
    def buscar_evento(self):   
        while True:
            nombre_evento = input("\nIngrese el nombre del evento: ")
            #evento_existe = False
            for evento in lista_eventos:
                if(nombre_evento == evento.nombre):
                    #Retorno el objeto para poder cambiar el lugar del evento
                    return evento
            print("\nNo existe un evento con ese nombre.")
        