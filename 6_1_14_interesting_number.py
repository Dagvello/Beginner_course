def is_interesting_number(number_list: list[int]) -> bool:
    """ Функция определяет интересное число.
        Число интересное, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре
    """
    if len(number_list) != 3:
        raise ValueError("Неверное количество цифр в числе")
    if not all(isinstance(n, int) and 0 <= n <= 9 for n in number_list):
        raise ValueError("Неверный формат входных данных")
    num_list = sorted(number_list)
    return int(num_list[2]) - int(num_list[0]) == int(num_list[1])


if __name__ == '__main__':
    number_str = input("Введите список цифр через запятую: ")
    number_list = list(map(int, number_str.split(",")))
    try:
        is_interesting = is_interesting_number(number_list)
        if is_interesting:
            print('Число интересное')
        else:
            print('Число неинтересное')
    except ValueError as e:
        print(f"Ошибка: {e}")

