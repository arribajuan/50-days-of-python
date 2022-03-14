class ConvertNumber:
    def __init__(self):
        pass

    def convert_number(self, numbers: list) -> list:
        """
        Convert each of the numbers in the list into a string.

        Your code should then add a comma on each number as a thousand separator for readability.

        The numbers are saved in the following format:

        [1000000, 2356989, 2354672, 9878098]

        When you run your code on the above list, your output should be :

        ['1,000,000', '2,356,989', '2,354,672', '9,878,098']

        :rtype: list
        :param numbers: list of numbers to be converted into a string and formatted
        """
        result = list()

        for number in numbers:
            string_number = "{:,}".format(number)
            result.append(string_number)

        return result
