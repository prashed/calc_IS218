"""History testing"""
import pytest
from calculator.history.calculations import Calculations
from calculator.operations.addition import Addition


@pytest.fixture
def clear_history_fixture():  # pylint: disable=redefined-outer-name,unused-argument
    """Fixture - This will clear the history"""
    Calculations.clear_history()


def test_add_calculation_to_history():
    """Adding new calculation to the history test"""
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)
    assert len(Calculations.history) == 1


def test_clear_calculations_history():
    """Removing the calculation history test"""
    values = (1, 2)
    addition = Addition(values)
    Calculations.history.append(addition)
    assert len(Calculations.history) == 2
    assert Calculations.clear_history() is True


def test_get_calculation():
    """Get a calculation from the history test"""
    values = (1, 2)
    addition = Addition(values)
    Calculations.history.append(addition)
    assert Calculations.get_calculation(0).get_result() == 3


def test_count_calculations(clear_history_fixture):
    """How many calculations are in the history test"""
    # pylint: disable=unused-variable,unused-argument,redefined-outer-name
    values = (1, 2)
    for i in range(3):
        Calculations.history.append(Addition(values))
    assert Calculations.count_calculations() == 3


def test_remove_calculation(clear_history_fixture):
    """Deleting a specific calculation"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (1, 1)
    addition = Addition(numbers)
    Calculations.history.append(addition)
    assert Calculations.remove_calculation(0) is True


def test_get_calculation_last(clear_history_fixture):
    """Get last calculation in the history test"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_last() == addition2


def test_get_calculation_last_result(clear_history_fixture):
    """Get the result of the last calculation in the history test"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_last_result() == 9


def test_get_calculation_first(clear_history_fixture):
    """Get the first calculation in history test"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_first() == addition


def test_get_calculation_first_result(clear_history_fixture):
    """Get the result of the first calculation in the history test"""
    # pylint: disable=unused-argument,redefined-outer-name
    numbers = (2, 1)
    numbers2 = (4, 5)
    addition = Addition(numbers)
    addition2 = Addition(numbers2)
    Calculations.history.append(addition)
    Calculations.history.append(addition2)
    assert Calculations.get_calculation_first_result() == 3
