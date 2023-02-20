def interesting_number(number: list) -> None:
    """ Функция определяет интересное число.
        Число интересное, если в нем разность максимальной и минимальной цифры
        равняется средней по величине цифре.
    """
    num_list = sorted(number)
    if int(num_list[2]) - int(num_list[0]) == int(num_list[1]):
        print('Число интересное')
    else:
        print('Число неинтересное')


if __name__ == '__main__':
    number = list(input())
    interesting_number(number)
