#1. ������� 1 (cycle): �������� ������� cycle_string, ������� ��������� ������ � �����
#����� n � �������� ������� ������ � ���������� ������, ���������� �����������
#���������� ������� ������ n ���. ��������, cycle_string("abc", 3) ������
#������� "abcabcabc".
#def cycle_string(s, n):
#    res = ""
#    for i in range(n):
#        res += s;
#    return res

#print(cycle_string("math", 3))

#2. ������� 2 (count): �������� ������� count_from, ������� ��������� �����
#����� start � ����� ����� n � �������� ������� ������ � ���������� ������ �� n �����
#�����, ������� �� start. ��������, count_from(5, 3) ������ ������� [5, 6, 7].

#def count_from(start, n):
#    mas = []

#    for i in range(n):
#        mas.append(start)
#        start += 1

#    return mas

#print(count_from(5, 3))

#3. ������� 3 (starmap): �������� ������� multiply_elements, ������� ���������
#������ ��������, ��� ������ ������ �������� ��� ����� �����, � ���������� ������
#������������ ����� � ������ �������. ��������, multiply_elements([(1, 2), (3, 4), (5,
#6)]) ������ ������� [2, 12, 30].

#from itertools import starmap

#def mult(x, y):
#    return x * y

#def multiply_elements(lst):
#    res = list(starmap(mult, lst))
#    return res


#print(multiply_elements([(1, 2), (3, 4), (5, 6)]))

#4. ������� 4 (accumulate): �������� ������� accumulate_sums, ������� ���������
#������ ����� ����� � ���������� ������ ����������� ����.
#��������, accumulate_sums([1, 2, 3, 4, 5]) ������ ������� [1, 3, 6, 10, 15].
#from itertools import accumulate

#def accumulate_sums(numbers):
#    res = list(accumulate(numbers))
#    return res

#print(accumulate_sums([1, 2, 3, 4, 5]))

#5. ������� 5 (dropwhile): �������� ������� drop_less_than, ������� ��������� ������
#����� ����� � ����� ����� n � �������� ������� ������ � ���������� ������ �����
#����� �� �������� ������, ������� � ������� �����, ������� �� ������ n.
#��������, drop_less_than([1, 2, 3, 4, 5], 3) ������ ������� [3, 4, 5].

def drop_less_than(lst, n):
    mas = []
    for i in range(len(lst)):
        if(lst[i] >= n):
            mas.append(lst[i])

    return mas

print(drop_less_than([1, 2, 3, 4, 5], 3))