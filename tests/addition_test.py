"""Addition testing"""
from calculator.operations.addition import Addition


def test_addition():
    """Addition testing - AAA Testing"""
    numbers = (5, 5)  # ARRANGE
    addition = Addition(numbers)  # ACT
    assert addition.get_result() == 10  # ASSERT
