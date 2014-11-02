#!/usr/bin/env python3

from Sudoku import Sudoku
from SudokuReader import SudokuReader

if __name__ == '__main__':
    # Open the csv
    sudokuReader = SudokuReader()
    sudokuPuzzle = sudokuReader.readFromFile('sudoku.csv')
    # Initialize Sudoku solver
    sudoku = Sudoku(sudokuPuzzle)
    print(sudoku.sudokuPuzzle)
    # Call to solve method
    sudoku.solve()
    print(sudoku.sudokuPuzzle)
