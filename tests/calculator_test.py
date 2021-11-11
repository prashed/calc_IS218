""" Testing calculator operations"""
from calculator.calculator import Calculator


def test_calculator_add():
    """Addition test"""
    my_tuple = (1, 2)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 3


def test_calculator_subtract():
    """Subtraction test"""
    my_tuple = (10, 2)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 8


def test_calculator_multiply():
    """Multiplication test"""
    my_tuple = (5, 5)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 25


def test_calculator_divide():
    """Division test"""
    my_tuple = (10, 2)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 5


def test_calculator_divide_zero():
    """Exception for division by zero test"""
    my_tuple = (10, 0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() is None
