class Libro:
    #Constructor
    def __init__(self, Id, nombre, autor, estado = "No alquilado"):
        self.Id = Id
        self.nombre = nombre
        self.autor = autor
        self.estado = estado

    def presentarse(self):
        #Imprimo los datos del libro
        self.tipo_libro()
        print(f" - Id: {self.Id} - Nombre: {self.nombre} - Autor: {self.autor}, Estado: {self.estado}")

    def tipo_libro(self):
        #Muestro la clase de libro
        print(f"Tipo libro: {type(self).__name__}",end="")

    def alquilar(self):
        self.estado = "ALQUILADO"

    def devolver(self):
        self.estado = "No alquilado"

#--------------- ---------------
class Libro_Niños(Libro):
    #Constructor
    def __init__(self, Id, nombre, autor, estado = "No alquilado", edad_minima = 11):
        super().__init__(Id, nombre, autor, estado)
        self.edad_minima = edad_minima
    
    def presentarse(self):
        #Imprimo los datos del libro
        self.tipo_libro()
        print(f" - Id: {self.Id} - Nombre: {self.nombre} - Autor: {self.autor} - Estado: {self.estado} - Edad mínima: {self.edad_minima}")

#--------------- ---------------
class Libro_Idiomas(Libro):
    #Constructor
    def __init__(self, Id, nombre, autor, estado="No alquilado", idioma_libro="Español"):
        super().__init__(Id, nombre, autor, estado)
        self.idioma_libro = idioma_libro

    def presentarse(self):
        #Imprimo los datos del libro
        self.tipo_libro()
        print(f" - Id: {self.Id} - Nombre: {self.nombre} - Autor: {self.autor} - Estado: {self.estado} - Idioma: {self.idioma_libro}")
