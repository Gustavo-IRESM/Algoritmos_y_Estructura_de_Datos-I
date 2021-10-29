#https://www.codigopiton.com/variables-locales-y-globales-en-python/

def saludar():
    global saludo
    print(saludo)
    saludo = "variable local"

saludo = "variable global"
saludar()
print(saludo)
