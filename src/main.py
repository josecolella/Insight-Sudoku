#!/usr/bin/env python3

from Sudoku import Sudoku
from SudokuReader import SudokuReader
import optparse

if __name__ == '__main__':
    usage = "Usage: main.py [options] arg1"
    parser = optparse.OptionParser()
    parser.add_option(
        '-f', '--file', action="store", type="string", dest="filename",
        help="Specify file where sudoku puzzle is stored")
    (options, args) = parser.parse_args()
    print(options)
    print(args)
    # Open the csv
    # sudokuReader = SudokuReader()
    # Get file contents
    # sudokuPuzzle = sudokuReader.readFromFile('sudoku.csv')
    # Initialize Sudoku solver
    # sudoku = Sudoku(sudokuPuzzle)
    # print(sudoku.sudokuPuzzle)
    # Call to solve method
    # sudoku.solve()
    # print(sudoku.sudokuPuzzle)
