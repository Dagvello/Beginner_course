def abs_sum(lst: list[float]) -> float:
    """
    Функция суммирует все абсолютные значения списка.

    Args:
        lst: Список чисел.

    Returns:
        Сумма абсолютных значений списка.

    Raises:
        TypeError: Если элементы списка не могут быть приведены к типу float.

    """
    return sum(map(abs, lst))


if __name__ == '__main__':
    try:
        my_list = [float(input()) for _ in range(5)]
        print(abs_sum(my_list))
    except ValueError:
        print("Ошибка ввода. Проверьте правильность введенных значений.")
