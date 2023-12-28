#Создайте класс Число. Класс число хранит внутри одно значение.
# Используя перегрузку операторов реализуйте для него арифметические 
# операции для работы с числом (операции +, -, *, /).

from http.client import REQUEST_URI_TOO_LONG
from symbol import yield_arg


class Number:
    def __init__(self, n):
        self.number = n

    def __add__ (self, val):
        return Number(self.number + val.number);

    def __sub__ (self, val):
        return Number(self.number - val.number);

    def __mul__ (self, val):
        return Number(self.number * val.number);

    def __truediv__ (self, val):
        return Number(self.number / val.number)


#Создайте класс Дробь (или используйте уже ранее созданный вами). Используя перегрузку 
#операторов реализуйте для него арифметические операции для работы с дробями (операции +, -, *, /).


class Fraction():
    def __init__(self, n1, n2, n3 = 0):
        self.n1 = n1;
        self.n2 = n2;
        self.n3 = n3;

    def SetN1(self, n):
        self.n1 = n;

    def GetN1(self):
        return self.n1;

    def SetN2(self, n):
        self.n2 = n;

    def GetN2(self):
        return self.n2;

    def __add__(self, frac2):
        _n1 = self.n1 * frac2.n2 + self.n2 * frac2.n1;
        _n2 = self.n2 * frac2.n2;

        return Fraction(_n1, _n2)

    def __sub__(self, frac2):
        _n1 = self.n1 * frac2.n2 - self.n2 * frac2.n1;
        _n2 = self.n2 * frac2.n2;

        return Fraction(_n1, _n2)

    def __mul__(self, frac2):

        temp1 = Fraction(self.n1, self.n2)
        temp2 = Fraction(frac2.n1, frac2.n2)

        for i in range(2,10):
            if (self.n2 % i == 0 and frac2.n1 % i == 0):
                temp1.n2 = self.n2 / i;
                temp2.n1 = frac2.n1 / i;

        for i in range(2,10):
            if (self.n1 % i == 0 and frac2.n2 % i == 0):
                temp1.n1 = self.n1 / i;
                temp2.n2 = frac2.n2 / i;

        temp1.n1 *= temp2.n1;
        temp1.n2 *= temp2.n2;

        if (temp1.n1 > temp1.n2): temp1.Simplific();

        return temp1;

    def __truediv__(self, frac2):

        temp1 = Fraction(self.n1, self.n2)
        temp2 = Fraction(frac2.n1, frac2.n2)

        for i in range(2,10):
            if (self.n1 % i == 0 and frac2.n1 % i == 0):
                temp1.n1 = self.n1 / i;
                temp2.n1 = frac2.n1 / i;

        for i in range(2,10):
            if (self.n2 % i == 0 and frac2.n2 % i == 0):
                temp1.n2 = self.n2 / i;
                temp2.n2 = frac2.n2 / i;

        temp1.n1 *= temp2.n2;
        temp1.n2 *= temp2.n1;

        if (temp1.n1 > temp1.n2): temp1.Simplific();

        return temp1;

    def Simplific(self):
        temp = Fraction(self.n1, self.n2)
        self.n3 = temp.n1 // temp.n2;
        self.n1 = temp.n1 % temp.n2;

    def __str__(self):
        if(self.n3 > 0):
            return f"{int(self.n3)},{int(self.n1)}/{int(self.n2)}"
        else:
            return f"{int(self.n1)}/{int(self.n2)}"



a1 = Fraction(21, 5)
a2 = Fraction(5, 14)


print(a1 / a2)


#Создайте класс Библиотека. Класс предназначен для хранения информации о библиотеке (название, адрес, количество книг). 
#Реализуйте необходимые для класса методы. 
#Используя перегрузку операторов реализуйте для него следующие арифметические операции:
# + добавляет к количеству книг указанное значение;
# - вычитает из количества книг указанное значение;
# += добавляет к количеству книг указанное значение;
# -= вычитает из количества книг указанное значение; 
# Используя перегрузку операторов реализуйте (сравнение по количеству книг):
# <;
# >;
# <=;
# >=;
# ==; 
# !=.


class Library:
    def __init__(self, name, address, cntBooks):
        self.name = name
        self.address = address
        self.cntBooks = cntBooks

    def __add__ (self, newCntBooks ):
        return self.cntBooks + newCntBooks;

    def __sub__ (self, newCntBooks):
        return self.cntBooks + newCntBooks;

    def __iadd__ (self, newCntBooks ):
        self.cntBooks + newCntBooks;
        return self

    def __isub__ (self, newCntBooks):
        self.cntBooks - newCntBooks;
        return self

    def __lt__ (self, ohterLibrary):
        return self.cntBooks < ohterLibrary.cntBooks;

    def __gt__ (self, ohterLibrary):
        return self.cntBooks > ohterLibrary.cntBooks;

    def __le__ (self, ohterLibrary):
        return self.cntBooks <= ohterLibrary.cntBooks;

    def __ge__ (self, ohterLibrary):
        return self.cntBooks >= ohterLibrary.cntBooks;

    def __eq__ (self, ohterLibrary):
        return self.cntBooks == ohterLibrary.cntBooks;

    def __ne__ (self, ohterLibrary):
        return self.cntBooks != ohterLibrary.cntBooks;


l1 = Library("L1", "aaaaaaa", 5)
l2 = Library("L2", "bbbbbbb", 3)

print(l1!=l2)

    

#Задания №4
#Создайте класс Date, который будет содержать информацию о дате (день, месяц, год). 
#С помощью механизма перегрузки операторов, определите операцию разности двух дат 
#(результат в виде количества дней между датами), а также операцию увеличения даты на определенное количество дней.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


    def __add__ (self, newDays ):
        self.day += newDays;
        if self.day > 31:
            self.day -= 31
            self.month += 1
            if self.month > 12:
                self.month -= 12
                self.year += 1
        return self

    def __sub__ (self, newDate):
        day = self.day - newDate.day;
        month = self.month- newDate.month
        year = self.year- newDate.year

        if(year > 0):
            month += (year * 12)
            day += (month*30)
        elif(month > 0):
                day += (month*30)



        return f"Days - {day}"

    def __str__(self):
        if self.month < 10:
            return f"{self.day}.0{self.month}.{self.year}"
        else:
            return f"{self.day}.{self.month}.{self.year}"



d1 = Date(25, 12, 1996)
d2 = Date(23, 11, 1995)

print(d1 - d2)