'''
- Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorTaxis)**:
    - 1. Crear instancias de choferes y guardarlos en una lista de choferes
    - 4. Modificar el lugar de residencia del chofer indicando su nombre
    - 5. imprmir lista de choferes (con toda su informacion)
- Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
'''

class Chofer:
    def __init__(self,nombre, apellido, dni, fecha_nacimiento, residencia):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.residencia = residencia
        
    def get_dni(self):
        return self.dni

    def get_nombre(self):
        self.nombre
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_residencia(self, nueva_residencia):
        self.residencia = nueva_residencia

    def imprimir_info(self):
        print(f"Nombre: {self.get_nombre()} - Apellido: {self.apellido} - DNI: {self.dni} - Fecha nacimiento: {self.fecha_nacimiento} - Residencia: {self.residencia}")