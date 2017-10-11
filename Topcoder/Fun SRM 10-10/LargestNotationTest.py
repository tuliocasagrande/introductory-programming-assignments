import unittest
from LargestNotation import LargestNotation


class LargestNotationTest(unittest.TestCase):

    def test_Example0(self):
        N = 3
        __expected = 2
        __result = LargestNotation().maxDigitsSum(N)
        self.assertEqual(__expected, __result)

    def test_Example1(self):
        N = 4
        __expected = 2
        __result = LargestNotation().maxDigitsSum(N)
        self.assertEqual(__expected, __result)

    def test_Example2(self):
        N = 22
        __expected = 11
        __result = LargestNotation().maxDigitsSum(N)
        self.assertEqual(__expected, __result)

    def test_Example3(self):
        N = 1000000
        __expected = 500000
        __result = LargestNotation().maxDigitsSum(N)
        self.assertEqual(__expected, __result)

    def test_Example4(self):
        N = 12345
        __expected = 6173
        __result = LargestNotation().maxDigitsSum(N)
        self.assertEqual(__expected, __result)


if __name__ == '__main__':
    unittest.main()
