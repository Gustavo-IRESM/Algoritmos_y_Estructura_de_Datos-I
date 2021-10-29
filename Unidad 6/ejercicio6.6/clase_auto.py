'''
- Contar con 6 funciones disponibles en el menu **(estas funciones deben estar incluidas en una clase llamada GestorTaxis)**:
    - 1. Crear instancias de choferes y guardarlos en una lista de choferes
    - 2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
    - 3. Modificar el chofer de un auto
    - 4. Modificar el lugar de residencia del chofer indicando su nombre
    - 5. imprmir lista de choferes (con toda su informacion)
    - 6. imprimir lista de autos (con toda su informacions)
- Se deben crear los metodos correspondientes para las funciones del menu en las clases correspondientes
- Gestionar posibles errores
- Estructurar el programa a criterio propio
'''


class Auto:
    def __init__(self,patente, modelo, año, marca, nombre_chofer):
        self.patente = patente
        self.modelo = modelo
        self.año = año
        self.marca = marca
        self.nombre_chofer = nombre_chofer
        
    def get_patente(self):
        return self.patente

    def get_chofer(self):
        return self.nombre_chofer

    def set_chofer(self, nuevo_nombre):
        self.nombre_chofer = nuevo_nombre

    def imprimir_info(self):
        print(f"Patente: {self.patente} - Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.año} - Nombre chofer: {self.nombre_chofer}")


