"""
###**Ejercicio 6.4**
Crear una clase padre Vehiculos:
+   Constructor debe incluir los atributos (patente,marca,año,origen)
-   Crear metodos para esta clase de:
    + 1.  Presentarse (patente,marca,año,origen)
    2 2.  Indicar tipos de vehiculo(Clases heredadas)
    - 3.  Metodos que luego modificarán las clases hijas. 
        - Acelerar
        - Retroceder
        - Obtener_velocidad_max
        - Setear_velocidad_max
"""
class Vehiculo:
    def __init__(self,patente,marca,año,origen):
        self.patente = patente
        self.marca = marca
        self.año = año
        self.origen = origen
    
    def presentarse(self):
        #print(f"Soy un vehiculo con patente {self.patente}, marca {self.marca}, del año {self.año} y origen {self.origen}")
        self.tipo_vehiculo()
        print(f", con patente {self.patente}, marca {self.marca}, del año {self.año}, origen {self.origen}")
        
    def tipo_vehiculo(self):
        print(f"Soy un vehículo tipo {type(self).__name__}",end="")

    #def acelerar(self):
        #pass

    #def retroceder(self):
        #pass

    #def obtener_velocidad_max(self):
        #pass

    #def setear_velocidad_max(self):
        #pass

#--------------- ---------------
class Vehiculo_Particular(Vehiculo):
    def __init__(self, patente, marca, ano, origen, velocidad_max = 130): #Velocidad por defecto
        super().__init__(patente, marca, ano, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Acelerar VP")
 
    def retroceder(self):
        print("Retroceder VP")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}")
        self.velocidad_max = velocidad_max_nueva
 

#--------------- ---------------
class Vehiculo_PickUp(Vehiculo):
    def __init__(self, patente, marca, ano, origen, velocidad_max = 100): #Velocidad por defecto
        super().__init__(patente, marca, ano, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Acelerar VPU")
 
    def retroceder(self):
        print("Retroceder VPU")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}")
        self.velocidad_max = velocidad_max_nueva
 

#--------------- ---------------
class Vehiculo_Deportivo(Vehiculo):
    def __init__(self, patente, marca, ano, origen, velocidad_max = 200): #Velocidad por defecto
        super().__init__(patente, marca, ano, origen)
        self.velocidad_max = velocidad_max
 
    def acelerar(self):
        print("Acelerar VD")
 
    def retroceder(self):
        print("Retroceder VD")
 
    def obtener_velocidad_max(self):
        print(f"La velocidad maxima es {self.velocidad_max}")
 
    def setear_velocidad_max(self, velocidad_max_nueva):
        print (f"La velocidad maxima era {self.velocidad_max} y ahora es {velocidad_max_nueva}")
        self.velocidad_max = velocidad_max_nueva
 
