import register_check


class TestRegisterCheck:
    def test_1(self):
        input = {}
        rc = register_check.RegisterCheck()
        result = rc.register_check(input)
        assert result == 0

    def test_2(self):
        input = {'Michael': 'yes'}
        rc = register_check.RegisterCheck()
        result = rc.register_check(input)
        assert result == 1

    def test_3(self):
        input = {'John': 'no'}
        rc = register_check.RegisterCheck()
        result = rc.register_check(input)
        assert result == 0

    def test_4(self):
        input = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
        rc = register_check.RegisterCheck()
        result = rc.register_check(input)
        assert result == 3
