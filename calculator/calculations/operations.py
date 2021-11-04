""" Mathematical operations """
from calculator.calculations.calculation import Calculation


class Addition(Calculation):
    """ calculating the sum of all numbers """

    def get_result(self):
        """ calculating the sum of value in self.values """
        total = 0
        for value in self.values:
            total += value
        return total


class Subtraction(Calculation):
    """ save the first result and subtract the other numbers """

    def get_result(self):
        """ the sum of the values in self.values """
        total = self.values[0]
        for value in self.values[1:]:
            total -= value

        return total


class Multiplication(Calculation):
    """ save the first result and multiply the other numbers """

    def get_result(self):
        """ the sum of the values in self.values """
        total = self.values[0]

        for value in self.values[1:]:
            total *= value

        return total


class Division(Calculation):
    """ save the first result and divide the other numbers """

    def get_result(self):
        """ the sum of the values in self.values """
        total = self.values[0]

        for value in self.values[1:]:
            total /= value

        return total
