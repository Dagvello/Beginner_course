def min_and_max(my_list: list) -> int:
    """Функция возвращает наибольшее и наименьшее число в списке"""
    return min(my_list), max(my_list)


if __name__ == '__main__':
    my_list = []
    for i in range(5):
        my_list.append(int(input()))
    print(f'Наименьшее число = {min_and_max(my_list)[0]}')
    print(f'Наибольшее число = {min_and_max(my_list)[1]}')

