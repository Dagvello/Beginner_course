def numerical_triangle(number: int) -> None:
    """
    Функция печатает численный треугольник
    :param number: integer
    :return: None
    """
    for j in range(1, number + 1):
        for i in range(1, j + 1):
            print(i, end='')
        for i in range(j - 1, 0, -1):
            print(i, end='')
        print()


if __name__ == '__main__':
    numerical_triangle(int(input()))
