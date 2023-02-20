def fahrenheit(F: float) -> float:
    """Перевод градусов Фаренгейта в градусы Цельсия"""
    return 5 * (F - 32) / 9


if __name__ == '__main__':
    print(fahrenheit(float(input())))
