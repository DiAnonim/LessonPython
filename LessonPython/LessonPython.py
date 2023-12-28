#—оздайте класс „исло.  ласс число хранит внутри одно значение.
#»спользу€ перегрузку операторов реализуйте дл€ него арифметические 
#операции дл€ работы с числом (операции +, -, *, /).

class Number:
    def __init__(self, n):
        self.number = n

    def __add__ (self, val):
        return self.number + val;

    def __sub__ (self, val):
        return self.number - val;

    def __mul__ (self, val):
        return self.number * val;

    def __truediv__ (self, val):
        return self.number / val;
