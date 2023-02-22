from math import sqrt


def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Функция вычисляет эвклидовое расстояние"""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == '__main__':
    x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
    print(euclidean_distance(x1, y1, x2, y2))