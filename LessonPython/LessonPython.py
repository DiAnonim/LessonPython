

# 1
inpA = input()
inpB = input()

if int(inpA) % int(inpB) == 0:
    print("divisible")
else:
    print("not divisible")



#2

inpYear = input();

def LeapYear(year):
    if int(year)%4==0 and int(year) % 100 != 0 or int(year)%400==0: print("Leap")
    else: print("Not Leap")

LeapYear(inpYear);



#3

inpN= input();

def cntProgram(cnt):
    if int(cnt) == 1: print(f"{cnt} Programmist")
    elif 1 < int(cnt) < 5 : print(f"{cnt} Programmista")
    elif 4 < int(cnt) < 100 : print(f"{cnt} Programmistov")
    else: print("There are no programmers")

cntProgram(inpN);



#4
i = 0;
while i < 21:
    n = 2**i
    print(n)
    i += 1


#5

from ast import Mult


inpA = input()
inpB = input()
inpC = input()
inpD = input()


def MultipTable(a, b, c, d):
    for i in range(a, b+1):
        print(f"{i}")
        for j in range(c, d+1):
            res = j*i
            print(f"{j} {res}")

MultipTable(int(inpA), int(inpB), int(inpC), int(inpD),)