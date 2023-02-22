from math import pi


def area(R: float) -> float:
    """Функция вычисления площади круга"""
    return pi * R ** 2


def length(R: float) -> float:
    """Функция вычисления длинны окружности"""
    return 2 * pi * R


if __name__ == '__main__':
    R = float(input())
    print(area(R))
    print(length(R))
