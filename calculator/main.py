"""" This is the Calculator object """
from calculator.calculations.operations import Addition, Subtraction, Multiplication, Division


class Calculator:
    """ Calculator class"""

    history = []

    @staticmethod
    def add_number(*values):
        """ add to the result """
        total = Addition(*values)

        Calculator.history.append(total)

        return total.get_result()

    @staticmethod
    def subtract_number(*values):
        """ subtract from result """
        total = Subtraction(*values)

        Calculator.history.append(total)

        return total.get_result()

    @staticmethod
    def multiply_number(*values):
        """ multiply by a number """
        total = Multiplication(*values)

        Calculator.history.append(total)

        return total.get_result()

    @staticmethod
    def divide_number(*values):
        """ divide by a number """
        total = Division(*values)

        Calculator.history.append(total)

        return total.get_result()

    @staticmethod
    def get_first_calculation():
        """ the first calc in calc history """
        return Calculator.history[0]

    @staticmethod
    def get_last_calculation():
        """ most recent calc in calc history """
        return Calculator.history[-1]

    @staticmethod
    def get_num_of_calculations():
        """ return total calcs in calc history """
        return len(Calculator.history)

    @staticmethod
    def clear_history():
        """ clear calcs in calc history """
        Calculator.history = []

    @staticmethod
    def remove_from_history(index):
        """ clear calc in index of calc history """
        Calculator.history.pop(index)
