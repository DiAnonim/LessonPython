#balance = {"$": 500}
#print(balance)


#def Withdraw(bal):
#    print("Enter an amount and valuta(ex:500 $)")
#    moneyWith = input().split(" ")
#    b = int(moneyWith[0])
#    v = moneyWith[1]

#    if v in balance:
#        if bal.get(v) >= b:

#            temp = bal.get(v)
#            temp -= b
#            balance.update({v: temp})
#        else:
#            print("There are not enough funds on your balance")
#        print("Do you want to check your balance?")
#        choice = input()
#        if choice == "yes":
#            print(f"Your balance is {bal.get(v)}, valuta {v}")
#    else:
#        print(f"This {v} currency was not found")


#def Deposit(bal):
#    print("Enter an amount and valuta(ex:500 $)")
#    moneyWith = input().split(" ")
#    b = int(moneyWith[0])
#    v = moneyWith[1]

#    if v in balance == True:
#        temp = bal.get(v)
#        temp += b
#        balance.update({v: temp})
#    else:
#        bal.update({v:b})
#        print(f"You have opened a new balance for this currency {v}")

#    print("Do you want to check your balance?")
#    choice = input()
#    if choice == "yes":
#        print(f"Your balance is {b}, valuta {v}")


#while True:
#    print("Do you want withdraw or deposit money?")
#    userChoice = input()

#    if userChoice == "withdraw":
#        Withdraw(balance)
#        print(balance)
#    elif userChoice == "deposit":
#        Deposit(balance)
#    elif userChoice == "exit":
#        break
#    else:
#        print("This option does not exist")


##Написать рекурсивную функцию нахождения степени числа. 

##Input: 
##Enter numbers: 2 3 
##Output: 
##2 to the 3 power is 8 
#def rec(a, b):
#    if b == 1: 
#        return a
#    else: 
#        return a * rec(a, b-1)

#print(rec(2, 3))



#Написать рекурсивную функцию, которая вычисляет сумму всех чисел в диапазоне от a до b. Пользователь вводит a и b. Проиллюстрируйте работу функции примером. 

#Input: 
#Enter numbers: 4 7 
#Output: 
#Sum from 4 to 7 is 22 



#def rec(a, b):
#    if a < b: 
#        return a + rec(a+1, b)
#    else: 
#        return a

#print(rec(4, 7))

 
