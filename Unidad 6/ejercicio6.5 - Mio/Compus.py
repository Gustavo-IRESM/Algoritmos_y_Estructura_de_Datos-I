
class Compus:
    def __init__(self,id,listaPerifericos,SO):
        self.id = id
        self.listaPerifericos = listaPerifericos
        self.SO = SO

    def presentarse(self):
        print(f"""Computadora con id {self.id + 1} incluye los periféricos {self.listaPerifericos} y con Sistema Operativo {self.SO}""")
    
    def tipo_compu(self):
        print ("Computadora tipo:", type(self).__name__)

    def agregar_periferico(self,nuevo_periferico):
        print (f"Los periféricos que tiene la Computadora Genérica son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)

    def cambiar_so(self, nuevo_SO):
        print (f"El SO de la computadora Genérica era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO

#--------------- ---------------
class Escritorio(Compus):
    def __init__(self,id,listaPerifericos,SO,marca):
        super().__init__(id,listaPerifericos,SO)
        self.marca = marca

    def agregar_perifericos(self,nuevo_periferico):
        print (f"Los periféricos que tiene la Computadora de Escritorio son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)

    def cambiar_so(self,nuevo_SO):
        print (f"El SO de la computadora Escritorio era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO
    

#--------------- ---------------
class Notebook(Compus):
    def __init__(self,id,listaPerifericos,SO,marca):
        super().__init__(id,listaPerifericos,SO)
        self.marca = marca

    def agregar_perifericos(self,nuevo_periferico):
        print (f"Los periféricos que tiene la Notebook son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)


    def cambiar_so(self,nuevo_SO):
        print (f"El SO de la Notebook era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO
            