class Evento:
    #Constructor
    def __init__(self, nombre, fecha, hora, lugar):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar

    #No uso esta función. La creo porque se pide en el enunciado
    def setear_fecha_hora(self, fecha, hora):
        self.fecha = fecha
        self.hora = hora

    def setear_lugar(self,lugar):
        self.lugar = lugar

    def info_evento(self):
        #Muestro los datos del evento
        tipo_evento = self.tipo_evento()
        print(f"Tipo de evento: {tipo_evento} - Nombre: {self.nombre} - Fecha y hora: {self.fecha} - {self.hora} - Lugar: {self.lugar}")

    def tipo_evento(self):
        #Devuelvo el tipo de evento
        return type(self).__name__

#--------------- ---------------
class EventoPersonal(Evento):
    #Constructor
    def __init__(self, nombre, fecha, hora, lugar, organizador):
        super().__init__(nombre, fecha, hora, lugar)
        self.organizador = organizador
    
    def info_evento(self):
        #Imprimo los datos del evento personal
        tipo_evento = self.tipo_evento()
        print(f"Tipo de evento: {tipo_evento} - Nombre: {self.nombre} - Fecha y hora: {self.fecha} - {self.hora} - Lugar: {self.lugar} - Organizador: {self.organizador}")

#--------------- ---------------
class EventoLaboral(Evento):
    #Constructor
    def __init__(self, nombre, fecha, hora, lugar, obligatorio = True):
        super().__init__(nombre, fecha, hora, lugar)
        self.obligatorio = obligatorio

    def info_evento(self):
        #Imprimo los datos del evento laboral
        tipo_evento = self.tipo_evento()
        print(f"Tipo de evento: {tipo_evento} - Nombre: {self.nombre} - Fecha y hora: {self.fecha} {self.hora} - Lugar: {self.lugar} - Obligatorio: {self.obligatorio}")
