# Функция, которая проверяет является ли число простым
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# функция, которая ищет блищайший простой делитель
def least_prime_divisor(x):
    if is_prime(x):
        return x
    else:
        for i in range(3, int(x ** 0.5) + 1):
            if x % i == 0 and is_prime(i):
                return i

def right_subpolygon(N):
    if N % 3 == 0:
        return 3
    elif N % 4 == 0:
        return 4
    else:
        return least_prime_divisor(N)

N = int(input("Введите количество вершин : "))
print(right_subpolygon(N))
