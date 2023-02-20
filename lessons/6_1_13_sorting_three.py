def sorting_three(my_list: list) -> list:
    """Функция выводит сортированный список"""
    return print(*sorted(my_list), sep='\n')


if __name__ == '__main__':
    my_list = []
    for i in range(3):
        my_list.append(int(input()))
    sorting_three(my_list)