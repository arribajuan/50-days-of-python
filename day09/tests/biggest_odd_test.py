from day09.modules import biggest_odd


class TestBiggestOdd:
    def test_1(self):
        number_list = "23569"

        bo = biggest_odd.BiggestOdd()
        result = bo.biggest_odd(number_list)

        assert result == 9

    def test_2(self):
        number_list = "2356"

        bo = biggest_odd.BiggestOdd()
        result = bo.biggest_odd(number_list)

        assert result == 5

    def test_3(self):
        number_list = "2356958"

        bo = biggest_odd.BiggestOdd()
        result = bo.biggest_odd(number_list)

        assert result == 9

    def test_4(self):
        number_list = "9"

        bo = biggest_odd.BiggestOdd()
        result = bo.biggest_odd(number_list)

        assert result == 9

    def test_5(self):
        number_list = "6"

        bo = biggest_odd.BiggestOdd()
        result = bo.biggest_odd(number_list)

        assert result == 0

    def test_6(self):
        number_list = ""

        bo = biggest_odd.BiggestOdd()
        result = bo.biggest_odd(number_list)

        assert result == 0
