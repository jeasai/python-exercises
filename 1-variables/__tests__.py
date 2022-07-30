from io import StringIO
import unittest
import sys
import re

mystdout = StringIO()
sys.stdout = mystdout

import variables

sys.stdout = sys.__stdout__
printed = mystdout.getvalue().splitlines()


class VariablesTest(unittest.TestCase):

    def assertVariablesHasattr(self, name):
        errmsg = f"variable {name} does not exist"
        self.assertTrue(hasattr(variables, name), errmsg)

    def assertType(self, var, expected_type):
        errmsg = f"variable {var} does not have type {expected_type}"
        self.assertIs(type(var), expected_type, errmsg)

    def test_age(self):
        self.assertVariablesHasattr("age")
        self.assertType(variables.age, int)

    def test_name(self):
        self.assertVariablesHasattr("name")
        self.assertType(variables.name, str)

    def test_size(self):
        self.assertVariablesHasattr("size")
        self.assertType(variables.size, float)

    def test_food(self):
        self.assertVariablesHasattr("likes_apples")
        self.assertVariablesHasattr("likes_pasta")
        self.assertType(variables.likes_apples, bool)
        self.assertType(variables.likes_pasta, bool)
        self.assertTrue(variables.likes_apples or variables.likes_pasta)

    def test_neg(self):
        self.assertVariablesHasattr("neg")
        self.assertType(variables.neg, int)
        self.assertTrue(variables.neg < 0)

    def test_print_age(self):
        for v in printed:
            if (v.isdecimal()):
                return
        self.assertTrue(False)

    def test_print_likes_apples(self):
        for v in printed:
            if (v == "True" or v == "False"):
                return
        self.assertTrue(False)

    def test_print_neg(self):
        for v in printed:
            if (re.match('^-[0-9]+$', v)):
                return
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
