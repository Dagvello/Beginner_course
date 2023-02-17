def intersection(a1: int, b1: int, a2: int, b2: int) -> str or int:
    """Нахождение пересечения отрезков"""
    if b1 < a2:
        return print('пустое множество')
    elif b1 == a2:
        return print(b1)

    else:
        if b1 < b2:
            return print(a2, b1)
        else:
            return print(a2, b2)


if __name__ == '__main__':
    a1 = int(input())
    b1 = int(input())
    a2 = int(input())
    b2 = int(input())
    intersection(a1, b1, a2, b2)
