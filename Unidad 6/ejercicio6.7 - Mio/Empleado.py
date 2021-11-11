
class Empleado:
    def __init__(self,legajo, nombre, apellido, lista_animales_a_cuidar = []):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.lista_animales_a_cuidar = lista_animales_a_cuidar
    
    def asignar_animales(self,nuevo_animal):
        self.lista_animales_a_cuidar.append(nuevo_animal)
    
    def presentarse(self):
        #print(f"{self.legajo} - {self.nombre} {self.apellido}")
        print(f"Mi número de legajo es {self.legajo}. Me llamo {self.nombre} {self.apellido}", end=". ")
        print(f"Cuido los siguientes animales {self.lista_animales_a_cuidar}")
        #for anim_cuidar in self.lista_animales_a_cuidar:
            #anim_cuidar.presentarse()

    def get_legajo(self):
        return self.legajo