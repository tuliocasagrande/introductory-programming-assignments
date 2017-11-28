import unittest
from GravityPuzzleEasy import GravityPuzzleEasy


class GravityPuzzleEasyTest(unittest.TestCase):

    def test_Example0(self):
        board = [
            "#",
            ".",
            "."
        ]
        __expected = [
            ".",
            ".",
            "#"
        ]
        __result = GravityPuzzleEasy().solve(board)
        self.assertEqual(__expected, __result)

    def test_Example1(self):
        board = [
            "##",
            ".#",
            "#."
        ]
        __expected = [
            "..",
            "##",
            "##"
        ]
        __result = GravityPuzzleEasy().solve(board)
        self.assertEqual(__expected, __result)

    def test_Example2(self):
        board = [
            "..#.#",
            "#.#..",
            "...##"
        ]
        __expected = [
            ".....",
            "..#.#",
            "#.###"
        ]
        __result = GravityPuzzleEasy().solve(board)
        self.assertEqual(__expected, __result)

    def test_Example3(self):
        board = [
            "#####",
            "#####",
            "#####",
            "#####"
        ]
        __expected = [
            "#####",
            "#####",
            "#####",
            "#####"
        ]
        __result = GravityPuzzleEasy().solve(board)
        self.assertEqual(__expected, __result)

    def test_Example4(self):
        board = [
            "."
        ]
        __expected = [
            "."
        ]
        __result = GravityPuzzleEasy().solve(board)
        self.assertEqual(__expected, __result)


if __name__ == '__main__':
    unittest.main()
