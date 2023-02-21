def queen_move(x1: int, y1: int, x2: int, y2: int) -> None:
    """ Функция должна вывести «YES», если из первой клетки ходом ферзя можно попасть во вторую
        или «NO» в противном случае"""
    if x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
    print(queen_move(x1, y1, x2, y2))
