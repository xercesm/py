
n = int(input("Введите количество кустов: "))
a = list(map(int, input("Введите урожайность ягод для каждого куста: ").split()))

max_berries = []
for i in range(n):
    if i == 0:
        max_berries.append(a[i] + a[i+1] + a[n-1])
    elif i == n-1:
        max_berries.append(a[i] + a[0] + a[n-2])
    else:
        max_berries.append(a[i] + a[i-1] + a[i+1])

max_berries.sort(reverse=True)
print("Максимальное количество ягод, которое можно собрать с одного куста:", max_berries[0])