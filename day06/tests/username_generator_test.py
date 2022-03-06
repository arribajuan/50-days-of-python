from day06.modules import username_generator

class TestUsernameGenerator:
    def test_1(self):
        email = "ben@gmail.com"

        ug = username_generator.UsernameGenerator()
        result = ug.user_name(email)

        assert result == "ben"
