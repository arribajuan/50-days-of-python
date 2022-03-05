import only_floats

class TestOnlyFloats:
    def test_1(self):
        of = only_floats.OnlyFloats()
        result = of.only_floats(1.1, 2.2)
        assert result == 2

    def test_2(self):
        of = only_floats.OnlyFloats()
        result = of.only_floats(1, 2.2)
        assert result == 1

    def test_3(self):
        of = only_floats.OnlyFloats()
        result = of.only_floats(1, 2)
        assert result == 0
