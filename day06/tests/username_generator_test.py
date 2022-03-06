from day06.modules import username_generator
import pytest


class TestUsernameGenerator:
    def test_1(self):
        email = "john@gmail.com"

        ug = username_generator.UsernameGenerator()
        result = ug.user_name(email)

        assert result == "john"

    def test_2(self):
        email = "john.doe@gmail.com"

        ug = username_generator.UsernameGenerator()
        result = ug.user_name(email)

        assert result == "john.doe"

    def test_3(self):
        email = "john.doe@gmail_com"

        with pytest.raises(AssertionError) as e_info:
            ug = username_generator.UsernameGenerator()
            result = ug.user_name(email)

        assert str(e_info.value) == "Email address is not valid (john.doe@gmail_com)"

    def test_4(self):
        email = "john.doe@gmail.com"

        ug = username_generator.UsernameGenerator()
        result = ug.is_email(email)

        assert result == True

    def test_5(self):
        email = "john.doe@gmail_com"

        ug = username_generator.UsernameGenerator()
        result = ug.is_email(email)

        assert result == False
