
def power(A, B):
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        return A * power(A, B-1)

A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))

result = power(A, B)
print("Результат возведения числа A в степень B:", result)