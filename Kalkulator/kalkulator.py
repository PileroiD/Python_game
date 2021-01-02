a = int(input("Пожалуйста, введите первое число :  "))
b = int(input("Пожалуйста, введите второе число :  "))
c = input("Что будем делать?: +, -, /, * :    ")

if c == "+":
	print(f'Ваш ответ: {a+b}')
elif c == "-":
	c = input('что от чего отнимаем? '+ str(a)   +' от '+  str(b)  +' или '+  str(b)  +' от '+  str(a)  +' : '  )
	if c == str(a) +' от '+ str(b):
		print(int(b-a))
	if c == str(b) +' от '+ str(a):
		print(int(a-b))
elif c == "/":
	c=input("что на что делим?  "+ str(a) +' на '+ str(b) + ' или '+ str(b) + ' на '+ str(a) + ' : ')
	if c == str(a) + ' на ' + str(b):
		print(float(a / b))
	if c == str(b)+ ' на '+ str(a):
		print(float(b / a))
elif c=="*":
	print(a*b)	