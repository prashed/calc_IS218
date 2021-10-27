""" This is the increment function"""


def inc(x_value):
    """ Increment Function adds one to the x_value"""
    return x_value + 1


class Calculator:
    """ This is the Calculator class"""

    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(xvalue, yvalue):
    return xvalue - yvalue


# This function multiplies two numbers
def multiply(xvalue, yvalue):
    return xvalue * yvalue


# This function divides two numbers
def divide(xvalue, yvalue):
    try:
        return xvalue / yvalue
    except ZeroDivisionError:
        return "Error: You are dividing by 0!"


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")