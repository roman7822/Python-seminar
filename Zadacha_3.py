def minmax (lst):
    max_min = []
    for i in range(len(lst)):
        if lst[i]%1 != 0:
            max_min.append(lst[i]%1)
    return max(max_min) - min(max_min)



lst1 = list(map(float, input("Введите числа через пробел:  ").split()))
print(lst1)
result = minmax(lst1)
print(f'Разница между максимальным и минимальным значением дробной части = {result:.2f}')

