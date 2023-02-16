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

    if sign is not '+-*/':
        print('Неверная операция')

    if sign == '+':
        addition(a, b)
    elif sign == '-':
        subtraction(a, b)
    elif sign == '*':
        multiplication(a, b)
    elif sign == '/':
        if b == 0:
            print('На ноль делить нельзя!')
        division(a, b)


if __name__ == '__main__':
    a, b, sign = int(input()), int(input()), input()

    print(self_written_calculator(a, b, sign))
