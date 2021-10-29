#https://python-para-impacientes.blogspot.com/2014/02/variables-locales-y-variables-globales.html


# Define función
def acelerar():
    # Declara la variable 'km' como global
    # Ahora se podrá utilizar dentro de la función
    global km
    
    # Declara variable local (ámbito función)
    tiempo = 1

    # Se incrementa la velocidad en 5 km
    km+= 5

# Define variable local (ámbito programa principal)
km = 10

# Muestra variable 'km'
print('Velocidad:', km)  # velocidad: 10

# Llama a la función acelerar()
acelerar()

# Muestra variable 'km'
print('Velocidad:', km)  # velocidad: 15

# Intenta mostrar la variable 'tiempo'
# Se produce una excepción (error) de tipo NameError
# porque la variable no pertenece a este ámbito:
# NameError: name 'tiempo' is not defined
#print('Tiempo:', tiempo)