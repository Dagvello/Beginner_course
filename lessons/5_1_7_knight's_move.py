def is_knight_move(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Функция проверяет, может ли конь попасть с первой клетки на вторую одним ходом.
    :param x1: Номер столбца первой клетки.
    :param y1: Номер строки первой клетки.
    :param x2: Номер столбца второй клетки.
    :param y2: Номер строки второй клетки.
    :return: Возвращает True, если конь может попасть из первой клетки во вторую одним ходом, иначе False.
    """
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return dx == 2 and dy == 1 or dx == 1 and dy == 2


if __name__ == '__main__':
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    if is_knight_move(x1, y1, x2, y2):
        print('YES')
    else:
        print('NO')
