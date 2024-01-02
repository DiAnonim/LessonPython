#Создайте класс Device, который содержит информацию об устройстве.
#С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
#класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).
#Каждый из классов должен содержать необходимые для работы методы.

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return self.name

class CoffeeMachine(Device):
    def __init__(self, brand, model, coffeeBeans = "Lifeboost Organic Whole Bean Coffee"):
        super().__init__(brand, model)
        self.coffeeBeans = coffeeBeans

    def coffeeBeans(self):
        print("Which coffee beans are recommended?")
        print("1. Lifeboost Organic Whole Bean Coffee")
        print("2. Koa Hawaiian Coffee")
        print("3. Volcanica Ethiopian Roast")
        print("4. Costa Rica Peaberry")


class Blender(Device):
    def __init__(self, brand, model, lvlSpeed):
        super().__init__(brand, model)
        self.lvlSpeed = lvlSpeed

    def blend(self):
        print(f"{self.brand} {self.model} is blending at speed level {self.lvlSpeed}.")



class MeatGrinder(Device):
    def __init__(self, brand, model, typeGrind):
        super().__init__(brand, model)
        self.typeGrind = typeGrind

    def grindMeat(self):
        print("1.Pork")
        print("2.Beef")
        print("3.Sheepmeat")

    
#Используя механизм множественного наследования разработайте класс “Автомобиль”, 
#который наследует от классов «Колеса», «Двигатель», «Двери».


class Wheels:
    def __init__(self, number):
        self.number = number

    def rotate(self):
        print(f"Wheels are rotating.")


class Engine:
    def __init__(self, fuelType):
        self.fuelType = fuelType

    def start(self):
        print(f"The engine is started.")

    def stop(self):
        print(f"The engine is stopped.")


class Doors:
    def __init__(self, numberDoors):
        self.numberDoors = numberDoors

    def open(self):
        print(f"Doors are opened.")

    def close(self):
        print(f"Doors are closed.")


class Car(Wheels, Engine, Doors):
    def __init__(self, brand, model, fuelType, numberDoors):
        Wheels.__init__(self, 4)
        Engine.__init__(self, fuelType)
        Doors.__init__(self, numberDoors)
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is now on the road.")


car = Car("Toyota", "Camry", "Gasoline", 4)

car.start()
car.open()
car.drive()
car.rotate()
car.close()
car.stop()



class Shape:
    def __init__(self, color):
        self.color = color

    def show(self):
        print(f"This is a {self.color} shape.")

    def save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.color} shape\n")

    def load(cls, filename):
        shapes = []
        with open(filename, 'r') as file:
            for line in file:
                color = line.strip().split()[0]
                shapes.append(cls(color))
        return shapes


class Square(Shape):
    def __init__(self, color, topLeftX, topLeftY, sideLen):
        super().__init__(color)
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.sideLen = sideLen

    def show(self):
        print(f"This is a {self.color} square with top-left coordinates ({self.topLeftX}, {self.topLeftY}) and side length {self.sideLen}.")

    def save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.color} square {self.topLeftX} {self.topLeftY} {self.sideLen}\n")

    @classmethod
    def load(cls, filename):
        squares = []
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                if data[1] == 'square':
                    color = data[0]
                    topLeftX = int(data[2])
                    topLeftY = int(data[3])
                    sideLen = int(data[4])
                    squares.append(cls(color, topLeftX, topLeftY, sideLen))
        return squares


class Rectangle(Shape):
    def __init__(self, color, topLeftX, topLeftY, w, h):
        super().__init__(color)
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.width = w
        self.height = h

    def show(self):
        print(f"This is a {self.color} rectangle with top-left coordinates ({self.topLeftX}, {self.topLeftY}), width {self.width}, and height {self.height}.")

    def save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.color} rectangle {self.topLeftX} {self.topLeftY} {self.width} {self.height}\n")

    @classmethod
    def load(cls, filename):
        rectangles = []
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                if data[1] == 'rectangle':
                    color = data[0]
                    topLeftX = int(data[2])
                    topLeftY = int(data[3])
                    width = int(data[4])
                    height = int(data[5])
                    rectangles.append(cls(color, topLeftX, topLeftY, width, height))
        return rectangles


class Circle(Shape):
    def __init__(self, color, centerX, centerY, r):
        super().__init__(color)
        self.centerX = centerX
        self.centerY = centerY
        self.radius = r

    def show(self):
        print(f"This is a {self.color} circle with center coordinates ({self.centerX}, {self.centerY}) and radius {self.radius}.")

    def save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.color} circle {self.centerX} {self.centerY} {self.radius}\n")

    @classmethod
    def load(cls, filename):
        circles = []
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                if data[1] == 'circle':
                    color = data[0]
                    centerX = int(data[2])
                    centerY = int(data[3])
                    radius = int(data[4])
                    circles.append(cls(color, centerX, centerY, radius))
        return circles


class Ellipse(Shape):
    def __init__(self, color, topLeftX, topLeftY, majorAxis, minorAxis):
        super().__init__(color)
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.majorAxis = majorAxis
        self.minorAxis = minorAxis

    def show(self):
        print(f"This is a {self.color} ellipse with top-left coordinates ({self.topLeftX}, {self.topLeftY}), major axis {self.majorAxis}, and minor axis {self.minorAxis}.")

    def save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.color} ellipse {self.topLeftX} {self.topLeftY} {self.majorAxis} {self.minorAxis}\n")

    @classmethod
    def load(cls, filename):
        ellipses = []
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                if data[1] == 'ellipse':
                    color = data[0]
                    topLeftX = int(data[2])
                    topLeftY = int(data[3])
                    majorAxis = int(data[4])
                    minorAxis = int(data[5])
                    ellipses.append(cls(color, topLeftX, topLeftY, majorAxis, minorAxis))
        return ellipses


square = Square("yellow", 0, 0, 5)
rectangle = Rectangle("orange", 2, 3, 6, 4)

# Вызываем методы show() для каждой фигуры
square.show()
rectangle.show()