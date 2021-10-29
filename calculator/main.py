""" This is the Calculator object """


class Calculator:
    """ This is the Calculator class"""

    def __init__(self, starting_result=0):
        self.result = starting_result

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, *value):
        """ Add to the result"""
        for values in value:
            self.result += values

        return self.result

    def subtract_number(self, *value):
        """ Subtract from the result """
        for values in value:
            self.result -= values

        return self.result

    def multiply_number(self, *value):
        """ Multiply by the result """
        for values in value:
            self.result *= values

        return self.result

    def divide_number(self, *value):
        """ Divide by the result """
        for values in value:
            self.result /= values

        return self.result
