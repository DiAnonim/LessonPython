
#Напишите программу, где я ввожу логин и пароль. 
#И если данные были введены верно, то мы выводим Authentication completed, 
#иначе Invalid login or password. Правильность логина не зависит от 
#(Логин должен быть user, пароль - qwerty) 

log = input()
pas = input()

def Check():
    if log == "user" and pas == "qwerty": print("Authentication completed")
    else: print("Invalid login or password")

Check()


#Напишите программу обмена валют, 
#где я ввожу сумму в тенге и выбираю на какую валюту хочу перевести. 
#(Курс USD – 420, EUR – 510, RUB - 5.8).

tenge = float(input("Введите сумму в тенге: "))

valuta = input("Выберите валюту (USD, EUR, RUB): ")

exchangeRates = {'USD': 420, 'EUR': 510, 'RUB': 5.8}

def currency_exchange(t, v):
    if v not in exchangeRates:
        print("Неверный выбор.")
        return

    exchangeRates = exchangeRates[v]
    result_amount = t / exchangeRates

    print(f'{t} тг = {result_amount:.2f} {v}.')


currency_exchange(tenge, valuta)



#Вася получил первую зарплату и захотел это отпраздновать: провести вечер за любимым сериалом и пиццей. 
#Хватит ли Васе денег, если подписка на онлайн кинотеатр стоит s рублей,
# пицца – p рублей, а всего он заработал m рублей? 
#На вход подается стоимость подписки на онлайн-кинотеатр (s), 
#стоимость пиццы (p) и зарплата Пети (m), а выводится «Да»,
#если он сможет позволить себе покупку, а иначе – «Нет». 

def Expenses(s, p, m):
    if(m<s+p): print("No")
    else: print("Yes")

Expenses(500, 600, 2000)


#Паша очень любит кататься на общественном транспорте, а получая билет, 
#сразу проверяет, счастливый ли ему попался. Билет считается счастливым, 
#если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.
#Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, 
#которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.
#На вход программе подаётся строка из шести цифр.
#Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.

def ticket(s):
    res1 = int(s[0]) + int(s[1]) + int(s[2])
    res2 = int(s[3]) + int(s[4]) + int(s[5])

    if res1 == res2: print("Счастливый")
    else: print("Обычный")



ticket("090234")


#По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
#В решении этой задачи можно использовать только один цикл.
#Пользоваться математической библиотекой math в этой задаче запрещено

def calFactorialSum(n):
    res = 0
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        res += fact

    return res


#По данному натуральному n ≤ 9 выведите лесенку из n ступенек,
#i-я ступенька состоит из чисел от 1 до i без пробелов.


def ladderNumbers(n):
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

ladderNumbers(3)


#Для настольной игры используются карточки с номерами от 1 до N. 
#Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
#Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).
#Программа должна вывести номер потерянной карточки.

N = int(input("Введите число: "))

cards = list(map(int, input("Введите номера карточек через пробел: ").split()))

def findCard(N, cards):
    resSum = N * (N + 1) // 2
    remainingSum = sum(cards)
    missingCard = resSum - remainingSum
    return missingCard

missingCard = findCard(N, cards)

print(f"Потерянная карточка: {missingCard}")


#По данному целому числу N распечатайте все квадраты натуральных чисел, 
#не превосходящие N, в порядке возрастания.

def square(N):
    i = 1
    while i**2 <= N:
        print(i**2)
        i += 1

N = int(input("Введите целое число: "))

square(N)


