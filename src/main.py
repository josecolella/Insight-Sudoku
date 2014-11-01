#!/usr/bin/env python3


from Sudoku import *

if __name__ == '__main__':
    sudoku = Sudoku.Sudoku([
        [0, 3, 5, 2, 9, 0, 8, 6, 4],
        [0, 8, 2, 4, 1, 0, 7, 0, 3],
        [7, 6, 4, 3, 8, 0, 0, 9, 0],
        [2, 1, 8, 7, 3, 9, 0, 4, 0],
        [0, 0, 0, 8, 0, 4, 2, 3, 0],
        [0, 4, 3, 0, 5, 2, 9, 7, 0],
        [4, 0, 6, 5, 7, 1, 0, 0, 9],
        [3, 5, 9, 0, 2, 8, 4, 1, 7],
        [8, 0, 0, 9, 0, 0, 5, 2, 6],
    ])

    sudoku.solve()
    print(sudoku.sudokuPuzzle)
