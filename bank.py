import account
import evro


def main():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))

    result = account.calculate_income(rate, money, period)
    print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: ", result)

    currency = int(input("Укажите код валюты (доллары - 400, евро - 401, брит.фунт - 402, гривна - 403)): "))
    a = evro.procedure_income(result, currency)
    print("Итого:", a)


if __name__ == "__main__":
    main()
