def abc():
	
	lista= []
	abcde= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',  'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	while True:
		try:
			numero= int(input("Ingrese un numero 2 o 3: "))
			if numero>=2 and numero<=3:
				break
			else:
					print("dato fuera de rango")			
		except:
			print("dato erroneo")
	if numero== 2:		
		for i in range(len(abcde)):
			if i % numero == 0:
				lista.append(i-1)
		lista.pop(0)
		print(lista)
		lista.reverse()
		for i in (lista):
			abcde.pop(i)
			
		print(f"el abecedario sin los multiplos de 2 son:\n{abcde}")
		
	if numero== 3:		
		for i in range(len(abcde)):
			if i % numero == 0:
				lista.append(i+2)
		print(lista)
		lista.reverse()
		for i in (lista):
			abcde.pop(i)
			
		print(f"el abecedario sin los multiplos de 3 son:\n{abcde}")
	
			

abc()			