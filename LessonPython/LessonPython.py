#Напишите программу, в которой я ввожу трехзначное число. Найти сумму, произведение его цифр. В случае ввода текста выведите сообщение.  

#def calcSum(number):
#    num1 = number // 100
#    num2 = (number // 10) % 10
#    num3 = number % 10

#    summa = num1 + num2 + num3
#    umnojenie = num1 * num2 * num3

#    return summa, umnojenie

#try:
#    inpNumb = input("Enter number: ")

#    if 99 < int(inpNumb) < 1000:
#        resSum, resUmn = calcSum(int(inpNumb))

#        print(f"The sum: {resSum}")
#        print(f"The product: {resUmn}")

#    else:
#        print("Error: Enter a three-digit number.")

#except ValueError:
#    print("Error: Entered text instead of a number.")



def avg(a, b):
    try:
        result = (a * b) ** 0.5
        return result
    except ValueError:
        raise ValueError("Error: It is impossible to extract the root")

try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Geometric mean = {:.2f}".format(c))
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Error: {e}")
