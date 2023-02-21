def beginning_of_the_century(n: int) -> bool:
    """Функция определяет, оканчивается ли год с данным номером на два нуля"""
    return n % 100 == 0


if __name__ == '__main__':
    year = int(input())
    if beginning_of_the_century(year):
        print('YES')
    else:
        print('NO')
