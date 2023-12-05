#1. Напишите программу для удаления заданного числа из набора.
#Output:
#Enter the number you want to remove:12
#After Removing: {1, 2, 3, 4, 5, 6, 24}

#s = {1, 2, 3, 4, 5, 6, 24}

#inp = input();

#s.remove(int(inp))

#print(s)


#2. Напишите программу для добавления нескольких элементов к множеству.
#Output:
#{1, 2, 4, 'Apple', 'John', 'CS', 'Mango', 'Grapes'}

#s = {1 ,2 ,3}
#print(s)

#Adds = {'Apple', 'John'}

#s.update(Adds)

#print(s)

#3. Напишите программу для нахождения объединения двух множеств.
#Output:
#{96, 65, 2, 'Joseph', 1, 'Peter', 59}

#s1 = {1, 2, 'Peter', 6}
#s2 = {9, 5, 'Joseph', 2}

#us = s1.union(s2)

#print(us)


#4. Есть множество, содержащее название стран. Необходимо предоставить
#пользователю возможности:
#•Добавление стран;
#•Удаления стран;
#•Поиска стран по введенным символам;
#•Проверки существует ли страна внутри множества.


Country = {"Russian", "USA"}
print(Country)

def AddCountry(c):
    Country.add(c)
    print(f"Country {c} added to the set.")

def RemoveCountry(c):
    Country.remove(c)
    print(f"Country {c} removed from the set.")


def SearchCountry(c):
    search = [ctr for ctr in Country if c.lower() in str(ctr).lower()]
    print(f"Countries found: {search}")

def CheckCountry(c):
        if c in Country:
            print(f"The country {c} exists in a variety of.")

while True:

    print("1 - Adding countries")
    print("2 - Deleting countries")
    print("3 - Search for countries by entered characters")
    print("4 - Checks whether a country exists within a set")
    print("5 - Exit")
    inp = input();

    if inp == "1":
        print("Enter Country")
        inp2 = input()
        AddCountry(inp2)
        print(Country)

    if inp == "2":
        print("Enter Country")
        inp2 = input()
        RemoveCountry(inp2)
        print(Country)

    if inp == "3":
        print("Enter Str")
        inp2 = input()
        SearchCountry(inp2)
        print(Country)

    if inp == "4":
        print("Enter Country")
        inp2 = input()
        CheckCountry(inp2)
        print(Country)

    if inp == "5": break;




