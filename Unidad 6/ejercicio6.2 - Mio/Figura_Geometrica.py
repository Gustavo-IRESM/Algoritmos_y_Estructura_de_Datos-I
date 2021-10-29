class FiguraGeometrica:
    def __init__(self,tipo_de_figura, color, tamaño="Pequeño"):
        self.tipo_de_figura = tipo_de_figura
        self.color = color
        self.tamaño = tamaño
    
    def presentar_figura(self):
        print(f"Un {self.tipo_de_figura} de color {self.color} y tamaño {self.tamaño}")

    def cambiar_color(self, nuevo_color):
        print(f"Cambio de color {self.color} a {nuevo_color}")
        self.color = nuevo_color

    #def verificar_figura(self, nuevo_tamaño):
    def verificar_figura(self):
        if(self.tamaño == "Pequeño"):
            self.tamaño = "Grande"
            print(f"Cambió el tamaño de Pequeño a {self.tamaño}")
        else:
            print(f"No es necesario cambiar el tamaño, ya es {self.tamaño}")

figura1 = FiguraGeometrica("Triángulo", "Blanco")
print(figura1.tamaño)
figura1.presentar_figura()
figura1.cambiar_color("Rojo")
figura1.presentar_figura()

figura1.verificar_figura()
figura1.verificar_figura()
