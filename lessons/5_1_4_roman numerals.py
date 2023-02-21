def roman_numerals(number: str) -> str:
    """Функция считывает целое число и выводит соответствующую ему римскую цифру"""
    if not number.isdigit() or int(number) <= 0 or int(number) > 10:
        return 'ошибка'
    roman_numerals_list = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
    return roman_numerals_list[int(number)]


if __name__ == '__main__':
    number = input()
    print(roman_numerals(number))
