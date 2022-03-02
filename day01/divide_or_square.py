import math


class DivideOrSquare:
    def __init__(self):
        pass

    def divide_or_square(self, input_number: float):
        remainder = float(input_number % 5)
        if (remainder == 0):
            return math.sqrt(input_number)
        else:
            return remainder
