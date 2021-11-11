"""Division testing"""
from calculator.operations.division import Division


def test_division():
    """Division testing - AAA Testing"""
    numbers = (10, 2)  # ARRANGE
    division = Division(numbers)  # ACT
    assert division.get_result() == 5  # ASSERT
