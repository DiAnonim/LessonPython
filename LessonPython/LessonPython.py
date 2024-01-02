#�������� ������ Book � Article, ������� ��������� ����� word_count. 
#�������� ������� total_words, ������� ��������� ������ ���������� � ���������� ����� ���������� ����.


class Document:
    def __init__(self, content, title, author):
        self.content = content
        self.title = title
        self.author = author

    def word_count(self):
        words = self.content.split()
        return len(words)


class Book(Document):
    def __init__(self, content, title, author):
        super().__init__(content, title, author)


class Article(Document):
    def __init__(self, content, title, author):
        super().__init__(content, title, author)


def total_words(documents):
    total = 0
    for doc in documents:
        total += doc.word_count()
    return total


#�������� ������ Box � Cylinder, ������� ��������� ����� volume. 
#�������� ������� total_volume, ������� ��������� ������ ����������� � ���������� ����� �����.


from math import pi


class Container:
    def __init__(self, height):
         self.height = height

  


class Box(Container):
    def __init__(self, length, width, height):
        super().__init__(height)
        self.length = length
        self.width = width

    def volume(self):
        return self.length * self.width * self.height


class Cylinder(Container):
    def __init__(self, radius, height):
        super().__init__(height)
        self.radius = radius

    def volume(self):
        return pi * self.radius**2 * self.height


def total_volume(containers):
    total = 0
    for container in containers:
        total += container.volume()
    return total


#Создайте классы Dog и Cat, которые реализуют метод make_sound.
#Напишите функцию play_sounds, которая принимает список объектов 
#и вызывает метод make_sound если объект является экземпляром классов
#Dog или Cat. Используйте функцию isinstance. 

class Dog:
    def makeSound(self):
        print("Woof")


class Cat:
    def makeSound(self):
        print("Meow")


def play_sounds(mas):
    for i in mas:
        if isinstance(i, Dog) or isinstance(i, Cat):
            i.makeSound()


d = Dog()
c = Cat()

arr = [d,c]

play_sounds(arr)