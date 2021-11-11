"""Multiplication testing"""
from calculator.operations.multiplication import Multiplication


def test_multiplication():
    """Multiplication testing - AAA Testing"""
    numbers = (5, 5)  # ARRANGE
    multiplication = Multiplication(numbers)  # ACT
    assert multiplication.get_result() == 25  # ASSERT
