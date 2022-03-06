import re


class UsernameGenerator:
    def __init__(self):
        pass

    def user_name(self, email: str) -> str:
        """
        Takes the text to the left of the @ symbol in the provided email and returns it as the generated username

        For example, the email address 'ben@gmail.com' should return 'ben' as the username

        :rtype: str
        :param email: email to derive the username from
        :return: the generated username
        """
        assert (self.is_email(email)), "Email address is not valid ({email_address})".format(email_address=email)
        return email[0:email.find("@")]

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
