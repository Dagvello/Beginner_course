def dog_age(n: int) -> int:
    """Функция переводит возраст собаки в человеческий"""
    if 0 <= n < 2:
        return n * 10.5
    else:
        return 21 + (n - 2) * 4


if __name__ == '__main__':
    age = int(input())
    print(dog_age(age))
