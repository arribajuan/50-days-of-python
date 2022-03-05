import convert_add


class TestConvertAdd:
    def test_empty(self):
        ca = convert_add.ConvertAdd()
        result = ca.convert_add([])
        assert result == 0

    def test_one_item(self):
        ca = convert_add.ConvertAdd()
        result = ca.convert_add(['1'])
        assert result == 1

    def test_three_items(self):
        ca = convert_add.ConvertAdd()
        result = ca.convert_add(['1', '3', '5'])
        assert result == 9
