"""
*   Se debe crear una clase GestorEvento que cuente con las siguientes funciones para un menu:

    1.  Crear instancias de un evento y guárdalos en una lista de eventos. 
        1.1) Se debe verificar que tipo de instancia de evento a crear y los parámetros. IMPORTANTE!: clase hijas verificar y pedir parámetros
             - nombre_evento: debe ser único
             - Fecha: formato (dd/mm/yyyy) -> únicamente verificar la longitud del string = 10 
             - Hora: formato (hh:mm) -> no es necesario verificar
             - Lugar: sin formato especifico, no es necesario verificar
        1.2) Al crear un evento es necesario logearlo (Escribir en una línea nueva: nombre_evento-Fecha-Hora-Lugar-Tipo_de_evento(tipo de clase)) 
             en un archivo llamado lista_eventos.txt (Crear función en el mismo gestor). IMPORTANTE!: verificar permisos
        1.3) En caso que la instancia del evento sea EventoPersonal.
             - Para el organizador, el usuario debe elegir a través de una clave (mostradas por el programa) 
                desde un diccionario de organizadores.
             - En caso que no exista el organizador deseado debe ser "incognito" (AYUDA: Funcion get de diccionarios)
    2.   Listar eventos disponibles, leyendo la lista_evetos.txt. IMPORTANTE!: recorrer el archivo, no la lista. 
    3.   Cambiar el lugar de un evento, seleccionando su nombre. (Hacer check correspondientes)
    """
import Clases as cl
import os
organizadores = {
    "FA": "familia", 
    "AM": "amigos",
    "PR": "propio"
    }
lista_eventos = []
class GestorEvento:
    def instanciar_eventos(self):
        while True:
            instancia = input("""Ingrese la instancia que desea crear:
                             1. Evento comun
                             2. Evento Laboral
                             3. Evento personal""")
            
            if(instancia == "1" or instancia == "2" or instancia == "3"):
                break
            else:
                print("Opcion incorrecta!")
        #Nombre del evento
        existe = True
        while True:
            nombre_evento = input("ingrese el nombre: ")
            for i in lista_eventos:
                if(nombre_evento == i.get_nombre()):
                    print("ese nombre ya existe!")
                    existe = False
                    break
            if(existe):
                break
        #verificar la fecha
        while True:
            fecha = input("ingrese la fecha: ")
            if (len(fecha)==10):
                break
            else:
                print("Mal formato")
                
        hora = input("ingrese la hora: ")
        lugar = input("ingrese el lugar: ")
        
        if(instancia =="1"):
            evento = cl.Evento(nombre_evento,fecha,hora,lugar)
            lista_eventos.append(evento)
            self.loogear(nombre_evento,fecha,hora,lugar,evento.tipo_evento)
        elif(instancia =="2"):
            while True:
                obligatorio = input("""ingrese si el evento es obligatrio o no:
                                1. True
                                2. False""")
                if(obligatorio=="1"  or obligatorio =="2"):
                    break
                else:
                    print("incorrecto")
            if(obligatorio=="1"):
                obligatorio = True
            else:
                obligatorio = False
            
            evento =cl.EventoLaboral(nombre_evento,fecha,hora,lugar,obligatorio)
            lista_eventos.append(evento)
            self.loogear(nombre_evento,fecha,hora,lugar,evento.tipo_evento)
        elif(instancia =="3"):
            print("Posibles organizadores")
            for i in organizadores:
                print(i)
            clave = input("ingrese la clave: ").upper()
            organizador = organizadores.get(clave,"incognito")
            evento =cl.EventoPersonal(nombre_evento,fecha,hora,lugar,organizador)
            lista_eventos.append(evento)
            self.loogear(nombre_evento,fecha,hora,lugar,evento.tipo_evento)

    def loogear(self,nombre_evento,fecha,hora,lugar,tipo_evento):
        
        path = os.path.abspath(os.path.dirname(__file__))
        path_archivo = path+"\\lista_eventos.txt"
        try:
            fichero = open(path_archivo, 'a+')
            fichero.write(f"Nombre del evento: {nombre_evento}, Fecha: {fecha}, Hora: {hora}, Lugar: {lugar}, Tipo: {tipo_evento}) \n")
            fichero.close()
        except:
            print("ERROR.")
    
    def leer_archivo(self):
        path = os.path.abspath(os.path.dirname(__file__))
        path_archivo = path+"\\lista_eventos.txt"
        try:
            archivo = open(path_archivo,'r')
            while True:
                linea = archivo.readline()
                if (linea == ""):
                    break
                print(linea,end="")
            archivo.close()
        except:
            print("error")
    
    def cambiar_lugar(self):
        for i in lista_eventos:
            print(i.mostrar_info())
        existe = False
        while True:
            evento = input("Que evento quiere cambiar de lugar? indique el nombre: ")
            for i in lista_eventos:
                if(evento == i.get_nombre()):
                    nuevo_lugar = input("ingrese el nuevo lugar")
                    i.set_lugar(nuevo_lugar)
                    existe = True
                    break
            if(existe):
                break