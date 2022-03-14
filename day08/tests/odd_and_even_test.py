from day08.modules import odd_and_even


class TestOddAndEven:
    def test_1(self):
        number_list = []

        oae = odd_and_even.OddAndEven()
        result = oae.odd_and_even(number_list)

        assert result == 0

    def test_2(self):
        number_list = [1, 3, 5]

        oae = odd_and_even.OddAndEven()
        result = oae.odd_and_even(number_list)

        assert result == -1

    def test_3(self):
        number_list = [2, 4, 6]

        oae = odd_and_even.OddAndEven()
        result = oae.odd_and_even(number_list)

        assert result == 6

    def test_4(self):
        number_list = [1, 2, 4, 6]

        oae = odd_and_even.OddAndEven()
        result = oae.odd_and_even(number_list)

        assert result == 5
