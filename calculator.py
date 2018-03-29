print("Ноль в качестве знака операции завершит работу программы")
while True:
	s = input("Знак (XOR,OR,AND,NOT): ")
	if s == '0': break
	if s in ('XOR','OR','AND','NOT'):
		x = int(input("x="))
		y = int(input("y="))
		if s == 'XOR':
			print("%.2f" % (x^y))
		elif s == 'OR':
			print("%.2f" % (x|y))
		elif s == 'AND':
			print("%.2f" % (x&y))
		elif s == 'NOT':
			if y != 0:
				print("%.2f" % (~x))
			else:
				print("Деление на ноль!")
	else:
		print("Неверный знак операции!")