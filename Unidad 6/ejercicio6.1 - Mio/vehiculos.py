class vehiculo:
    def __init__(self, marca="", tipo="auto", combustible="nafta", velmax=0, kilometraje=0):
        self.marca = marca
        self.tipo = tipo
        self.combustible = combustible
        self.velmax = velmax
        self.kilometraje = kilometraje

    def datos_vehiculo(self):
        print(f"\t{self.marca} \t\t {self.tipo} \t\t {self.combustible} \t\t {self.velmax} \t\t {self.kilometraje}")

    def ver_mantenimiento(self):
        flag_mantenimiento = False
        if(self.tipo == "Moto"):
            if(self.kilometraje > 20000):
                flag_mantenimiento = True
        if(self.tipo == "Auto"):
            if(self.kilometraje > 60000):
                flag_mantenimiento = True
        if(self.tipo == "Camión"):
            if(self.kilometraje > 100000):
                flag_mantenimiento = True
        
        print(f"Al vehículo tipo {self.tipo} marca {self.marca} con {self.kilometraje}", end=" ")
        if(flag_mantenimiento):
            print("corresponde hacerle mantenimiento")
        else:
            print("NO corresponde hacerle mantenimiento")

