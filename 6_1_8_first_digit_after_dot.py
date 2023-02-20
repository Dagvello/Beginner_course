def first_digit_after_dot(number: float) -> int:
    """Функция выводит первую цифру после точки"""
    left, right = str(number).split('.')
    return int(right[0])


if __name__ == '__main__':
    print(first_digit_after_dot(float(input())))