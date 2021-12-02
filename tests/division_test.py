"""Division testing"""
import pytest
from calculator.operations.division import Division


def test_division():
    """Division testing - AAA Testing"""
    numbers = (10, 2)  # ARRANGE
    division = Division(numbers)  # ACT
    assert division.get_result() == 5  # ASSERT


def test_division_zero():
    """Testing division by zero"""
    # Arrange
    numbers = (10, 0)
    division = Division(numbers)
    # Act
    # Assert
    with pytest.raises(ZeroDivisionError):
        division.get_result()
