#Создать генератор списка из исходного, который:

#1. из [1,2,3,4,5,6,7] получить {1: 1, 3: 27, 5: 125, 7: 343}
def generatList(inp):
    res = {x: x**3 for x in inp if x % 2 != 0}
    return res

lst = [1, 2, 3, 4, 5, 6, 7]

newDict = generatList(lst)
print(newDict)


#2. из [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] получить {2, 4, 6}
def generatListEven(inp):
    res = {x for x in inp if x % 2 == 0}
    return res

lst = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

res = generatListEven(lst)
print(res)

#3. получить список [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] без исходного

def newLst(inp):
    res = [x for x in inp if x != 0]
    return res

lst = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

newLst = newLst(lst)
print(newLst)

#4. написать функцию-генератор с yield, которая может перебирать числа, делящиеся на 7,
#в диапазоне от 0 до n

def divisibleSeven(n):
    for i in range(0, n + 1, 7):
        yield i

n = 50
for num in divisibleSeven(n):
    print(num)




