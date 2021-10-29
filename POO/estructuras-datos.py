# Colecciones de Datos

# Listas, Tuplas y Diccionarios

# Listas (Array o Vectores)

l = [2, 'Verdadero', True, ['uno', False], 10]
print(l[1])

#Acceder a un indice en memoria de la lista
l2 = l[1]
print(l2)
l2 = l[3][0]
print(l2)
l[1] = 3
print(l)

# Slizing
l3 = l[0:3]
print(l3)
l4 = l[0:3:2]
print(l4)
l5 = l[0::2]
print(l5)
l[0:2] = [4, 3]
print(l)
print(l[-1])

print('------------------------------------')

# Tuplas
t = 1, True, 'Hola'
print(t)
t2 = (2, False, 'Chau')
print(t2)
print(t[1])
# Las tuplas son inmutables
#t[1] = 'jaja'
#print(t)

