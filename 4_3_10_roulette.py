def color_odd(n: int) -> str:
    """Функция присваивает четным черный цвет"""
    if n % 2 == 0:
        color = 'черный'
    else:
        color = 'красный'
    return color


def color_even(n: int) -> str:
    """Функция присваивает четным красный цвет"""
    if n % 2 == 0:
        color = 'красный'
    else:
        color = 'черный'
    return color


def roulette(n: int) -> str:
    """Функция определяет диапазон присваивания цвета"""
    if n == 0:
        color = 'зеленый'
        return color
    if 0 < n <= 36:
        if 0 < n <= 10:
            return color_odd(n)
        if 11 <= n <= 18:
            return color_even(n)
        if 19 <= n <= 28:
            return color_odd(n)
        if 29 <= n <= 36:
            return color_even(n)
    else:
        color = 'ошибка ввода'
        return color


if __name__ == '__main__':
    n = int(input())
    print(roulette(n))
