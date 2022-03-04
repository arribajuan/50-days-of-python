class ConvertAdd:
    def __init__(self):
        pass

    def convert_add(self, input_array: list) -> int:
        """
        Takes a list of strings as an argument and converts it to integers and sums the list.
        For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

        :rtype: int
        :param input_array: list of strings to be summed up
        :return: the sum of the string's integer values
        """
        total = 0

        for item in input_array:
            total += int(item)

        return total
