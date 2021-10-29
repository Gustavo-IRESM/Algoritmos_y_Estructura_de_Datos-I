"""
*   La Clase Animales tiene los atributos (nombre, tipo_animal, fecha_nacimiento, encargado_cuidar (Nombre de objeto empleado))
    *   Crear 3 clases que hereden de animal segun su sector del zoologico)
        1. AnimalesEnjaulados.
        2. AnimalesSueltos.
        3. AnimalesAcuaticos
"""

class Animal:
    def __init__(self, nombre, tipo_animal, fecha_nacimiento, encargado_cuidar):
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.encargado_cuidar = encargado_cuidar

    def tipo_animal():
        print("Soy un animal tipo ", type(self).__name__)
        
#--------------- ---------------
class AnimalesEnjaulados(Animal):
    pass

class AnimalesSueltos(Animal):
    pass

class AnimalesAcuaticos(Animal):
    pass

animal = Animal("animal1","felino","1/1/2010","Pedro")
animal_marino = AnimalesAcuaticos("animal2","felino","9/1/2010","Pedro")
animal_jaula = AnimalesEnjaulados("animal3","felino","1/1/2010","Pedro")
animal_suelto = AnimalesSueltos("animal4","felino","1/1/2010","Pedro")



