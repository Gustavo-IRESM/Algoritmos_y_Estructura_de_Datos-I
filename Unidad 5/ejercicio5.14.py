'''
Crear una funcion que debe: (usar diccionario)
    - Crear un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
    - Pida al usuario el dato a agregar (key) y el valor
    - Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

personas={}
def agregar_informacion():
  while True:
    key = input("Ingrese la informacion que registrara o salir (para abandonar el programa): ")
    if key =="salir":
      break
    if key in personas:
      print("Ya existe el valor, ingrese uno diferente!!")
    else:
      valor = input(f"Por favor ingrese el valor de {key}: ")
      personas.setdefault(key,valor)
      print(personas)

def imprimir_diccionario(nombre,diccionario):
    print("Función imprimir_diccionario()")
    print(f"--------{nombre}--------")
    print(f"--key\tValor--")
    for i in diccionario:
        print(f"  {i}\t{diccionario.get(i)}")

def imprimir_diccionario2(nombre,diccionario):
    print("Función imprimir_diccionario2()")
    print(f"--------{nombre}--------")
    print(f"--key\tValor--")
    for i,j in diccionario.items(): #i trae los key (tupla) j trae los valores (tupla)
        print(f"  {i}\t{j}")


agregar_informacion()
imprimir_diccionario("Datos de la persona",personas)
imprimir_diccionario2("Datos de la persona",personas)
  