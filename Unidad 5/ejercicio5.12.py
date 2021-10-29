'''
Crear una funcion que debe: (usar diccionario)
    - Preguntar al usuario su nombre, edad, dirección y teléfono y lo guardar en un diccionario.
    - Mostrar por pantalla el mensaje: "nombre" tiene "edad" años, vive en "direccion" y su número de teléfono es "telefono".
'''
datos_persona = {}
def datos_de_persona():
  nombre = input("Por favor ingrese el nombre: ").capitalize()
  datos_persona.update({"Nombre":nombre})
  while True:
    try:
      edad = int(input("Por favor ingrese su edad: "))
      datos_persona.update({"Edad":edad})
      break
    except:
      print("Error de datos")
  
  #Si entramos la dirección con la altura da error el .capitalize()
  direccion = input("Por favor su direccion: ").capitalize()
  datos_persona.update({"Dirección":direccion})

  while True:
    try:
      telefono = int(input("Por favor ingrese su telefono ej(351123456): "))
      datos_persona.update({"Telefono":telefono})
      break
    except:
      print("Error de datos")

  print(datos_persona)
  print(f"{datos_persona.get('Nombre')} tiene {datos_persona.get('Edad')} vive en {datos_persona.get('Direccion')} su telefono es {datos_persona.get('Telefono')}")

datos_de_persona()