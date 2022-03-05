class MyDiscount:
    def __init__(self):
        pass

    def my_discount(self, price: float, discount_percentage: float) -> float:
        """
        The function should return the price after the discount.

        For example, if the user enters 150 as price and 15% as the discount, your function should
        return 127.5.

        :rtype: float
        :param price: Price of the product
        :param discount_percentage: Discount percentage
        :return: Price after applying the discount
        """
        result = price - (price * (discount_percentage / 100))

        return result