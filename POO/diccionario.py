#Diccionario
#Colección que almacena elementos de tipo key,value (clave, valor)
#Tampoco maneja indices, maneja keys

diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

#Largo
print(len(diccionario))

#Acceder a un valor
print(diccionario['IDE'])
print(diccionario.get('IDE'))

# Modificar un valor
diccionario['IDE'] = 'Integrated development environment'

# Iterar diccionario
for termino in diccionario:
    print(termino) #Se iteran las claves

for termino in diccionario:
    print(diccionario[termino]) # Acá accedo a las keys y los values

for valor in diccionario.values():
    print(valor) # Acá accedo sólo a los values

# Identificar si un elemento existe
print('IDE' in diccionario)

# Remover un elemento
diccionario.pop('DBMS')
print(diccionario)

# Limpiar
diccionario.clear()
print(diccionario)

# Del
del diccionario
