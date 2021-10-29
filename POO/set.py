#Set
'''
A diferencia de Listas y Tuplas, no tienen ningún order,
y los elementos son únicos, no se pueden duplicar.
No se pueden modificar tampoco.
Si se pueden agregar o remover elementos.
'''

planetas = {'Marte', 'Venus', 'Jupiter'}
print(planetas)

#Largo
print(len(planetas))

# Verificar si un elemento existe dentro del set
print('Marte' in planetas)

# Agregar
planetas.add('Tierra')
planetas.add('Tierra') #No arroja error, pero lo agrega una única vez
print(planetas)

# Se puede iterar con el ciclo FOR
for planeta in planetas:
    print(planeta)

# Eliminar
planetas.remove('Tierra')
#planetas.remove('Tierras') - Devuelve una exception
print(planetas)

planetas.discard('Jupiter')
planetas.discard('Jupiters') # - No devuelve una exception
print(planetas)

# Limpiar
planetas.clear()
print(planetas)

# Palabra reservada
del planetas