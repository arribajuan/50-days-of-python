import divide_or_square


class TestDivideOrSquare:
    def test_0(self):
        doq = divide_or_square.DivideOrSquare()
        result = doq.divide_or_square(0)
        assert result == 0.0

    def test_1(self):
        doq = divide_or_square.DivideOrSquare()
        result = doq.divide_or_square(1)
        assert result == 1.0

    def test_9(self):
        doq = divide_or_square.DivideOrSquare()
        result = doq.divide_or_square(9)
        assert result == 4.0

    def test_25(self):
        doq = divide_or_square.DivideOrSquare()
        result = doq.divide_or_square(25)
        assert result == 5.0
