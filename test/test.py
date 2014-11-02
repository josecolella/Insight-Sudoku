#!/usr/bin/env python3


import os
import sys

# Set the correct path to Sudoku module
path = os.path.abspath(os.path.join(os.path.dirname('Sudoku.py'), '../src'))
if path not in sys.path:
    sys.path.insert(0, path)

from Sudoku import Sudoku
import unittest
import numpy as np


class SudokuTestCase(unittest.TestCase):
    """
    Tests the validity of the solve() method on the challenge problem to
    check whether the solved puzzle matches the correct solution
    """
    def setUp(self):
        self.sudoku = Sudoku([
            [0, 3, 5, 2, 9, 0, 8, 6, 4],
            [0, 8, 2, 4, 1, 0, 7, 0, 3],
            [7, 6, 4, 3, 8, 0, 0, 9, 0],
            [2, 1, 8, 7, 3, 9, 0, 4, 0],
            [0, 0, 0, 8, 0, 4, 2, 3, 0],
            [0, 4, 3, 0, 5, 2, 9, 7, 0],
            [4, 0, 6, 5, 7, 1, 0, 0, 9],
            [3, 5, 9, 0, 2, 8, 4, 1, 7],
            [8, 0, 0, 9, 0, 0, 5, 2, 6]
        ])

    def test_sudoku_puzzle_not_solved(self):
        self.assertFalse(self.sudoku.isSolved())

    def test_sudoku_puzzle_solved(self):
        self.sudoku.solve()
        self.assertTrue(self.sudoku.isSolved())

    def test_sudoku_valid_solution(self):
        self.sudoku.solve()
        solution = np.array([[1, 3, 5, 2, 9, 7, 8, 6, 4],
                             [9, 8, 2, 4, 1, 6, 7, 5, 3],
                             [7, 6, 4, 3, 8, 5, 1, 9, 2],
                             [2, 1, 8, 7, 3, 9, 6, 4, 5],
                             [5, 9, 7, 8, 6, 4, 2, 3, 1],
                             [6, 4, 3, 1, 5, 2, 9, 7, 8],
                             [4, 2, 6, 5, 7, 1, 3, 8, 9],
                             [3, 5, 9, 6, 2, 8, 4, 1, 7],
                             [8, 7, 1, 9, 4, 3, 5, 2, 6]])
        equality = {i == j for i, j in zip(
            self.sudoku.puzzle.flatten(), solution.flatten())}
        self.assertTrue(True in equality and False not in equality)


class SudokuTestCase2(unittest.TestCase):
    """
    Tests the validity of the solve() method of the Sudoku class to
    make sure that the ending puzzle matches the correct solution
    """
    def setUp(self):
        self.sudoku = Sudoku([
            [0, 0, 0, 0, 5, 6, 4, 0, 0],
            [6, 0, 7, 0, 0, 1, 0, 8, 9],
            [0, 1, 0, 0, 0, 0, 0, 6, 0],
            [7, 2, 0, 3, 0, 9, 0, 5, 0],
            [1, 3, 0, 0, 6, 0, 0, 7, 2],
            [0, 9, 0, 1, 0, 7, 0, 4, 3],
            [0, 7, 0, 0, 0, 0, 0, 9, 0],
            [8, 5, 0, 9, 0, 0, 3, 0, 6],
            [0, 0, 1, 5, 8, 0, 0, 0, 0]
        ])

    def test_sudoku_solved(self):
        self.sudoku.solve()
        self.sudoku.isSolved()

    def test_sudoku_valid_solution(self):
        self.sudoku.solve()
        solution = np.array([
                            [2, 8, 9, 7, 5, 6, 4, 3, 1],
                            [6, 4, 7, 2, 3, 1, 5, 8, 9],
                            [3, 1, 5, 4, 9, 8, 2, 6, 7],
                            [7, 2, 6, 3, 4, 9, 1, 5, 8],
                            [1, 3, 4, 8, 6, 5, 9, 7, 2],
                            [5, 9, 8, 1, 2, 7, 6, 4, 3],
                            [4, 7, 3, 6, 1, 2, 8, 9, 5],
                            [8, 5, 2, 9, 7, 4, 3, 1, 6],
                            [9, 6, 1, 5, 8, 3, 7, 2, 4],
                            ])
        equality = {i == j for i, j in zip(
            self.sudoku.puzzle.flatten(), solution.flatten())}
        self.assertTrue(True in equality and False not in equality)


class SudokuTestCase3(unittest.TestCase):

    """
    Tests the validity of the sudoku solver algorithms, in making sure that
    the solution puzzle that it obtains is correct
    """

    def setUp(self):
        self.sudoku = Sudoku([
            [8, 0, 0, 0, 5, 4, 0, 6, 0],
            [0, 9, 0, 0, 3, 2, 0, 0, 0],
            [0, 0, 4, 0, 6, 7, 0, 3, 1],
            [0, 0, 2, 7, 0, 0, 0, 0, 5],
            [4, 6, 0, 2, 0, 5, 0, 1, 8],
            [1, 0, 0, 0, 0, 8, 7, 0, 0],
            [2, 1, 0, 4, 8, 0, 9, 0, 0],
            [0, 0, 0, 5, 7, 0, 0, 4, 0],
            [0, 4, 0, 6, 2, 0, 0, 0, 3]
        ])

    def test_sudoku_valid_solution(self):
        self.sudoku.solve()
        solution = np.array([
            [8, 7, 3, 1, 5, 4, 2, 6, 9],
            [6, 9, 1, 8, 3, 2, 5, 7, 4],
            [5, 2, 4, 9, 6, 7, 8, 3, 1],
            [3, 8, 2, 7, 1, 6, 4, 9, 5],
            [4, 6, 7, 2, 9, 5, 3, 1, 8],
            [1, 5, 9, 3, 4, 8, 7, 2, 6],
            [2, 1, 6, 4, 8, 3, 9, 5, 7],
            [9, 3, 8, 5, 7, 1, 6, 4, 2],
            [7, 4, 5, 6, 2, 9, 1, 8, 3],
        ])
        equality = {i == j for i, j in zip(
            self.sudoku.puzzle.flatten(), solution.flatten())}
        self.assertTrue(True in equality and False not in equality)


if __name__ == '__main__':
    unittest.main()
