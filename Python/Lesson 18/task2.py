"""
"""
import unittest
from functions import quadratic_equation as QE


class QETest(unittest.TestCase):

    def test_NegDescriminant(self):
        qe = QE(2,1,1)
        self.assertEqual(qe, None)

    def test_PosDescriminant(self):
        qe = QE(2,1,-1)
        self.assertEqual(qe, (0.5, -1.0))

    def test_ZeroDescriminant(self):
        qe = QE(1,-4,4)
        self.assertEqual(qe, 2.0)

    def test_error(self):
        self.assertRaises(ValueError, QE, 0, 1, 2)