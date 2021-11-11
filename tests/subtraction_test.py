"""Subtraction testing"""
from calculator.operations.subtraction import Subtraction


def test_subtraction():
    """Subtraction testing - AAA Testing"""
    numbers = (10, 5)  # ARRANGE
    subtraction = Subtraction(numbers)  # ACT
    assert subtraction.get_result() == 5  # ASSERT
