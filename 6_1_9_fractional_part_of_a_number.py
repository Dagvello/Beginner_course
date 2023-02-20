
def fractional_part_of_a_number(number: float) -> float:
    """Функция выводит дробную часть числа"""
    left, right = str(number).split('.')
    return float(str('0.') + right)


if __name__ == '__main__':
    print(fractional_part_of_a_number(float(input())))