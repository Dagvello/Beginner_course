from unittest import TestCase, main
from calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)
    def test_minus(self):
        self.assertEqual(calculator('5-3'), 2)
    def test_multi(self):
        self.assertEqual(calculator('5*3'), 15)
    def test_divide(self):
        self.assertEqual(calculator('10/5'), 2.0)
if __name__ == '__main__':
    main()
