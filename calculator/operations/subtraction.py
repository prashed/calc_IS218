"""Subtraction Class"""
import pprint
from calculator.operations.calculation import Calculation


class Subtraction(Calculation):  # pylint: disable=too-few-public-methods
    """subtraction class"""

    def get_result(self):
        """Get the difference"""
        difference = self.values[0]
        for value in self.values[1:]:
            difference = difference - value
            pprint.pprint(str(difference) + " - " + str(value))
        return difference
