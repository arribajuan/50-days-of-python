import my_discount

class TestMyDiscount:
    def test_1(self):
        price = 100
        discount_percentage = 50.0

        md = my_discount.MyDiscount()
        result = md.my_discount(price, discount_percentage)

        assert result == 50.0

    def test_2(self):
        price = 100
        discount_percentage = 100.0

        md = my_discount.MyDiscount()
        result = md.my_discount(price, discount_percentage)

        assert result == 0.0

    def test_3(self):
        price = 100
        discount_percentage = 0.0

        md = my_discount.MyDiscount()
        result = md.my_discount(price, discount_percentage)

        assert result == 100.0

