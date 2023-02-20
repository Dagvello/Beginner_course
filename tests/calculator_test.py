from unittest import TestCase, main
from lessons.calculator import calculator


class CalculatorTest(TestCase):
    """Тесты для функции calculator"""

    def test_plus(self):
        """Тест функции плюс"""
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        """Тест функции минус"""
        self.assertEqual(calculator('5-3'), 2)

    def test_multi(self):
        """Тест функции умножения"""
        self.assertEqual(calculator('5*3'), 15)

    def test_divide(self):
        """Тест функции деления"""
        self.assertEqual(calculator('10/5'), 2.0)

    def test_no_signs(self):
        """Функция проверки наличие знака"""
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-*/)', e.exception.args[0])

    def test_two_signs(self):
        """Функция проверки наличие более одного знака"""
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и один знак', e.exception.args[0])

    def test_many_signs(self):
        """Функция проверки наличие разных знаков"""
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('Выражение должно содержать 2 целых числа и один знак', e.exception.args[0])

    def test_no_ints(self):
        """Функция проверки, что число целое"""
        with self.assertRaises(ValueError) as e:
            calculator('2.0+3.0')
        self.assertEqual('Выражение должно содержать 2 целых числа и один знак', e.exception.args[0])

    def test_strings(self):
        """Функция проверки, что число целое"""
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Выражение должно содержать 2 целых числа и один знак', e.exception.args[0])


if __name__ == '__main__':
    main()
