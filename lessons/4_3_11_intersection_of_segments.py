def intersection(a1: int, b1: int, a2: int, b2: int) -> int:
    """Нахождение пересечения отрезков"""
    A = set(x for x in range(a1, b1+1, 1))
    B = set(x for x in range(a2, b2+1, 1))
    C = A & B
    my_lst = sorted(list(C))
    if len(my_lst) == 0:
        return print('пустое множество')
    if len(my_lst) == 1:
        return print(my_lst[0])
    return print(my_lst[0], my_lst[-1])


if __name__ == '__main__':
    a1 = int(input())
    b1 = int(input())
    a2 = int(input())
    b2 = int(input())
    intersection(a1, b1, a2, b2)
