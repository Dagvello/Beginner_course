from math import sqrt


def arithmetic(a: float, b: float) -> float:
    """Функция вычисляющая среднее арифметическое"""
    return (a + b) / 2


def geometric(a: float, b: float) -> float:
    """Функция вычисляющая среднее геометрическое"""
    return sqrt(a * b)


def harmonic(a: float, b: float) -> float:
    """Функция вычисляющая среднее гармоническое"""
    return 2 * a * b / (a + b)


def quadratic(a: float, b: float) -> float:
    """Функция вычисляющая среднее квадратичное"""
    return sqrt((a ** 2 + b ** 2) / 2)


if __name__ == '__main__':
    A, B = float(input()), float(input())
    print(arithmetic(A, B))
    print(geometric(A, B))
    print(harmonic(A, B))
    print(quadratic(A, B))
