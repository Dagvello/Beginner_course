def meetin_gtime(s: float, v1: float, v2: float) -> float:
    """Время встречи двух старушек"""
    return s / (v1 + v2)


if __name__ == '__main__':
    S, V1, V2 = float(input()), float(input()), float(input())
    print(meetin_gtime(S, V1, V2))
