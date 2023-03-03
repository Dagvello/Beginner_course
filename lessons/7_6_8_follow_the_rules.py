def follow_the_rules(number: int) -> int:
    """Функция выводит числа от 1 до n включительно за исключением"""
    for i in range(1, number + 1):
        if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
            continue
        print(i)


if __name__ == '__main__':
    follow_the_rules(int(input()))
