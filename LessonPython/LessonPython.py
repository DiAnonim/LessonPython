#1. Дан список. Определите, является ли он монотонно возрастающим (то есть верно ли, что каждый элемент этого списка больше предыдущего).
#Выведите YES, если список монотонно возрастает и NO в противном случае.
#Решение оформите в виде функции IsAscending(A).

#def IsAscending(*A):
#    size = len(A)
#    if size == 0 or size == 1: return print("Yes")
#    for i in range(size-1):
#        if A[i] > A[i + 1]: return print("No")
#    return print("Yes")

#IsAscending(1, 5, 2, 4)


#Дан список чисел, число a и натуральное число k. Выведите индекс k-го по счету появления в массиве числа a. 
#Если число a встречается в массиве менее k раз, выведите число -1.
#Решение оформите в виде функции KthAppearance(A, a, k).

#def KthAppearance(*A, a, k):
#    cnt = 0
#    for i in range(len(A)):
#        if A[i] == a:
#            cnt += 1
#            if cnt == k:
#                return i  # Нашли k-е появление, возвращаем индекс
#    return -1 

#lst = [1, 2, 1, 3, 2, 3, 2, 3, 2, 2]
#a= 3
#k= 1
#res = KthAppearance(lst, a, k)
#print(res)

#Системный администратор вспомнил, что давно не делал архива пользовательских файлов. 
#Однако, объем диска, куда он может поместить архив, может быть меньше чем суммарный объем архивируемых файлов.
#Известно, какой объем занимают файлы каждого пользователя.
#Напишите программу, которая по заданной информации о пользователях и свободному объему на архивном диске определит максимальное число пользователей,
#чьи данные можно поместить в архив, при этом используя свободное место как можно более полно.
#Программа получает на вход в одной строке число S размер свободного места на диске, и число N — количество пользователей, 
#после этого идет N чисел — объем данных каждого пользователя, записанных каждое в отдельной строке.
#Выведите наибольшее количество пользователей, чьи данные могут быть помешены в архив.

#def max_users_in_archive(S, userData):
#    userData.sort()

#    userCnt = 0
#    totalData = 0

#    for data in userData:
#        totalData += data
#        if totalData <= S:
#            userCnt += 1
#        else:
#            break

#    return userCnt

#S = int(input("Enter the amount of free disk space: "))
#N = int(input("Enter the number of users: "))
#userData = [int(input(f"The amount of user data {i + 1}: ")) for i in range(N)]

#result = max_users_in_archive(S, userData)
#print(f"Maximum number of users: {result}")


#После затянувшегося совещания директор фирмы решил заказать такси, чтобы развезти сотрудников по домам. 
#Он заказал N машин —ровно столько, сколь у него сотрудников. Однако, когда они подъехали, оказалось, что у каждого водителя такси свой тариф за 1 километр.
#Директор знает, какому сотруднику сколько километров от работы до дома (к сожалению, все сотрудники живут в разных направлениях,
#поэтому нельзя отправить двух сотрудников на одной машине). Теперь директор хочет определить, сколько придется заплатить за перевозку всех сотрудников. 
#Естественно, директор хочет заплатить как можно меньшую сумму.
#В первой строке записаны N чисел через пробел, задающих расстояния в километрах от работы до домов сотрудников компании.
#Во второй строке записаны N чисел — тарифы за проезд одного километра в такси.
#Выведите одно целое число — наименьшую сумму, которую придется заплатить за доставку всех сотрудников.

#def min_TaxiCost(distances, tariffs):
#    total_cost = sum(dist * tariff for dist, tariff in zip(distances, tariffs))
#    return total_cost

#dist = list(map(int, input().split()))
#tariffs = list(map(int, input().split()))

#result = min_TaxiCost(dist, tariffs)
#print(result)


#Дана последовательность чисел, состоящая только из чисел 1, ..., 9. Последовательность завершается числом 0. Каждое число записано в отдельной строке.
#Подсчитайте, сколько раз в этой последовательности встречаются значения 1, 2, ..., 9. Сохранять всю последовательность введенных чисел в списке нельзя.
#Программа должна вывести ровно 9 чисел: количество единиц, двоек, ..., девяток в данной последовательности.

#cnt = [0] * 9

#while True:
#    num = int(input())
#    if num == 0:
#        break
#    elif 1 <= num <= 9:
#        cnt[num - 1] += 1

#for c in cnt:
#    print(c, end=" ")


#Напишите программу, в которой необходимо вывести первое слово из строки. 

#def firstWord(inp):
#    words = inp.split()
#    if words:
#        return words[0]
#    else:
#        return "Empty str"

#inp = input("Enter string: ")

#res = firstWord(inp)
#print("First word in string:", res)

#Напишите программу, которая извлечет дату из строки.  

#import re

#def searchDate(input_string):
#    date_pattern = re.compile(r'\b(\d{2}[\./]\d{2}[\./]\d{4})\b')

#    match = date_pattern.search(input_string)

#    if match:
#        return match.group(1)
#    else:
#        return "Date not found"

#inp = input("Enter string: ")

#res = searchDate(inp)
#print("Date retrieved:", res)


#Напишите программу, в которой я ввожу телефонный номер. Необходимо проверить правильность формата телефонного номера

import re

def searchPhoneNumber(numb):
    phone_pattern = re.compile(r'^\+?[0-9]{1,3}[-.\s]?[0-9]{1,}$')

    return bool(phone_pattern.match(numb))

phoneNumber = input("Enter Phone number: ")

print(searchPhoneNumber(phoneNumber))





