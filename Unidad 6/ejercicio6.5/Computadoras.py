"""
Crear una clase padre Computadoras:
*   Constructor debe incluir los atributos (id_modelo,listaPerifericos,SO)
*   Crear metodos para esta clase de:
    1.  Presentarse (id_modelo,listaPerifericos,SO)
    2.  Indicar tipo de Computadora (Clases heredadas)
    3.  Metodos que luego modificarán las clases hijas. agregar_perifericos,CambiarSO

Crear 2 clases que hereden de la clase padre Computadoras, con un atributo en particular para cada una
1.   Escritorio
2.   Notebbok
"""
class Computadora:
    #CONSTRUCTOR
    def __init__(self,id_modelo,listaPerifericos,SO):
        self.id_modelo = id_modelo
        self.listaPerifericos= listaPerifericos
        self.SO = SO
 
    def presentarse(self):
        print(f"""Computadora con id {self.id_modelo} de la lista {self.listaPerifericos} y con Sistema Operativo {self.SO}""")
 
    def tipo_computadora(self):
        print ("Computadora tipo: ", type(self).__name__)
 
    def agregar_perifericos(self):
        pass
 
    def CambiarSO(self):
        pass
 
class ComputadoraEscritorio(Computadora):
    def __init__(self,id_modelo,listaPerifericos,SO, marca = "Samsung"):
        super().__init__(id_modelo,listaPerifericos,SO)
        self.marca = marca
 
    def agregar_perifericos(self,nuevo_periferico):
        print (f"Los periféricos que tiene la Computadora de Escritorio son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)

 
    def CambiarSO(self,nuevo_SO):
        print (f"El SO de la computadora Escritorio era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO
 
 
 
class ComputadoraNotebook(Computadora):
    def __init__(self,id_modelo,listaPerifericos,SO, marca = "LG"):
        super().__init__(id_modelo,listaPerifericos,SO)
        self.marca = marca
 
    def agregar_perifericos(self,nuevo_periferico):
        print (f"Los periféricos que tiene la Computadora de Escritorio son {self.listaPerifericos}")
        self.listaPerifericos.append(nuevo_periferico)

 
    def CambiarSO(self,nuevo_SO):
        print (f"El SO de la computadora Notebook era {self.SO} y ahora es {nuevo_SO}")
        self.SO = nuevo_SO
