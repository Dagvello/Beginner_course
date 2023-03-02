def smallest_divisor(number: int) -> int:
    """Функция возвращает наименьший делитель числа отличный от единицы"""
    for i in range(2, number + 1):
        if number % i == 0:
            return i
    return i


if __name__ == '__main__':
    print(smallest_divisor(int(input())))
