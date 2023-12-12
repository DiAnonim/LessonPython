
#Напишите программу для создания списка, длина которого равна N.
#После создания списка нужно подсчитать нечетные и четные числа.
#Если нечетных чисел больше, чем четных, вывод должен быть «Нет»,
#в остальных ключах «Да». 

#import random

#def createList(n):
#    lst = [random.randint(1, 100) for _ in range(n)] 
#    print(lst)

#    cnt1 = cnt2 = 0;

#    for i in lst:
#        if i % 2 == 0: cnt1 += 1
#        else: cnt2 += 1
    
#    if(cnt1>cnt2): print("YES")
#    else: print("NO")

#createList(5)



#Создайте вложенный список размером 3*3 через функцию. 
#И посчитайте сумму элементов главной диагонали. 

def diagonal():
    s1 = input().split(" ")
    s2 = input().split(" ")
    s3 = input().split(" ")

    lst = [s1, s2, s3]

    print(int(lst[0][0]) + int(lst[1][1]) + int(lst[2][2]))


diagonal()