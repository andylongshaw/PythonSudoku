import unittest

from SudokuGame import SudokuGame


class TestSudokuGame(unittest.TestCase):

    def test_row_retrieval(self):
        game = SudokuGame([1,2,3,4,4,3,2,1,3,1,4,2,2,4,1,3])
        self.assertEqual([1,2,3,4], game.get_row(0))
        self.assertEqual([3,1,4,2], game.get_row(2))
        self.assertEqual([2,4,1,3], game.get_row(3))

        game = SudokuGame([1,2,2,1])
        self.assertEqual([1,2], game.get_row(0))
        self.assertEqual([2,1], game.get_row(1))

if __name__ == '__main__':
    unittest.main()
