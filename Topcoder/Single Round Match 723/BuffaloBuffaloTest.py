import unittest
from BuffaloBuffalo import BuffaloBuffalo


class BuffaloBuffaloTest(unittest.TestCase):

    def test_Example0(self):
        s = "buffalo buffalo"
        __expected = "Good"
        __result = BuffaloBuffalo().check(s)
        self.assertEqual(__expected, __result)

    def test_Example1(self):
        s = "buffalobuffalo"
        __expected = "Not good"
        __result = BuffaloBuffalo().check(s)
        self.assertEqual(__expected, __result)

    def test_Example2(self):
        s = "buffalo buffalo buffalo"
        __expected = "Good"
        __result = BuffaloBuffalo().check(s)
        self.assertEqual(__expected, __result)

    def test_Example3(self):
        s = "buf falo buffalo"
        __expected = "Not good"
        __result = BuffaloBuffalo().check(s)
        self.assertEqual(__expected, __result)

    def test_Example4(self):
        s = "cow"
        __expected = "Not good"
        __result = BuffaloBuffalo().check(s)
        self.assertEqual(__expected, __result)

    def test_Example5(self):
        s = "buffalo  buffalo"
        __expected = "Not good"
        __result = BuffaloBuffalo().check(s)
        self.assertEqual(__expected, __result)


if __name__ == '__main__':
    unittest.main()
