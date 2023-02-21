def is_beautiful_number(number: int) -> bool:
    """Назовем число красивым, если оно является четырехзначным и делится нацело на
       7 или на 17. Напишите программу, определяющую, является ли введённое число красивым.
       Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
    """
    return number % 7 == 0 or number % 17 == 0 or len(str(number)) == 4


if __name__ == '__main__':

    try:
        beautiful_number = is_beautiful_number(int(input()))
        if beautiful_number:
            print('YES')
        else:
            print('NO')
    except ValueError as e:
        print(f"Ошибка: {e}")