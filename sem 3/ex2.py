
N = int(input())  # Вводим количество элементов в массиве
A = list(map(int, input().split()))  # Вводим элементы массива
X = int(input())  # Вводим число X

closest = A[0]  # Инициализируем переменную closest первым элементом массива A

# Проходим по всем элементам массива и сравниваем их с числом X
for i in range(1, N):
    if abs(A[i] - X) < abs(closest - X):
        closest = A[i]

print(closest)  # Выводим результат