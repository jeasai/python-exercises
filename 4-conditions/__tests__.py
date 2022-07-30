import unittest
import conditions


class ConditionsTest(unittest.TestCase):

    def test_company_size(self):
        self.assertEqual(conditions.company_size(10001), "Big")
        self.assertEqual(conditions.company_size(10000), "Small")
        self.assertEqual(conditions.company_size(50), "Small")

    def test_has_debt(self):
        self.assertEqual(conditions.has_debt(50), "No")
        self.assertEqual(conditions.has_debt(0), "No")
        self.assertEqual(conditions.has_debt(-1), "Yes")

    def test_is_best_client(self):
        self.assertEqual(conditions.is_best_client("Mary"), "No")
        self.assertEqual(conditions.is_best_client("Jean"), "Yes")

    def test_is_not_best_product(self):
        self.assertEqual(conditions.is_not_best_product("apples"), 0)
        self.assertEqual(conditions.is_not_best_product("banana"), 1)

    def test_soccer_client_type(self):
        tt = conditions.soccer_client_type(True, True)
        tf = conditions.soccer_client_type(True, False)
        ft = conditions.soccer_client_type(False, True)
        ff = conditions.soccer_client_type(False, False)

        self.assertEqual(tt, "soccer fan")
        self.assertEqual(tf, "not a soccer fan")
        self.assertEqual(ft, "not a soccer fan")
        self.assertEqual(ff, "not a soccer fan")

    def test_sport_client_type(self):
        tt = conditions.sport_client_type(True, True)
        tf = conditions.sport_client_type(True, False)
        ft = conditions.sport_client_type(False, True)
        ff = conditions.sport_client_type(False, False)

        self.assertEqual(tt, "sports fan")
        self.assertEqual(tf, "sports fan")
        self.assertEqual(ft, "sports fan")
        self.assertEqual(ff, "not a sports fan")

    def test_get_biggest_company(self):
        theorical_values = {
            "France": "TotalEnergies",
            "China": "SGCC",
            "Nigeria": "Dangote"
        }

        for key, val in theorical_values.items():
            self.assertEqual(conditions.get_biggest_company(key), val)

    def test_get_buy_scenario(self):
        self.assertEqual(conditions.buy_scenario(10, True, 100), 3)
        self.assertEqual(conditions.buy_scenario(10, True, 1), 2)
        self.assertEqual(conditions.buy_scenario(100, False, 1000), 1)
        self.assertEqual(conditions.buy_scenario(100, False, 90), 0)


if __name__ == '__main__':
    unittest.main()
