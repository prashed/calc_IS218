""""History calculations"""
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class Calculations:
    """Calculations class"""
    # pylint: disable=too-few-public-methods
    history = []

    @staticmethod
    def add_calculation(calculation):
        """Adding a calculation to the history"""
        Calculations.history.append(calculation)
        return True

    @staticmethod
    def clear_history():
        """Clearing calculations from the history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def get_calculation(num):
        """Getting a calculation from the history"""
        return Calculations.history[num]

    @staticmethod
    def count_calculations():
        """the total number of calculations in the history"""
        return len(Calculations.history)

    @staticmethod
    def remove_calculation(num):
        """Clear a specific calculation from the history"""
        Calculations.history.remove(Calculations.history[num])
        return True

    @staticmethod
    def get_calculation_first():
        """the first calculation in the history"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation_first_result():
        """The result of the first calculation in the history"""
        return Calculations.history[0].get_result()

    @staticmethod
    def get_calculation_last():
        """the last calculation in the history"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation_last_result():
        """the result of the last calculation in the history"""
        return Calculations.history[-1].get_result()

    @staticmethod
    def add_addition_calculation(values):
        """Addition object to history with "create" factory method"""
        Calculations.add_calculation(Addition.create(values))
        return True

    @staticmethod
    def add_subtraction_calculation(values):
        """Subtraction object to history with "create" factory method"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation(values):
        """Multiplication object to history with "create" factory method"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation(values):
        """Division object to history with "create" factory method"""
        Calculations.add_calculation(Division.create(values))
        return True
