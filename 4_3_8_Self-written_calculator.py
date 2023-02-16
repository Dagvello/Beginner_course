def self_written_calculator(a: int, b: int, sign: str) -> int or float:
    """Самописный калькулятор"""

    def addition(a: int, b: int) -> int:
        """Сложение"""
        return a + b

    def subtraction(a: int, b: int) -> int:
        """Вычитание"""
        return a - b

    def multiplication(a: int, b: int) -> int:
        """Умножение"""
        return a * b

    def division(a: int, b: int) -> float:
        """Деление"""
        return a / b

    if sign == '+' or sign == '-' or sign == '*' or sign == '/':
        if sign == '+':
            return print(addition(a, b))
        elif sign == '-':
            return print(subtraction(a, b))
        elif sign == '*':
            return print(multiplication(a, b))
        elif sign == '/':
            if b == 0:
                return print('На ноль делить нельзя!')
            return print(division(a, b))
    else:
        return print('Неверная операция')


if __name__ == '__main__':
    a, b, sign = int(input()), int(input()), input()

    self_written_calculator(a, b, sign)
