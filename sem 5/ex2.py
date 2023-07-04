def sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum(a+1, b-1)
    else:
        return sum(a-1, b+1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

result = sum(a, b)
print("Сумма чисел a и b:", result)