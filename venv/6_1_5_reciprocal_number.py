def reciprocal_number(n: float) -> float:
    """Обратное число"""
    return 1/n


if __name__ == '__main__':
    n = float(input())
    if n == 0:
        print('Обратного числа не существует')
    else:
        print(reciprocal_number(n))