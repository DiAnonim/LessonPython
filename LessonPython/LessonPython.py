#Создайте классы Book и Article, которые реализуют метод word_count. 
#Напишите функцию total_words, которая принимает список документов и возвращает общее количество слов.


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


#Создайте классы Box и Cylinder, которые реализуют метод volume. 
#Напишите функцию total_volume, которая принимает список контейнеров и возвращает общий объем.


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


# Пример использования
box1 = Box(2, 3, 4)
cylinder1 = Cylinder(1, 5)
box2 = Box(3, 4, 5)

containers = [box1, cylinder1, box2]

total_container_volume = total_volume(containers)
print("Total volume of all containers:", total_container_volume)
