# to reader puzzles inside files
import csv


class SudokuReader:

    """
    """

    def __init__(self):
        pass

    def readFromFile(self, filePathString):

        with open('sudoku.csv') as csvfile:
            sudokureader = csv.reader(
                csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            return [row for row in sudokureader]
