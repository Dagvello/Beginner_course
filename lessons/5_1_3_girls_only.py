def girls_only(age: int, gender: str) -> bool:
    """Функция определяет возраст и пол"""
    return 10 <= age <= 15 and gender == "f"


if __name__ == '__main__':
    age, gender = int(input()), input()
    if girls_only(age, gender):
        print('YES')
    else:
        print('NO')
