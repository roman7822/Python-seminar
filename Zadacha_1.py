def sum(lst1):
    sum = 0
    for i in range (1, len(lst1), 2):
        sum += lst1[i]
    return sum

# list = [2, 3, 5, 9, 3]
lst = list(map(int, input("Введите числа через пробел:\n").split()))
result = sum(lst)
print(lst)
print(f'Сумма элементов, стоящих на нечетной позиции = {result}')