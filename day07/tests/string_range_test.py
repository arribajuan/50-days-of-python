from day07.modules import string_range


class TestStringRange:
    def test_1(self):
        range_value = -1

        sr = string_range.StringRange()
        result = sr.string_range(range_value)

        assert result == ""

    def test_2(self):
        range_value = 0

        sr = string_range.StringRange()
        result = sr.string_range(range_value)

        assert result == ""

    def test_3(self):
        range_value = 6

        sr = string_range.StringRange()
        result = sr.string_range(range_value)

        assert result == "0.1.2.3.4.5"
