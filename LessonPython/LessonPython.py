
# 2

from ast import Mult


inpA = 9
inpB = 5


def MultipTable(a, b):
    for i in range(0, a + 1):
        for j in range(0, i):
            if j <= i:
                print("*", end=" ")
       
        print()


MultipTable(int(inpA), int(inpB))