'''
Crear una funcion que debe: (usar diccionario)
    - Contener un diccionario con distintas monedas de paises, siendo la key el nombre de la moneda y el valor el simbolo.
    - Preguntar al usuario que tipo de moneda desea y mostrar el simbolo si existe en el diccionario, caso contrario indicar que no existe.
'''
monedas = {
    "Peso":"$", 
    "Dolar": "USD",
    "Euro":  "€"
    }

def obtener_simbolo():
  moneda = input("Ingrese que tipo de moneda desea saber el simbolo: ").capitalize()
  print(moneda)
  if moneda in monedas:
    print(f"El simbolo de {moneda} es {monedas[moneda]}")
  else:
    print("La moneda no existe en el diccionario")

def obtener_simbolo_2():
  moneda = input("Ingrese que tipo de moneda desea saber el simbolo: ").capitalize()
  valor = monedas.get(moneda,"No existe")
  print(f"El simbolo de {moneda} : {valor}")

obtener_simbolo()
obtener_simbolo_2()