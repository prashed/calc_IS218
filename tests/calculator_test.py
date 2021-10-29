"""Testing the Calculator"""
import pytest
from calculator.main import Calculator


def test_calculator_result():
    """ Testing result=0 """
    calc = Calculator()
    assert calc.result == 0


def test_calculator_get_result():
    """ Testing get result """
    calc = Calculator()

    assert calc.get_result() == 0


def test_calculator_add():
    """ Testing addition operation """
    calc = Calculator()
    calc.add_number(1)
    assert calc.result == 1


def test_calculator_subtract():
    """ Testing subtraction operation """
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1


def test_calculator_multiply():
    """ Testing multiplication operation """
    calc = Calculator()
    calc.multiply_number(1)
    assert calc.get_result() == 0


def test_calculator_divide():
    """ Testing division operation """
    calc = Calculator()
    calc.divide_number(1)
    assert calc.get_result() == 0


def test_calculator_divide_by_zero():
    """ Testing division by zero exception"""
    with pytest.raises(ZeroDivisionError):
        calc = Calculator()
        calc.add_number(10)
        calc.divide_number(0)
