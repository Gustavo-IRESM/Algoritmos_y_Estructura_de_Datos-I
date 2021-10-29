'''
Crear una funcion que debe: (usar diccionario)
    - Guardar en un diccionario los precios de las frutas de la tabla.
    - Preguntar al usuario por una fruta, un número de kilos y mostrar por pantalla el precio de ese número de kilos de fruta.
    - Si la fruta no está en el diccionario debe mostrar un mensaje informando ERROR.
                    Fruta	Precio
                    -----   ------
                    banana	    50
                    manzana	    80
                    pera	   100
                    naranja	    30
'''

stock_frutas = {
    "banana" : 50,
    "manzana" : 80,
    "pera" : 100,
    "naranja" : 30
}

def precio_final(stock_frutas):
    fruta = input("Ingrese la fruta a comprar: ").casefold()
    valor = stock_frutas.get(fruta,'La fruta no está en el stock')
    while True:
        if valor == "La fruta no está en el stock":
            print(valor)
            break
        else: 
            try:
                kilos = int(input("Ingrese la cantidad de Kilos a comprar: "))
                precio = valor*kilos
                print(f"{kilos} kilos de {fruta} es: {precio}")
                break
            except:
                print("Reintentar, valor erroneo.")

precio_final(stock_frutas)