def min_and_max(number: int) -> None:
    """Функция печатает минимальную и максимальную цифру в числе"""
    minimum = 9
    maximum = 0
    while number > 0:
        num = number % 10
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        number = number // 10
    print('Максимальная цифра равна', maximum)
    print('Минимальная цифра равна', minimum)


if __name__ == '__main__':
    min_and_max(int(input()))
