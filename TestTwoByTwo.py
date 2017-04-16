import unittest
import numpy


class TestTwoByTwo(unittest.TestCase):
    def test_a_solved_puzzle_is_returned_without_change(self):
        completed_game = [1,2,2,1]
        expected_game = [1,2,2,1]
        actual_game = self.solve(completed_game)
        self.assertEquals(expected_game, actual_game)

    def test_single_empty_if_top_left_is_empty_and_top_right_is_two_then_set_top_left_to_one(self):
        partially_completed_game = [0,2,2,1]
        expected_game = [1,2,2,1]
        actual_game = self.solve(partially_completed_game)
        self.assertEquals(expected_game, actual_game)

    def test_single_empty_if_top_right_is_empty_and_top_left_is_two_then_set_top_right_to_one(self):
        partially_completed_game = [2,0,1,2]
        expected_game = [2,1,1,2]
        actual_game = self.solve(partially_completed_game)
        self.assertEquals(expected_game, actual_game)

    def test_single_empty_1221_bottom_right_empty(self):
        partially_completed_game = [1,2,2,0]
        expected_game = [1,2,2,1]
        actual_game = self.solve(partially_completed_game)
        self.assertEquals(expected_game, actual_game)

    def test_single_empty_1234432131422413_bottom_right_empty(self):
        partially_completed_game = numpy.array([1,2,3,4,4,3,2,1,3,1,4,2,2,4,1,0])
        expected_game = numpy.array([1,2,3,4,4,3,2,1,3,1,4,2,2,4,1,3])
        actual_game = self.solve(partially_completed_game)
        self.assertTrue(numpy.array_equal(expected_game, actual_game))

    def test_single_row_with_single_missing_number(self):
        row = [0, 1]
        self.assertEqual(0, self.find_empty_square_in_row(row))
        row = [1, 0]
        self.assertEqual(1, self.find_empty_square_in_row(row))
        row = [1, 2, 3, 0]
        self.assertEqual(3, self.find_empty_square_in_row(row))
        row = [1, 2, 0, 4]
        self.assertEqual(2, self.find_empty_square_in_row(row))

    def test_row_retrieval(self):
        game = [1,2,3,4,4,3,2,1,3,1,4,2,2,4,1,3]
        row = self.get_row(0, game)
        self.assertEqual([1,2,3,4], row)
        row = self.get_row(2, game)
        self.assertEqual([3,1,4,2], row)
        row = self.get_row(3, game)
        self.assertEqual([2,4,1,3], row)

        game = [1,2,2,1]
        row = self.get_row(0, game)
        self.assertEqual([1,2], row)
        row = self.get_row(1, game)
        self.assertEqual([2,1], row)


    def solve(self, partially_completed_game):
        num_rows = int(numpy.sqrt(len(partially_completed_game)))

        for index in range(num_rows):
            row = self.get_row(index, partially_completed_game)
            empty_square = self.find_empty_square_in_row(row)

            if empty_square is not None:
                partially_completed_game[(index * num_rows) + empty_square] = self.find_missing_number_in_row(row)

        return partially_completed_game

    def find_empty_square_in_row(self, row):
        for possible_empty_square in range(len(row)):
            if row[possible_empty_square] == 0:
                return possible_empty_square

    def get_row(self, index, partially_completed_game):
        row_length = int(numpy.sqrt(len(partially_completed_game)))
        first_cell_in_row = index * row_length
        row = []
        for index in range (row_length):
            row.append(partially_completed_game[first_cell_in_row + index])
        return row


    def find_missing_number_in_row(self, row):
        for possible_missing_number in range(1, len(row) + 1):
            if possible_missing_number not in row:
                return possible_missing_number


if __name__ == '__main__':
    unittest.main()
