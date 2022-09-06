"""
pytest test_3.py -v
"""
import pytest
from functions import quadratic_equation as QE


class TestQE:

    def test_NegDescriminant(self):
        qe = QE(2,1,1)
        assert qe is None

    def test_PosDescriminant(self):
        qe = QE(2,1,-1)
        assert  qe == (0.5, -1.0)

    def test_ZeroDescriminant(self):
        qe = QE(1,-4,4)
        assert qe == 2.0

    def test_error(self):
        with pytest.raises(ValueError):
            QE(10, 1, 2)