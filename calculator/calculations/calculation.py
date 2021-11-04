""" Calculation component - base of all calculations done """


class Calculation:  # pylint: disable=too-few-public-methods
    """ Calculation class to be instantiated"""

    def __init__(self, *values):
        self.values = values
