from unittest import TestCase, main
from calculator import calculator


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
if __name__ == '__main__':
    main()
