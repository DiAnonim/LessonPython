#1. ��� ������. ����������, �������� �� �� ��������� ������������ (�� ���� ����� ��, ��� ������ ������� ����� ������ ������ �����������).
#�������� YES, ���� ������ ��������� ���������� � NO � ��������� ������.
#������� �������� � ���� ������� IsAscending(A).

#def IsAscending(*A):
#    size = len(A)
#    if size == 0 or size == 1: return print("Yes")
#    for i in range(size-1):
#        if A[i] > A[i + 1]: return print("No")
#    return print("Yes")

#IsAscending(1, 5, 2, 4)


#��� ������ �����, ����� a � ����������� ����� k. �������� ������ k-�� �� ����� ��������� � ������� ����� a. 
#���� ����� a ����������� � ������� ����� k ���, �������� ����� -1.
#������� �������� � ���� ������� KthAppearance(A, a, k).

#def KthAppearance(*A, a, k):
#    cnt = 0
#    for i in range(len(A)):
#        if A[i] == a:
#            cnt += 1
#            if cnt == k:
#                return i  # ����� k-� ���������, ���������� ������
#    return -1 

#lst = [1, 2, 1, 3, 2, 3, 2, 3, 2, 2]
#a= 3
#k= 1
#res = KthAppearance(lst, a, k)
#print(res)

#��������� ������������� ��������, ��� ����� �� ����� ������ ���������������� ������. 
#������, ����� �����, ���� �� ����� ��������� �����, ����� ���� ������ ��� ��������� ����� ������������ ������.
#��������, ����� ����� �������� ����� ������� ������������.
#�������� ���������, ������� �� �������� ���������� � ������������� � ���������� ������ �� �������� ����� ��������� ������������ ����� �������������,
#��� ������ ����� ��������� � �����, ��� ���� ��������� ��������� ����� ��� ����� ����� �����.
#��������� �������� �� ���� � ����� ������ ����� S ������ ���������� ����� �� �����, � ����� N � ���������� �������������, 
#����� ����� ���� N ����� � ����� ������ ������� ������������, ���������� ������ � ��������� ������.
#�������� ���������� ���������� �������������, ��� ������ ����� ���� �������� � �����.

#def max_users_in_archive(S, userData):
#    userData.sort()

#    userCnt = 0
#    totalData = 0

#    for data in userData:
#        totalData += data
#        if totalData <= S:
#            userCnt += 1
#        else:
#            break

#    return userCnt

#S = int(input("Enter the amount of free disk space: "))
#N = int(input("Enter the number of users: "))
#userData = [int(input(f"The amount of user data {i + 1}: ")) for i in range(N)]

#result = max_users_in_archive(S, userData)
#print(f"Maximum number of users: {result}")


#����� ������������� ��������� �������� ����� ����� �������� �����, ����� �������� ����������� �� �����. 
#�� ������� N ����� ������ �������, ����� � ���� �����������. ������, ����� ��� ���������, ���������, ��� � ������� �������� ����� ���� ����� �� 1 ��������.
#�������� �����, ������ ���������� ������� ���������� �� ������ �� ���� (� ���������, ��� ���������� ����� � ������ ������������,
#������� ������ ��������� ���� ����������� �� ����� ������). ������ �������� ����� ����������, ������� �������� ��������� �� ��������� ���� �����������. 
#�����������, �������� ����� ��������� ��� ����� ������� �����.
#� ������ ������ �������� N ����� ����� ������, �������� ���������� � ���������� �� ������ �� ����� ����������� ��������.
#�� ������ ������ �������� N ����� � ������ �� ������ ������ ��������� � �����.
#�������� ���� ����� ����� � ���������� �����, ������� �������� ��������� �� �������� ���� �����������.

#def min_TaxiCost(distances, tariffs):
#    total_cost = sum(dist * tariff for dist, tariff in zip(distances, tariffs))
#    return total_cost

#dist = list(map(int, input().split()))
#tariffs = list(map(int, input().split()))

#result = min_TaxiCost(dist, tariffs)
#print(result)


#���� ������������������ �����, ��������� ������ �� ����� 1, ..., 9. ������������������ ����������� ������ 0. ������ ����� �������� � ��������� ������.
#�����������, ������� ��� � ���� ������������������ ����������� �������� 1, 2, ..., 9. ��������� ��� ������������������ ��������� ����� � ������ ������.
#��������� ������ ������� ����� 9 �����: ���������� ������, �����, ..., ������� � ������ ������������������.

#cnt = [0] * 9

#while True:
#    num = int(input())
#    if num == 0:
#        break
#    elif 1 <= num <= 9:
#        cnt[num - 1] += 1

#for c in cnt:
#    print(c, end=" ")


#�������� ���������, � ������� ���������� ������� ������ ����� �� ������. 

#def firstWord(inp):
#    words = inp.split()
#    if words:
#        return words[0]
#    else:
#        return "Empty str"

#inp = input("Enter string: ")

#res = firstWord(inp)
#print("First word in string:", res)

#�������� ���������, ������� �������� ���� �� ������.  

#import re

#def searchDate(input_string):
#    date_pattern = re.compile(r'\b(\d{2}[\./]\d{2}[\./]\d{4})\b')

#    match = date_pattern.search(input_string)

#    if match:
#        return match.group(1)
#    else:
#        return "Date not found"

#inp = input("Enter string: ")

#res = searchDate(inp)
#print("Date retrieved:", res)


#�������� ���������, � ������� � ����� ���������� �����. ���������� ��������� ������������ ������� ����������� ������

import re

def searchPhoneNumber(numb):
    phone_pattern = re.compile(r'^\+?[0-9]{1,3}[-.\s]?[0-9]{1,}$')

    return bool(phone_pattern.match(numb))

phoneNumber = input("Enter Phone number: ")

print(searchPhoneNumber(phoneNumber))





