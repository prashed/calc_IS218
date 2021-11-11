"""Division Class"""
from calculator.operations.calculation import Calculation


class Division(Calculation):  # pylint: disable=too-few-public-methods
    """Division Class"""

    def get_result(self):
        """Get the quotient"""
        try:
            quotient = self.values[0]
            for value in self.values[1:]:
                quotient /= value
            return quotient
        except ZeroDivisionError:
            return None
