import unittest
from SnakeMove import SnakeMove


class SnakeMoveTest(unittest.TestCase):

    def test_Example0(self):
        board = [
            "10.",
            "2..",
            "34."
        ]
        __expected = [
            "210",
            "3..",
            "4.."
        ]
        __result = SnakeMove().move(board)
        self.assertEqual(__expected, __result)

    def test_Example1(self):
        board = [
            "21",
            ".0"
        ]
        __expected = [
            "YOU LOST"
        ]
        __result = SnakeMove().move(board)
        self.assertEqual(__expected, __result)

    def test_Example2(self):
        board = [
            "765",
            "0.4",
            "123"
        ]
        __expected = [
            "076",
            "1.5",
            "234"
        ]
        __result = SnakeMove().move(board)
        self.assertEqual(__expected, __result)

    def test_Example3(self):
        board = [
            "8765",
            ".0.4",
            ".123"
        ]
        __expected = [
            "YOU LOST"
        ]
        __result = SnakeMove().move(board)
        self.assertEqual(__expected, __result)

    def test_Example4(self):
        board = [
            ".012.",
            "..43.",
            "..5.9",
            "..678"
        ]
        __expected = [
            "0123.",
            "..54.",
            "..6..",
            "..789"
        ]
        __result = SnakeMove().move(board)
        self.assertEqual(__expected, __result)


if __name__ == '__main__':
    unittest.main()
