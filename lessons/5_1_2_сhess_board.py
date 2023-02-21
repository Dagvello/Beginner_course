def chess_board(a: int, b: int, c: int, d: int) -> bool:
    """Функция  определяет имеют ли указанные клетки один цвет или нет"""
    return (a + b + c + d) % 2 == 0


if __name__ == '__main__':
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    if chess_board(x1, y1, x2, y2):
        print('YES')
    else:
        print('NO')
