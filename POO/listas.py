# Lista

nombres = ['Juan', 'Karla', 'Ricardo', 'María']
#Conocer el largo
print(len(nombres))

#Acceder a un elemento
print(nombres[0])

#Navegación inversa
print(nombres[-1])

#Imprimir un rango (Slyzing)
print(nombres[0:2])#Sin incluir el 2

#Omitir el primer indice
print(nombres[:2])

#Omitir el segundo indice
print(nombres[1:])

#Cambiar los elementos de una lista
nombres[3] = 'Cintia'
print(nombres)

#Iterar la lista con ciclo FOR
print("Iterar la lista con ciclo FOR")
for nombre in nombres:
    print(nombre, end=' ')

#Revisar si un elemento existe
if 'Cintia' in nombres:
    print('\nCintia si existe en la lista')
else:
    print('\nCintia no existe en la lista')

# Agregar un nuevo elemento
nombres.append('Lorenzo')
print(nombres)

# Agregar un elemento en un indice especifico
nombres.insert(1, 'Octavio')
print(nombres)

# Remove un elemento
nombres.remove('Octavio')
print(nombres)

# Método pop - remover el último
nombres.pop()
print(nombres)

# Palabra reservada del
print("Delete")
del nombres[0]

#del nombres - Elimina la variable de memoria
print(nombres)

# Método clear
nombres.clear()
print(nombres)
