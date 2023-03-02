def second_digit(number: int) -> int:
    """Функция возвращает вторую с начала цифру числа"""
    count = 0
    digits = number
    while number > 0:
        count += 1
        number = number // 10
    digittwo = (digits // (10 ** (count - 2))) % 10
    return digittwo


if __name__ == '__main__':
    print(second_digit(int(input())))
