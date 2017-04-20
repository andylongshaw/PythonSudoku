import numpy

class SudokuGame:
    raw_game_data = None

    def __init__(self, raw_game_data):
        self.raw_game_data = raw_game_data

    def get_row(self, index):
        row_length = int(numpy.sqrt(len(self.raw_game_data)))
        first_cell_in_row = index * row_length
        row = []
        for index in range(row_length):
           row.append(self.raw_game_data[first_cell_in_row + index])
        return row