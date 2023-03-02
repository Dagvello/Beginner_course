def together(number: int) -> int:
    """Функция вычисляет сумму его цифр; количество цифр в нем;
    произведение его цифр; среднее арифметическое его цифр;
    его первую цифру; сумму его первой и последней цифры."""

    def summa(number: int) -> None:
        """Сумма цифр"""
        in_total = 0
        while number > 0:
            num = number % 10
            in_total += num
            number = number // 10
        print(in_total)

    def number_of_digits(number: int) -> None:
        """Количество цифр"""
        count = 0
        while number > 0:
            num = number % 10
            count += 1
            number = number // 10
        print(count)

    def product_of_digits(number: int) -> None:
        """Произведение цифр"""
        product = 1
        while number > 0:
            num = number % 10
            product *= num
            number = number // 10
        print(product)

    def average(number: int) -> None:
        """Среднее арифметическое"""
        in_total = 0
        count = 0
        while number > 0:
            num = number % 10
            in_total += num
            count += 1
            number = number // 10
            avr = in_total / count
        print(avr)

    def first_digit(number: int) -> None:
        """Первая цифра"""
        count = 0
        digits = number
        while number > 0:
            num = number % 10
            count += 1
            number = number // 10
            f_digit = digits // (10 ** (count - 1))
        print(f_digit)

    def first_and_last(number: int) -> None:
        """Сумма первой и последней цифры"""
        count = 0
        digits = number
        while number > 0:
            num = number % 10
            count += 1
            number = number // 10
            f_digit = digits // (10 ** (count - 1))
            summa = f_digit + digits % 10
        print(summa)

    summa(number)
    number_of_digits(number)
    product_of_digits(number)
    average(number)
    first_digit(number)
    first_and_last(number)


if __name__ == '__main__':
    together(int(input()))
