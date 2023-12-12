
#Напишите программу для создания списка, длина которого равна N.
#После создания списка нужно подсчитать нечетные и четные числа.
#Если нечетных чисел больше, чем четных, вывод должен быть «Нет»,
#в остальных ключах «Да». 

import random

def createList(n):
    lst = [random.randint(1, 100) for _ in range(n)] 
    print(lst)

    cnt1 = cnt2 = 0;

    for i in lst:
        if i % 2 == 0: cnt1 += 1
        else: cnt2 += 1
    
    if(cnt1>cnt2): print("YES")
    else: print("NO")

createList(5)



#Создайте вложенный список размером 3*3 через функцию. 
#И посчитайте сумму элементов главной диагонали. 

def diagonal():
    s1 = input().split(" ")
    s2 = input().split(" ")
    s3 = input().split(" ")

    lst = [s1, s2, s3]

    print(int(lst[0][0]) + int(lst[1][1]) + int(lst[2][2]))


diagonal()



#Написать рекурсивную функцию, которая по заданному целому числу 
#возвращает n-e число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,……

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)



#Напишите функцию, которая проверяет является ли число степенью двойки. Если истинно выведите True, иначе False. 

def degreeTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

res = degreeTwo(8)

print(res)

#Реализовать инженерный калькулятор, для всех арифметических действий, 
#включая нахождение факториала, Фибоначчи, и всех тригонометрических функций, также возведения числа в степени. 
#В ходе решения, допустимо использования модуля math, функции 
#определяемой пользователем, рекурсивной функции и лямбда-функции. 
#Реализуйте диалог с пользователем. 




import math


while True:
    print("Select an action")
    print("(+, -, /, *)")
    print("(factorial, fibonacci, degree)")
    choice = input()

    if choice == "+" or choice == "-" or choice == "/" or choice == "*" or choice == "degree":

        print("(enter two number)")
        n1 = int(input())
        n2 = int(input())

        if choice == "+":
            res = n1 + n2
            print(res)

        elif choice == "-":
            res = n1 - n2
            print(res)

        elif choice == "/":
            if(n2 < 0): print("you can't divide by zero")
            else:
                res = n1 / n2
                print(res)

        elif choice == "*":
            res = n1 * n2
            print(res)

        elif(choice == "degree"):
            print(int(math.pow(n1, n2)))
    else:
        print("(enter number)")
        n1 = int(input())

        if(choice == "fibonacci"):
            res = fib(n1)
            print(f"{n1}-е число Фибоначчи: {res}")

        elif(choice == "factorial"):
            res = 1
            for i in range(1, n1 + 1):
                res *= i
            print(f"Факториал {res}")
        



    



