class BiggestOdd:
    def __init__(self):
        pass

    def biggest_odd(self, numbers: str) -> int:
        """
        Takes a string of numbers and returns the biggest odd number in the list.

        For example, if you pass ‘23569’ as an argument, your function should return 9.

        :rtype: int
        :param numbers: A string with numbers (single digits) where we will search for the biggest odd number
        :return: biggest odd number in the number string
        """
        odd_numbers = [int(x) for x in numbers if (int(x) % 2 != 0)]
        if len(odd_numbers) == 0:
            return 0
        else:
            odd_numbers.sort(reverse=True)
            return odd_numbers[0]
