#Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
#Проверка на равенство радиусов двух окружностей (операция = =);
#Сравнения длин двух окружностей (операции >, <, <=,>=);
#Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=).

class Circle:
    def __init__(self, r):
        self.radius = r
        self.pi = 3.14

    def __eq__(self, otherCircle):
        return self.radius == otherCircle.radius

    def calcLength(self):
        return 2*self.pi * self.radius

    def __gt__(self, otherC):
        return self.calcLength() > otherC.calcLength()

    def __lt__(self, otherC):
        return self.calcLength() < otherC.calcLength()

    def __ge__(self, otherC):
        return self.calcLength() >= otherC.calcLength()

    def __le__(self, otherC):
        return self.calcLength() <= otherC.calcLength()

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self


#Вам необходимо создать класс Airplane (самолет). 
#С помощью перегрузки операторов реализовать: 
#Проверка на равенство типов самолетов (операция = =); 
#Увеличение и уменьшение пассажиров в салоне самолета (операции +  - +=  -=);
#Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > <  <=  >=)


class Airplane:
    def __init__(self, t, p, maxP):
        self.type = t
        self.passenger = p
        self.maxPassenger = maxP

    def __eq__(self, other):
        return self.type == other.type

    def __add__(self, value):
        return Circle(self.passenger + value)

    def __sub__(self, value):
        return Circle(self.passenger - value)

    def __iadd__(self, value):
        self.passenger += value
        return self

    def __isub__(self, value):
        self.passenger -= value
        return self

    def __gt__(self, other):
        return self.maxPassenger > other.maxPassenger

    def __lt__(self, other):
        return self.maxPassenger < other.maxPassenger

    def __ge__(self, other):
        return self.maxPassenger >= other.maxPassenger

    def __le__(self, other):
        return self.maxPassenger <= other.maxPassenger



#Создайте класс Roman (РимскоеЧисло), представляющий римское число и поддерживающий операции +, -, *, /.
#При реализации класса:
#операции +, -, *, / реализуйте как специальные методы 
#методы преобразования как статические методы.


class Roman:
    def __init__(self, v):
        self.val = v
        self.intVal = Roman.romanToInt(v)

    def __add__(self, other):
        resInt = self.intVal + other.intVal
        resRom = Roman.intToRoman(resInt)
        return Roman(resRom)

    def __sub__(self, other):
        resInt = self.intVal - other.intVal
        resRom = Roman.intToRoman(resInt)
        return Roman(resRom)

    def __mul__(self, other):
        resInt = self.intVal * other.intVal
        resRom = Roman.intToRoman(resInt)
        return Roman(resRom)

    def __truediv__(self, other):
        resInt = self.intVal / other.intVal
        resRom = Roman.intToRoman(resInt)
        return Roman(resRom)

    @staticmethod
    def romanToInt(roman):
        dictRoman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                      'D': 500, 'CM': 900, 'M': 1000}
        res = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in dictRoman:
                res += dictRoman[roman[i:i+2]]
                i += 2
            else:
                res += dictRoman[roman[i]]
                i += 1
        return res

    @staticmethod
    def intToRoman(num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        numRom = ''
        i = 0
        while num > 0:
            for _ in range(int(num // val[i])):
                numRom += syb[i]
                num -= val[i]
            i += 1
        return numRom

    def __str__(self):
        return self.val


r1 = Roman("XII")
r2 = Roman("IV")


result_add = r1 + r2
result_sub = r1 - r2
result_mul = r1 * r2
result_div = r1 / r2

print(f"{r1} + {r2} = {result_add}")
print(f"{r1} - {r2} = {result_sub}")
print(f"{r1} * {r2} = {result_mul}")
print(f"{r1} / {r2} = {result_div}")
