import unittest
import numpy

class TestTwoByTwo(unittest.TestCase):
    def test_a_solved_puzzle_is_returned_without_change(self):
        completed_game = numpy.array([1,2,2,1])
        expected_game = numpy.array([1,2,2,1])
        actual_game = self.solve(completed_game)
        self.assertTrue(numpy.array_equal(expected_game, actual_game))

    def test_single_empty_if_top_left_is_empty_and_top_right_is_two_then_set_top_left_to_one(self):
        partially_completed_game = numpy.array([0,2,2,1])
        expected_game = numpy.array([1,2,2,1])
        actual_game = self.solve(partially_completed_game)
        self.assertTrue(numpy.array_equal(expected_game, actual_game))

    def test_single_empty_if_top_right_is_empty_and_top_left_is_two_then_set_top_right_to_one(self):
        partially_completed_game = numpy.array([2,0,1,2])
        expected_game = numpy.array([2,1,1,2])
        actual_game = self.solve(partially_completed_game)
        self.assertTrue(numpy.array_equal(expected_game, actual_game))

    def test_single_empty_1221_bottom_right_empty(self):
        partially_completed_game = numpy.array([1,2,2,0])
        expected_game = numpy.array([1,2,2,1])
        actual_game = self.solve(partially_completed_game)
        self.assertTrue(numpy.array_equal(expected_game, actual_game))

    def test_single_row_with_single_missing_number(self):
        row = (0, 1)
        self.assertEqual(0, self.find_empty_square_in_row(row))
        row = (1, 0)
        self.assertEqual(1, self.find_empty_square_in_row(row))

    def solve(self, partially_completed_game):
        row = self.get_row(0, partially_completed_game)
        empty_square = self.find_empty_square_in_row(row)

        if empty_square is not None:
            partially_completed_game[empty_square] = self.find_missing_number_in_row(row)
        else:
            row = self.get_row(1, partially_completed_game)
            empty_square = self.find_empty_square_in_row(row)
            if empty_square is not None:
                partially_completed_game[empty_square] = 1

        return partially_completed_game

    def find_empty_square_in_row(self, row):
        for possible_empty_square in range(0, 2):
            if row[possible_empty_square] == 0:
                return possible_empty_square

    def get_row(self, index, partially_completed_game):
        return (partially_completed_game[index*2], partially_completed_game[(index*2)+1])


    def find_missing_number_in_row(self, row):
        for possible_missing_number in range(1, 2):
            if possible_missing_number not in row:
                return possible_missing_number


if __name__ == '__main__':
    unittest.main()
