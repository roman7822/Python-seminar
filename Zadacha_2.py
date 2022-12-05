def pari(lst):
    lst1 = []
    count = -1
    i = 0
    lenf = len(lst) / 2
    while i < lenf:
        lst1.append(lst[i]*lst[count])
        count -= 1
        i += 1
    return lst1

lst = list(map(int, input("Введите числа через пробел:  ").split()))
lst1 = pari(lst)
print(lst)
print(lst1)