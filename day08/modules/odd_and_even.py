class OddAndEven:
    def __init__(self):
        pass

    def odd_and_even(self, numbers: list) -> int:
        """
        Returns the difference between the largest even number in the list and the smallest odd number in the list.

        For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

        :rtype: int
        :param numbers: List of numbers to find even and odd numbers
        :return: Difference between the largest even number and the smallest odd number
        """
        numbers.sort()

        largest_even_number = 0
        for number in reversed(numbers):
            if number % 2 == 0:
                largest_even_number = number
                break

        smallest_odd_number = 0
        for number in numbers:
            if number % 2 != 0:
                smallest_odd_number = number
                break

        return largest_even_number - smallest_odd_number

