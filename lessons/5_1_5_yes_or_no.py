# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO»

def yes_or_no(number: int) -> None:
    """Функция выводит YES или NO в зависимости от условий"""
    if number % 2 != 0:
        return print('YES')
    else:
        if 2 <= number <= 5:
            return print('NO')
        elif 6 <= number <= 20:
            return print('YES')
        else:
            if number > 20:
                return print('NO')


if __name__ == '__main__':
    number = int(input())
    yes_or_no(number)
