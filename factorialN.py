def factorial():
	num= int(input("Ingresa un numero"))
	factorial= 1
	for i in range(num):
		factorial=factorial*num
		num-= 1
	print(factorial)
factorial()
