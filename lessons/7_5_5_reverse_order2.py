def reverse_order(number: int) -> int:
    """Функция преобразует натуральное число в число из цифр в обратном порядке"""
    while number > 0:
        num = number % 10
        print(num, end='')
        number = number // 10


if __name__ == '__main__':
    reverse_order(int(input()))
