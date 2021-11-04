"""Testing the Calculator"""
import pytest
from calculator.main import Calculator


def test_add():
    """ Addition test """
    calc = Calculator()

    total = calc.add_number(1, 2, 3)

    assert total == 6


def test_get_first_calculation():
    """ first calc in calc history test """
    calc = Calculator()

    calculation = calc.get_first_calculation()

    assert calculation.get_result() == 6


def test_add_and_get_last_calculation():
    """ last calc in calc history test """
    calc = Calculator()

    calc.add_number(3, 4)
    calc.add_number(5, 5)
    calculation = calc.get_last_calculation()

    assert calculation.get_result() != 7
    assert calculation.get_result() == 10


def test_number_of_calculations_in_history():
    """ check if all calcs are in calc history """
    calc = Calculator()

    assert calc.get_num_of_calculations() == 3


def test_remove_calculation_from_history():
    """ test if removing 2nd index makes it the last in calc history"""
    calc = Calculator()

    calc.remove_from_history(2)
    calculation = calc.get_last_calculation()

    assert calculation.get_result() == 7


def test_number_of_calculations_in_history_after_clearing():
    """ clearing calc history test """
    calc = Calculator()

    calc.clear_history()

    assert calc.get_num_of_calculations() == 0


def test_calculator_subtract():
    """ Subtraction test """
    calc = Calculator()

    calc.subtract_number(10, 8)

    calculation = calc.get_last_calculation()

    assert calculation.get_result() == 2


def test_calculator_multiply():
    """ Multiplication test """
    calc = Calculator()

    calc.multiply_number(2, 3, 2)

    calculation = calc.get_last_calculation()

    assert calculation.get_result() == 12


def test_calculator_divide():
    """ Division test """
    calc = Calculator()

    calc.divide_number(20, 2)

    calculation = calc.get_last_calculation()

    assert calculation.get_result() == 10


def test_calculator_divide_by_zero():
    """ Division by 0 exception test """

    with pytest.raises(ZeroDivisionError):
        calc = Calculator()
        calc.divide_number(10, 0)
