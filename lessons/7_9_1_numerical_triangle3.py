def numerical_triangle(number: int) -> None:
    """
    Функция выводит численный треугольник
    :param number: int
    :return: None
    """
    total = 1
    for i in range(1, number + 1):
        for _ in range(i):
            print(total, end=' ')
            total += 1
        print()


if __name__ == '__main__':
    numerical_triangle(int(input()))
