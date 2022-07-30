from io import StringIO
import unittest
import functions
import sys


class FunctionsTest(unittest.TestCase):

    def test_update_procudct_price(self):
        self.assertTrue(None in functions.calls)

    def test_update_product_price2(self):
        self.assertTrue(3 in functions.calls)

    def test_total_revenue(self):
        # Check if function exist
        self.assertEqual(functions.total_revenue(), 40000)

    def test_revenue_after_tax(self):
        # Check if function exist
        self.assertEqual(functions.revenue_after_tax(0), 0)
        self.assertEqual(functions.revenue_after_tax(1), 0.9)
        self.assertEqual(functions.revenue_after_tax(9000), 8100)

    def test_money_earnt(self):
        self.assertEqual(functions.money_earnt(0, 0), 0)
        self.assertEqual(functions.money_earnt(1, 0), 0)
        self.assertEqual(functions.money_earnt(0, 1), 0)
        self.assertEqual(functions.money_earnt(6, 30), 180)
        self.assertEqual(functions.money_earnt(60, 40), 2400)

    def test_money_earnt2(self):
        self.assertEqual(functions.money_earnt2(0, 0), 0)
        self.assertEqual(functions.money_earnt2(1, 0), 0)
        self.assertEqual(functions.money_earnt2(0, 1), 0)
        self.assertEqual(functions.money_earnt2(6, 10), 60)
        self.assertEqual(functions.money_earnt2(60, 40), 2400)
        self.assertEqual(functions.money_earnt2(1), 10)
        self.assertEqual(functions.money_earnt2(3000), 30000)

    def test_print_euro_to_dollar(self):
        mystdout = StringIO()
        sys.stdout = mystdout
        functions.print_euro_to_dollar(0)
        functions.print_euro_to_dollar(20)
        sys.stdout = sys.__stdout__
        printed = mystdout.getvalue().splitlines()

        self.assertEqual(printed, ["0.0", "22.0"])

    def test_print_euro_to_dollar2(self):
        mystdout = StringIO()
        sys.stdout = mystdout
        first_call = functions.print_euro_to_dollar2(0)
        second_call = functions.print_euro_to_dollar2(20)
        sys.stdout = sys.__stdout__
        printed = mystdout.getvalue().splitlines()

        self.assertEqual(printed, ["0.0", "22.0"])
        self.assertEqual(first_call, 0)
        self.assertEqual(second_call, 22)

    def test_print_total_number_of_sales(self):
        mystdout = StringIO()
        sys.stdout = mystdout
        functions.print_total_number_of_sales()
        sys.stdout = sys.__stdout__
        printed = mystdout.getvalue().splitlines()

        self.assertEqual(printed, ["2000"])

    def test_print_europe_sales(self):
        mystdout = StringIO()
        sys.stdout = mystdout
        eu_sales = functions.print_europe_sales()
        sys.stdout = sys.__stdout__
        printed = mystdout.getvalue().splitlines()

        self.assertEqual(printed, ["3300"])
        self.assertEqual(eu_sales, 3300)

    def test_update_catalog(self):
        mystdout = StringIO()
        sys.stdout = mystdout
        best_selling = functions.update_catalog()
        sys.stdout = sys.__stdout__
        printed = mystdout.getvalue().splitlines()

        self.assertEqual(printed, [])
        self.assertEqual(functions.new_products, ["toothbrush", "scale"])
        self.assertEqual(best_selling, "apples")


if __name__ == '__main__':
    unittest.main()
