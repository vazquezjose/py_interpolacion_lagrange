'''
*	Método de interpolación de Lagrange
*	Autor: José Isaías Vázquez Macías
'''

'''
*	Descripción:
*	Función para validar que una cadena pueda representar un número real
*	
*	Parámetros:
*	- "string" : la cadena a analizar
*	
*	Valor de retorno:
*	Booleano : validez de la cadena como número real
'''
def isFloat(string):
	validChars = ".-0123456789" # caracteres válidos en un número real
	slashFound = False	# variable para registrar si se halló algún guión en la cadena
	dotFound = False	# variable para registrar si se halló algún punto en la cadena
	
	if len(string) > 0: # si el tamaño de la cadena es mayor a 0...
		if '-' in string and string[0] != '-':	# si la cadena contiene un guión, pero dicho guión no se ubica como el primer caracter...
			return False	# la cadena no es un número real válido
		else:	# sino...
			for c in string:	# iterando en cada caracter de la cadena
				if c not in validChars: # si el caracter iterado no se encuentra en los caracteres validos...
					return False	# la cadena no es un número real válido
				
				if c == '-':	# si el caracter iterado es un guión...
					if not slashFound:	# si aún no se ha hallado algún guión...
						slashFound = True	# registrar que ya hay un guión en la cadena
					else:	# sino...
						return False	# la cadena no es un número real válido
				if c == '.':	# si el caracter iterado es un punto...
					if not dotFound:	# si aún no hay registro de algún punto...
						dotFound = True # registrar que ya hay un punto en la cadena
					else:	# sino...
						return False	# la cadena no es un número real valido
	else:	# sino...
		return False	# la cadena no es un número real válido
	return True # si a pesar de las trabas llega a este punto, es un número real válido

'''
*	Descripción:
*	Función para validar que una cadena pueda representar un número entero
*	
*	Parámetros:
*	- "string" : la cadena a analizar
*	- "forcePositive" : especifica si la cadena analizada debe ser, a parte de entero, un número positivo
*	
*	Valor de retorno:
*	Booleano : validez de la cadena como número entero (y positivo si requerido)
'''
def isInt(string, forcePositive):
	validChars = "-0123456789"	# caracteres válidos en un número entero
	slashFound = False	# variable para registrar si se halló algún guión en la cadena
	if len(string) > 0: # si el tamaño de la cadena es mayor a 0...
		for c in string:	# iterando en cada caracter de la cadena
			if c not in validChars: # si el caracter iterado no se encuentra en los caracteres validos...
				return False	# la cadena no es un número real válido
			
			if c == '-':	# si el caracter iterado es un guión...
				if not forcePositive:	# si el entero no debe ser un positivo forzosamente...
					if not slashFound and len(string) >= 2: # si aún no se ha hallado un guión y el tamaño de la cadena es mayor o igual a 2...
						slashFound = True	# registrar que ya hay un guión en la cadena
					else:	# sino...
						return False	# la cadena no es un número entero válido
				else:	# sino...
					return False	# la cadena no es un número entero positivo válido
	else:	# sino...
		return False	# la cadena no es un número entero válido
	return True # si a pesar de las trabas llega a este punto, es un número entero válido

'''
*	Descripción:
*	Función para calcular cada miembro i que será sumado en el resultado final.
*	
*	Parámetros:
*	- "xValues" : la lista de valores de x
*	- "yValues" : la lista de valores de y
*	- "i" : el número de miembro
*	- "desiredFunctionValue" : el x de y(x) deseado en el resultado final
*	
*	Valor de retorno:
*	Valor del miembro i, obtenido por una división. Es un sumando del resultado final.
'''
def calculateMember(xValues, yValues, i, desiredFunctionValue):
	dividend = yValues[i]	# el dividendo inicia con el valor actual de y
	remainingXValues = xValues.copy()	# clonamos la lista para tener una modificable
	remainingXValues.pop(i)	# usamos pop para eliminar el valor de x del miembro actual
	
	for value in remainingXValues:	# para cada valor de x restante en la lista despues del pop...
		dividend *= (desiredFunctionValue - value)	# restarlo del x de y(x) y multiplicarlo por el valor actual del dividendo
	
	divider = 1	# el divisor inicia con valor de 1 para poder ser multiplicado despues
	
	for value in remainingXValues:	# para cada valor de x restante en la lista despues del pop...
		divider *= (xValues[i] - value)	# restarlo del valor actual de x y multiplicarlo por el divisor
	
	return dividend / divider	# divide

'''
*	Descripción:
*	Función principal. Pide el ingreso de los datos y manda llamar a todas las demás.
*	
*	Parámetros:
*	No tiene.
*	
*	Valor de retorno:
*	No tiene.
'''
def main():
	infoInput = None	# variable temporal que almacena la información ingresada por el usuario
	
	keepAskingAmountOfValues = True	# variable temporal usada para saber si la información ingresada fue correcta
	amountOfValues = 0	# almacena la cantidad de valores. Es reemplazado por la info. ingresada
	
	while keepAskingAmountOfValues:	# ciclo controlador del ingreso de la cantidad de valores
		infoInput = input("Ingrese la cantidad de valores (numero entero mayor a 2): ")
		
		if isInt(infoInput, True):	# si la información ingresada es un entero positivo...
			amountOfValues = int(infoInput)	# asignar la información ingresada a la cantidad de valores
			
			if amountOfValues > 2:	# si la cantidad de valores es válido (mayor a 2)...
				keepAskingAmountOfValues = False	# salir del ciclo
			else:	# sino...
				print("- La cantidad de valores debe ser mayor a 2.")
		else:	# sino...
			print("- La informacion introducida no es un numero entero mayor a 2.")
			
	xValues = list()	# lista donde se almacenarán los valores de x
	for i in range(1, amountOfValues+1):	# ciclo controlador del ingreso de los valores de x
		keepAskingValue = True	# variable temporal usada para saber si la información ingresada fue correcta
		value = 0	# variable temporal para almacenar el candidado a valor de x
		
		while keepAskingValue:	# ciclo controlador del ingreso de informacion correcta
			infoInput = input(f"Ingrese el valor numero {i} de x: ")
			
			if isFloat(infoInput):	# si los caracteres ingresados cumplen los requisitos para poder convertirlo en un número real...
				value = float(infoInput)	# convertirlo en un número real
				
				if value in xValues:	# si el número introducido ya ha sido introducido con anterioridad...
					print("- El valor introducido es repetido. Debe ser unico. Introduzca uno valido.")
				else:	# sino...
					keepAskingValue = False # salir del ciclo
			else:	# sino...
				print("- La informacion introducida no es un valor valido.")
		xValues.append(value)	# agregar el valor de x a la lista
	
	yValues = list()	# lista donde se almacenarán los valores de y
	for i in range(1, amountOfValues+1):	# ciclo controlador del ingreso de los valores de y
		keepAskingValue = True	# variable temporal usada para saber si la información ingresada fue correcta
		value = 0	# variable temporal para almacenar el candidado a valor de y
		
		while keepAskingValue:	# ciclo controlador del ingreso de informacion correcta
			infoInput = input(f"Ingrese el valor numero {i} de y: ")
			
			if isFloat(infoInput):	# si los caracteres ingresados cumplen los requisitos para poder convertirlo en un número real...
				value = float(infoInput)	# convertirlo en un número real
				
				if value in yValues:	# si el número introducido ya ha sido introducido con anterioridad...
					print("- El valor introducido es repetido. Debe ser unico. Introduzca uno valido.")
				else:	# sino...
					keepAskingValue = False # salir del ciclo
			else:	# sino...
				print("- La informacion introducida no es un valor valido.")
		yValues.append(value)	# agregar el valor de y a la lista
	
	keepAskingDesiredFunctionValue = True	# variable temporal usada para saber si la información ingresada fue correcta
	desiredFunctionValue = 0	# almacena el valor x del y(x) deseado
	while keepAskingDesiredFunctionValue:	# ciclo controlador del ingreso de informacion correcta
		infoInput = input("Ingrese x del y(x) deseado: ")
		
		if isFloat(infoInput):	# si los caracteres ingresados cumplen los requisitos para poder convertirlo en un número real...
			desiredFunctionValue = float(infoInput) # convertirlo en un número real
			keepAskingDesiredFunctionValue = False	# salir del ciclo
		else:	# sino...
			print("- La informacion introducida no es un valor valido.")
	
	total = 0	# almacena el resultado
	if desiredFunctionValue in xValues: # si el valor de x del y(x) deseado se encuentra en la informacion ingresada...
		total = yValues[xValues.index(desiredFunctionValue)]	# asignar dicho valor al resultado
	else:	# sino...
		for i in range(amountOfValues): # para cada valor de x y y...
			total += calculateMember(xValues, yValues, i, desiredFunctionValue) # calcular los sumandos
	print(f"y(x) = {total}")
	
main()