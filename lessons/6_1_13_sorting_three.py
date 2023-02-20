def sorting_three(my_list: list) -> None:
    """Функция выводит сортированный список от большего к меньшему"""
    return print(*sorted(my_list, reverse=True), sep='\n')


if __name__ == '__main__':
    my_list = []
    for i in range(3):
        my_list.append(int(input()))
    sorting_three(my_list)
