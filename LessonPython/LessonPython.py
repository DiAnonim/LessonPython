
#Создать генератор списка из исходного, который:
#1.берет только четные значения, отрицательные возводит в куб, остальные в квадрат

def new_generator(lst):
    for x in lst:
        if x % 2 == 0:
            yield x**3 if x < 0 else x**2

lst = [1, 2, 3, 4, 5, -6, -7, 8, 9]
res_generator = new_generator(lst)

print("Исходный список:", lst)
print("Преобразованный генератор:")
for value in res_generator:
    print(value)



#2. считает длину строк для списка из строк

lst = ["aaa", "bb", "dddd", "ggggg"]
generator = (len(s) for s in lst)

print("Исходный список строк:", lst)
print("Длины строк в генераторе:")
for length in generator:
    print(length)


#3. список квадратов четных чисел

def new_generator(lst):
    for x in lst:
        if x % 2 == 0:
            yield x**2

lst = [1, 2, 3, 4, 5, -6, -7, 8, 9]
generator = new_generator(lst)

print("Исходный список строк:", lst)
print("Длины строк в генераторе:")
for i in generator:
    print(i)

#4. только положительные, кратные 5, отрицательные заменить на 0

def new_generator(lst):
    for x in lst:
        if x > 0 and x % 5 == 0:
            yield x
        else: yield 0

lst = [10, 2, 3, 15, 5, -6, -7, 8, 9]
generator = new_generator(lst)

print("Исходный список строк:", lst)
print("Длины строк в генераторе:")
for i in generator:
    print(i)

#5. из строки – только гласные буквы.

vowels = "aeiouAEIOU"
lst = ["mama", "banana", "chair", "milk"]
generator = (char for s in lst for char in s if char in vowels)

print("исходный список строк:", lst)
print("длины строк в генераторе:")
for length in generator:
    print(length)


##Написать декоратор, который оборачивает строку в теги <i></i>.

def tagI(f1):
    def tagPrintI():
        print("<i>", end="")
        f1()
        print("<i>", end="")
    return tagPrintI

##Написать декоратор, который оборачивает строку в теги <strong></strong>

def tagStrong(f1):
    def tagPrintStrong():
        print("<strong>", end="")
        f1()
        print("<strong>", end="")
    return tagPrintStrong


#Применить оба декоратора
@tagStrong
@tagI
def stringPrint():
    print("aaaaaaaaaaaaaaaa", end="")

stringPrint()


