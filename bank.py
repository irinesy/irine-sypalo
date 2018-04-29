flag = "+"
while flag == "+":
    print("\n","Добро пожаловать в банк выдачи кредита в иностранной валюте")

    euro = 60
    usd = 57
    print("\n","Курс евро = ",euro,"\n","Курс доллара = ",usd)

    currency = int(input("\nВведите код валюты, в которой вы хотите взять кредит (Евро - 1, Доллар - 2) "))
    x = (input("\nВведите с какой целью вы хотите взять кредит: "))

    if currency == 1:
        money = int(input("Введите количество евро, которые вы ходите взять в кредит: "))
        if money > 0:
            rate = int(input("Введите процентную ставку = "))
            period = int(input("Введите период, на который вы берете кредит = "))
            result = round((((money*rate)/100)+money),0)
            mounth = round(result/period,2)
            print("Вам надо будет отдать банку: ",result,"Евро","или по",mounth,"Евро в течение",period,"месяцев")
        else:
            print("Введите сумму побольше чем 0 :) ")
    elif currency == 2:
        money = int(input("Введите количество долларов, которые вы ходите взять в кредит: "))
        if money > 0:
            rate = int(input("Введите процентную ставку = "))
            period = int(input("Введите период на который вы берете кредит = "))
            result = round((((money*rate)/100)+money),0)
            mounth = round(result/period,2)
            print("Вам надо будет отдать банку: ",result,"Долларов","или по",mounth,"Долларов в течение",period,"месяцев")
        else:
            print("Введите сумму побольше чем 0 :) ")
    flag = input("\tЖелаете еще взять кредит? ( + или - ) ")