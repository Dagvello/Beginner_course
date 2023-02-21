def can_bishop_move(x1: int, y1: int, x2: int, y2: int) -> None:
    """Функция определяет, может ли слон попасть с первой клетки на вторую одним ходом"""
    if abs(x1 - x2) == abs(y1 - y2):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    print(can_bishop_move(x1, y1, x2, y2))
