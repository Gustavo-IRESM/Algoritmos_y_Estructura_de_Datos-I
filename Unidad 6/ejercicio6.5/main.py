import Computadoras as cp

lista = []
pc_1 = cp.Computadora("123",["teclado","mouse"],"Linux")
pc_2 = cp.ComputadoraEscritorio("126",["teclado","mouse"],"Windows")
pc_3 = cp.ComputadoraNotebook("124",["teclado","mouse"],"Ubuntu")
lista.append(pc_1)
lista.append(pc_2)
lista.append(pc_3)

for i in lista:
    i.presentarse()
    i.tipo_computadora()