#�������� ����������� �������, ������� ��������� ����� ���� ����� � ��������� �� a �� b. ������������ ������ a � b. ���������������� ������ ������� ��������. 

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


#�������� ����������� �������, ������� ������� N ����� � ���, ����� N ������ ������������. ���������������� ������ ������� ��������. 
#Input: 
#Enter amount of stars: 10 
 
#Output: 
#* * * * * * * * * *  

def printStar(n):
    if int(n)>0: 
        print("*", end=" ")
        return printStar(int(n)-1)

print(printStar(input()))
 
