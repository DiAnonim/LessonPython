
#1. Напишите функцию superset(), которая принимает 2 множества. Результат работы
#функции: вывод в консоль одного из сообщений в зависимости от ситуации:
#1 - «Супермножество не обнаружено»
#2 – «Объект {X} является чистым супермножеством»
#3 – «Множества равны»

def superset(s1, s2):
    if s1.issuperset(s2):
        print(f"Объект {s1} является чистым супермножеством")
    elif s1 == s2:
        print("Множества равны")
    else:
        print("Супермножество не обнаружено")

#2. Создайте программу «Англо-французский словарь». Нужно хранить слово на
#английском языке и его перевод на французский. Требуется реализовать возможность
#добавления, удаления, поиска, замены данных. Используйте словарь для хранения
#информации.

dictionary = {}

def wordAdd(eng, fren):
        dictionary[eng] = fren
        print(f'Слово "{eng}" добавлено в словарь с переводом "{fren}".')

def wordRemove(eng):
        if eng in dictionary:
            del dictionary[eng]
            print(f'Слово "{eng}" удалено из словаря.')
        else:
            print(f'Слово "{eng}" не найдено в словаре.')


def wordSearch(eng):
        if eng in dictionary:
            print(f'Перевод слова "{eng}" на французский: {dictionary[eng]}')
        else:
            print(f'Слово "{eng}" не найдено в словаре.')


def update(eng, newFren):
        if eng in dictionary:
            dictionary[eng] = newFren
            print(f'Перевод для слова "{eng}" обновлен: {newFren}.')
        else:
            print(f'Слово "{eng}" не найдено в словаре.')


def printDictionary():
        print("Словарь:")
        for eng, fren in dictionary.items():
            print(f'{eng}: {fren}')



#3. Предоставлен список натуральных чисел. Требуется сформировать из них множество.
#Если какое-либо число повторяется, то преобразовать его в строку по образцу: например, если
#число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка
#«44» (второе повторение, т.е. число дублируется в строке), строка «444» (третье повторение,
#т.е. строка множится на 3).
#Реализуйте вывод множества через функцию set_gen()

def set_gen(num):
    resSet = set()

    for num in num:
        cnt = num.count(num)
        if cnt == 1:
            resSet.add(num)
        else:
            temp = str(num) * cnt
            resSet.add(num)
            resSet.add(temp)

    return resSet


#4. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию
#biggest_dict(**kwargs), которая принимает неограниченное количество параметров «ключ:
#значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента
#«first_one» со значением «we can do it». Воссоздайте эту функцию.
#Output:
#{'first_one': 'we can do it', 'k1': 22, 'k2': 31, 'k3': 11, 'k4': 91, 'name': 'Елена', 'age': 31, 'weight':
#61, 'eyes_color': 'grey'}

def biggest_dict(**kwargs):
    my_dict = {'first_one': 'we can do it'}
    my_dict.update(kwargs)
    return my_dict


#2. Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый
#и последний элемент объекта. Удалите второй элемент. Добавьте в конец ключ «new_key» со
#значением «new_value». Выведите на печать итоговый словарь. Важно, чтобы словарь остался
#тем же (имел тот же адрес в памяти).

my_dict = {'key1': 10, 'key2': 20, 'key3': 30, 'key4': 40, 'key5': 50}

print("Исходный словарь:", my_dict)

first, last = next(iter(my_dict)), next(reversed(my_dict))
my_dict[first], my_dict[last] = my_dict[last], my_dict[first]

del my_dict[next(iter(my_dict))]

my_dict['new_key'] = 'new_value'

print("Итоговый словарь:", my_dict)



#3. Есть некоторый словарь, который хранит названия стран и столиц. Название страны
#используется в качестве ключа, название столицы в качестве значения. Необходимо
#реализовать: добавление данных, удаление данных, поиск данных, редактирование данных,
#сохранение и загрузку данных (используя упаковку и распаковку).

capitalsDict = {}

def add(country, capital):
        capitalsDict[country] = capital
        print(f'Данные для {country} добавлены. Столица: {capital}')

def remove(country):
        if country in capitalsDict:
            remCap = capitalsDict.pop(country)
            print(f'Данные для {country} удалены. Столица: {remCap}')
        else:
            print(f'Данные для {country} не найдены.')


