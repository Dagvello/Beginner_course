def ordered_digits(number: int) -> bool:
    """Функция, которая определяет, является ли последовательность его цифр
       при просмотре справа налево упорядоченной по неубыванию
    """
    while number > 0:
        num1 = number % 10
        number = number // 10
        num2 = number % 10
        if num1 <= num2:
            flag = True
        else:
            if num2 != 0:
                flag = False
                return flag
    return flag


if __name__ == '__main__':
    if ordered_digits(int(input())):
        print('YES')
    else:
        print('NO')
