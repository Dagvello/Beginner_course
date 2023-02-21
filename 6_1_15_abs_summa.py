def abs_summa(list: list[float]) -> float:
    """Функция суммирует все абсолютные значения списка"""
    return sum(abs(x) for x in list)


if __name__ == '__main__':
    my_list = [abs(float(input())) for _ in range(5)]
    print(abs_summa(my_list))
