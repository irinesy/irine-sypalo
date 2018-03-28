def procedure_income(money, currency):
    usd = 57
    euro = 71
    gbp = 81
    uah = 2

    if currency == 400:
        money = round(money / usd, 2)
        print("Валюта: доллары США")
    elif currency == 401:
        money = round(money / euro, 2)
        print("Валюта: евро")
    elif currency == 402:
        money = round(money / gbp, 2)
        print("Валюта: брит.фунт")
    elif currency == 403:
        money = round(money / uah, 2)
        print("Валюта: гривна")
    return money

def main():
    money = int(input("Введите сумму, которую вы хотите обменять: "))
    currency = int(input("Укажите код валюты (доллары - 400, евро - 401, брит.фунт - 402, гривна - 403: "))
    result = procedure_income(money, currency)
    print("К получению:", result)



if __name__ == "__main__":
    main()