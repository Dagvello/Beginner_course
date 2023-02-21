def triangle_inequality(lst: list[int]) -> bool:
    """ Функция которая принимает список из трёх положительных чисел и определяет,
        существует ли невырожденный треугольник с такими сторонами.
    """
    lst = sorted(lst)

    return lst[-1] < lst[0] + lst[1]


if __name__ == '__main__':
    my_list = [int(input()) for _ in range(3)]

    try:
        triangle_inequality = triangle_inequality(my_list)
        if triangle_inequality:
            print('YES')
        else:
            print('NO')
    except ValueError as e:
        print(f"Ошибка: {e}")