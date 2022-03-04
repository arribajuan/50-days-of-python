import math


class DivideOrSquare:
    def __init__(self):
        pass

    def divide_or_square(self, input_number: float) -> float:
        """
        Takes one argument (a number), and returns the square root of the number if it is divisible by 5,
        returns its remainder if it is not divisible by 5.
        For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.

        :rtype: float
        :param input_number: Number to divide or square
        :return: the square root of the number if it is divisible by 5, or its remainder if it is not divisible by 5.
        """
        remainder = float(input_number % 5)
        if remainder == 0.0:
            return math.sqrt(input_number)
        else:
            return remainder
