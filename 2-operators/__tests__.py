import unittest
import operators


class OperatorsTest(unittest.TestCase):

    def assertOperatorsHasattr(self, name):
        errmsg = f"variable {name} does not exist"
        self.assertTrue(hasattr(operators, name), errmsg)

    def assertType(self, var, expected_type):
        errmsg = f"variable {var} does not have type {expected_type}"
        self.assertIs(type(var), expected_type, errmsg)

    def test_sanity(self):
        errmsg = "variables in given code should not be modified!"
        self.assertEqual(operators.price, 100, errmsg)
        self.assertEqual(operators.price2, 2000, errmsg)
        self.assertEqual(operators.tax, 20, errmsg)
        self.assertEqual(operators.refund, 15, errmsg)
        self.assertEqual(operators.nb_items, 5, errmsg)
        self.assertEqual(operators.small_discount, True, errmsg)
        self.assertEqual(operators.big_discount, False, errmsg)
        self.assertEqual(operators.price_str, "3.1415", errmsg)
        self.assertEqual(operators.discount_price_float, 9.99, errmsg)

    def test_total_price(self):
        self.assertOperatorsHasattr("total_price")
        self.assertEqual(operators.total_price, 120)

    def test_discount_price(self):
        self.assertOperatorsHasattr("discount_price")
        self.assertEqual(operators.discount_price, 85)

    def test_items_price(self):
        self.assertOperatorsHasattr("items_price")
        self.assertEqual(operators.items_price, 500)

    def test_item_price(self):
        self.assertOperatorsHasattr("item_price")
        self.assertEqual(operators.item_price, 400)

    def test_price_adjusted(self):
        self.assertOperatorsHasattr("price_adjusted")
        self.assertEqual(operators.price_adjusted, 105)

    def test_price_adjusted2(self):
        self.assertOperatorsHasattr("price_adjusted2")
        self.assertEqual(operators.price_adjusted2, 110)

    def test_price_adjusted3(self):
        self.assertOperatorsHasattr("price_adjusted3")
        self.assertEqual(operators.price_adjusted3, 108)

    def test_rounded_price(self):
        self.assertOperatorsHasattr("rounded_price")
        self.assertEqual(operators.rounded_price, 315)

    def test_rounded_price2(self):
        self.assertOperatorsHasattr("rounded_price2")
        self.assertEqual(operators.rounded_price2, 315.14)

    def test_has_discount(self):
        self.assertOperatorsHasattr("has_discount")
        self.assertEqual(operators.has_discount, True)

    def test_same_price(self):
        self.assertOperatorsHasattr("same_price")
        self.assertEqual(operators.same_price, False)

    def test_different_price(self):
        self.assertOperatorsHasattr("different_price")
        self.assertEqual(operators.different_price, True)

    def test_bigger_price(self):
        self.assertOperatorsHasattr("bigger_price")
        self.assertEqual(operators.bigger_price, False)

    def test_both_expensive(self):
        self.assertOperatorsHasattr("both_expensive")
        self.assertEqual(operators.both_expensive, True)

    def test_both_cheap(self):
        self.assertOperatorsHasattr("both_cheap")
        self.assertEqual(operators.both_cheap, False)

    def test_no_discount(self):
        self.assertOperatorsHasattr("no_discount")
        self.assertEqual(operators.no_discount, False)

    def test_price_float(self):
        self.assertOperatorsHasattr("price_float")
        self.assertEqual(operators.price_float, 3.1415)

    def test_discount_price_str(self):
        self.assertOperatorsHasattr("discount_price_str")
        self.assertEqual(operators.discount_price_str, "9.99")


if __name__ == '__main__':
    unittest.main()
