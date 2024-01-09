#1. Задание 1 (cycle): Напишите функцию cycle_string, которая принимает строку и целое
#число n в качестве входных данных и возвращает строку, являющуюся результатом
#повторения входной строки n раз. Например, cycle_string("abc", 3) должна
#вернуть "abcabcabc".
#def cycle_string(s, n):
#    res = ""
#    for i in range(n):
#        res += s;
#    return res

#print(cycle_string("math", 3))

#2. Задание 2 (count): Напишите функцию count_from, которая принимает целое
#число start и целое число n в качестве входных данных и возвращает список из n целых
#чисел, начиная от start. Например, count_from(5, 3) должна вернуть [5, 6, 7].

#def count_from(start, n):
#    mas = []

#    for i in range(n):
#        mas.append(start)
#        start += 1

#    return mas

#print(count_from(5, 3))

#3. Задание 3 (starmap): Напишите функцию multiply_elements, которая принимает
#список кортежей, где каждый кортеж содержит два целых числа, и возвращает список
#произведений чисел в каждом кортеже. Например, multiply_elements([(1, 2), (3, 4), (5,
#6)]) должна вернуть [2, 12, 30].

#from itertools import starmap

#def mult(x, y):
#    return x * y

#def multiply_elements(lst):
#    res = list(starmap(mult, lst))
#    return res


#print(multiply_elements([(1, 2), (3, 4), (5, 6)]))

#4. Задание 4 (accumulate): Напишите функцию accumulate_sums, которая принимает
#список целых чисел и возвращает список накопленных сумм.
#Например, accumulate_sums([1, 2, 3, 4, 5]) должна вернуть [1, 3, 6, 10, 15].
#from itertools import accumulate

#def accumulate_sums(numbers):
#    res = list(accumulate(numbers))
#    return res

#print(accumulate_sums([1, 2, 3, 4, 5]))

#5. Задание 5 (dropwhile): Напишите функцию drop_less_than, которая принимает список
#целых чисел и целое число n в качестве входных данных и возвращает список целых
#чисел из входного списка, начиная с первого числа, которое не меньше n.
#Например, drop_less_than([1, 2, 3, 4, 5], 3) должна вернуть [3, 4, 5].

def drop_less_than(lst, n):
    mas = []
    for i in range(len(lst)):
        if(lst[i] >= n):
            mas.append(lst[i])

    return mas

print(drop_less_than([1, 2, 3, 4, 5], 3))