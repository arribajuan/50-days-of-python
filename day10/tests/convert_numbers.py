from day10.modules import convert_numbers


class TestConvertNumbers:
    def test_1(self):
        number_list = [1000000, 2356989, 2354672, 9878098]

        cn = convert_numbers.ConvertNumber()
        result = cn.convert_number((number_list))

        assert result == ['1,000,000', '2,356,989', '2,354,672', '9,878,098']
