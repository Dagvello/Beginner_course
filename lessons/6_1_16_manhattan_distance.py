def manhattan_distance(lst: list) -> int:
    """Функция нахождения Manhattan distance
     Args:
        lst: Список чисел.

     Returns:
         int: Расстояние

    Raises:
        TypeError: Если элементы списка не могут быть приведены к типу int.

    """
    return abs(lst[0] - lst[2]) + abs(lst[1] - lst[3])


if __name__ == '__main__':
    try:
        my_list = [int(input()) for _ in range(4)]
        print(manhattan_distance(my_list))
    except ValueError:
        print("Ошибка ввода. Проверьте правильность введенных значений.")
