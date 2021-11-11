"""Multiplication Class"""
from calculator.operations.calculation import Calculation


class Multiplication(Calculation):  # pylint: disable=too-few-public-methods
    """Multiplication Class"""

    def get_result(self):
        """Get the product"""
        product = 1
        for value in self.values:
            product *= value
        return product
