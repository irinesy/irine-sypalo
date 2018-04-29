print("Программа калькулятор, чтоб ее выключить введите 0")
while True:
    s = input("Какую логическую операцию вы хотите сделать И(i),Или(or),Не(not),Сложение по модулю 2(xor):")
    if s == '0': break
    if s in('i','or','not','xor'):
        x = float(input("x = "))
        y = float(input("y = "))
        if s == 'or':
            if x == y == 0:
                print("\tРезультат = ",0)
            else:
                print("\tРезультат = ", 1)
        if s == 'i':
            if x == y == 1:
                print("\tРезультат = ", 1)
            else:
                print("\tРезультат = ", 0)
        if s == 'xor':
            if x == y:
                print("\tРезультат = ",0)
            if x != y:
                print("\tРезультат = ",1)
        if s == 'not':
            if x == 0 and y == 0:
                print("\tРезультат, x = ",1," y = ",1)
            if x == 0 and y == 1:
                print("\tРезультат, x = ",1," y = ",0)
            if x == 1 and y == 0:
                print("\tРезультат, x = ",0," y = ",1)
            if x == 1 and y == 1:
                print("\tРезультат, x = ",0," y = ",0)