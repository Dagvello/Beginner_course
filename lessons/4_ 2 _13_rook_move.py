def rook_move(a: int, b: int, c: int, d: int) -> bool:
    """Функция определяет, может ли ладья попасть с первой клетки на вторую одним ходом"""
    return a == c or b == d


if __name__ == '__main__':
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    try:
        rook = rook_move(x1, y1, x2, y2)
        if rook:
            print('YES')
        else:
            print('NO')
    except ValueError as e:
        print(f"Ошибка: {e}")
