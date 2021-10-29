#Tuplas
frutas = ('Naranja', 'Banana', 'Frutilla')

#Largo
print(len(frutas))

#Acceder a un elemento
print(frutas[0])

#Navegación inversa
print(frutas[-1])

#Rango
print(frutas[0:2])

#Modificar el valor de una tupla
#frutas[0] = 'Naranjita' - No se puede
frutasLista = list(frutas) # parsear (convertir) la tupla en una lista
frutasLista[0] = 'Naranjita'
frutas = tuple(frutasLista)
print(frutas)

# Iteración ciclo for
for fruta in frutas:
    print(fruta)

# Eliminar un elemento de la tupla? No se puede hacer
del frutas
