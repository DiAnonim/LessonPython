# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: 
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к 
# отдельным полям через методы класса.


class Car:
    def __init__(self, name, year, proizv, ec, color, price):
        self._name = name
        self._year = year
        self._proizvoditel = proizv
        self._engineCapacity = ec
        self._color = color
        self._price= price

    def getName(self):
        return self._name

    def setName(self, n):
        self._name = n

    def getYear(self):
        return self._year

    def setYear(self, y):
        self._year = y

    def getProizvoditel(self):
        return self._proizvoditel

    def setProizvoditel(self, p):
        self._proizvoditel = p

    def getEngineCapacity(self):
        return self._engineCapacity

    def setEngineCapacity(self, ec):
        self._engineCapacity = ec

    def getColor(self):
        return self._color

    def setColor(self, c):
        self._color = c

    def getPrice(self):
        return self._price

    def setPrice(self, p):
        self._price = p

    def __str__(self):
        return f"Название модели - {self.getName()}\nГод выпуска - {self.getYear()}\nПроизводитель - {self.getProizvoditel()}\nOбъем двигателя - {self.getEngineCapacity()}\nЦвет машины - {self.getColor()}\nЦена - {self.getPrice()}\n"


car = Car("Toyota", "1900", "Someone", "5", "black", "15kk")

print(car)

# Реализуйте класс «Книга». Необходимо хранить в полях класса: 
# название книги, год выпуска, издателя, жанр, автора, цену. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте 
# доступ к отдельным полям через модификаторы доступа и свойства (@property).


class Book:
    def __init__(self, name, year, izdatel, genre , author, price):
        self._name = name
        self._year = year
        self._izdatel = izdatel
        self._genre = genre 
        self._author= author
        self._price= price

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, val):
        self._name = val

    @property
    def Year(self):
        return self._year

    @Year.setter
    def Year(self, val):
        self._year = val

    @property
    def Izdatel(self):
        return self._izdatel

    @Izdatel.setter
    def Izdatel(self, val):
        self._izdatel = val

    @property
    def Genre(self):
        return self._genre

    @Genre.setter
    def Genre(self, val):
        self._genre = val

    @property
    def Author(self):
        return self._author

    @Author.setter
    def Author(self, val):
        self._author = val

    @property
    def Price(self):
        return self._price

    @Price.setter
    def Price(self, val):
        self._price = val


    def __str__(self):
       return f"Название книги - {self.Name}\nГод выпуска - {self.Year}\nИздатель - {self.Izdatel}\nЖанр - {self.Genre}\nАвтор - {self.Author}\nЦена - {self.Price}"

book = Book("BookName", "1700", "Someone", "Horror", "Stiven King", "1500")

print(book)

