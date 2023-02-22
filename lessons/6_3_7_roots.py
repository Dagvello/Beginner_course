from math import sqrt


def discriminant(a: float, b: float, c: float) -> float:
    """Функция вычисляет дискриминант"""
    return b ** 2 - 4 * a * c


if __name__ == '__main__':
    A, B, C = float(input()), float(input()), float(input())
    D = discriminant(A, B, C)
    if D < 0:
        print('Нет корней')
    elif D == 0:
        print(-B / (2 * A))
    else:
        x1 = (-B - sqrt(D)) / (2 * A)
        x2 = (-B + sqrt(D)) / (2 * A)
        if x1 < x2:
            print(x1, x2, sep='\n')
        else:
            print(x2, x1, sep='\n')
