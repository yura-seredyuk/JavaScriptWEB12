"""
python -m unittest task1.py

python -m unittest -v task1.py 
-v  - verbose(with details end descriptions)

python -m unittest -v -f task1.py 
-f  - failed(stop after first failed test)

python -m unittest -v task1.DivTest     - run single test case
python -m unittest -v task1.DivTest.test_1     - run single test
"""
import unittest


def div(num_1, num_2):
    return float(num_1)/num_2


class DivTest(unittest.TestCase):
    def test_1(self):
        rez = div(10, 2)
        self.assertEqual(rez, 5.0, 'Incorrect divider!')

    def test_2(self):
        self.assertEqual(div(1, 3), 0.3333333333333333)

    def test_3(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)
    


# print(div(10,2)) # 5.0

# print(div(1,3)) # 0.3333333333333333

# print(div(1,0)) # ZeroDivisionError: float division by zero

