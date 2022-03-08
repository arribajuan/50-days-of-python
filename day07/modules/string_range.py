class StringRange:
    def __init__(self):
        pass

    def string_range(self, range_count: int) -> str:
        """
        Takes a single number and returns a string of its range.The string characters should be separated by dots(.)

        For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.

        :rtype: str
        :param range_count: The number of integers to add to the string
        :return: The string with the numbers separated by dots
        """
        result = ""

        if range_count > 0:
            result = str(0)

        if range_count > 1:
            for n in range(1, range_count):
                result = f"{result}.{str(n)}"

        return result
