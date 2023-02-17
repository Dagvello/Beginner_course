def area(a: float, b: float) -> float:
    """Площадь прямоугольного треугольника"""
    S = (a * b) / 2
    return S


if __name__ == '__main__':
    A = float(input())
    B = float(input())
    print(area(A, B))
