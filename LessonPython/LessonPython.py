
# Задание №1.
# Петя решил подвести итоги четверти и посчитать, сколько он получил пятерок,
# четверок, троек и двоек. Пользователь вводит список цифр через пробел. В первой строке вам
# необходимо вывести количество пятерок, четверок, троек и двоек через пробел. Во второй –
# средний балл Васи.
# Например,
# Input                               Output
# 5 5 5 5 3 4 5 4 4                  5 3 1 0
#                               4.444444444444445


strList = input().split(" ")


class Counter:
    cntFive: int = 0
    cntFour: int = 0
    cntThree: int = 0
    cntTwo: int = 0
    avg: float



cntEstimation = Counter()

for i in strList:
    if i == "5":
        cntEstimation.cntFive += 1
    if i == "4":
        cntEstimation.cntFour += 1
    if i == "3":
        cntEstimation.cntThree += 1
    if i == "2":
        cntEstimation.cntTwo += 1

print(cntEstimation.cntFive, cntEstimation.cntFour, cntEstimation.cntThree, cntEstimation.cntTwo)

cnt = cntEstimation.cntFive + cntEstimation.cntFour + cntEstimation.cntThree + cntEstimation.cntTwo

cntEstimation.avg = (cntEstimation.cntFive * 5 + cntEstimation.cntFour * 4 + cntEstimation.cntThree * 3 + cntEstimation.cntTwo * 2) / cnt

print(cntEstimation.avg)