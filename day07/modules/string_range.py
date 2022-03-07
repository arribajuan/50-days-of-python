class StringRange:
    def __init__(self):
        pass

    def string_range(self, range_count: int) -> str:
        """
        Takes a single number and returns a string of its range.The string characters should be separated by dots(.)

        For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.

        :rtype: str
        :param range: The number of integers to add to the string
        :return: The string with the nunmbers separated by dots
        """
        result = ""


        for n in range(range_count):
            print(n)


        return result

    def is_email(self, email: str) -> bool:
        """
        Tests the supplied email address for validity

        :rtype: bool
        :param email: The email address to be validated
        :return: True if the email address is valid, False otherwise
        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)):
            return True
        else:
            return False
