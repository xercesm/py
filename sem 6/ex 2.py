
def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))

result = find_indexes(lst, min_val, max_val)
print("Индексы элементов массива:", result)