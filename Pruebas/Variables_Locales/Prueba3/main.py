import variables_globales as vg
import archivo1 as a1

print(vg.saludo)
vg.saludo = "HOLA mundo..!!\n"
a1.imprimir()

print("Imprimiendo desde main")
print(vg.saludo)
