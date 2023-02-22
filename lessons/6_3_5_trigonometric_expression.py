from math import *


def expression(x_degree: float) -> float:
    """Тригонометрическое выражение"""
    r = radians(x_degree)
    return sin(r) + cos(r) + tan(r) ** 2


if __name__ == '__main__':
    x_degree = float(input())
    print(expression(x_degree))
