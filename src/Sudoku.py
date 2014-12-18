# For array manipulation
import numpy as np
# For chain method that creates a generator for multiple arrays
import itertools
# In order to use deepcopy
import copy
# to read an write to csv
import csv
# to check if file is valid
import os.path
import operator


class SudokuIO:

    """
    Class that manages interaction with IO such as reading from files and
    writing to files.
    """
    @staticmethod
    def readFromFile(filePathString):
        if os.path.isfile(filePathString):
            with open(filePathString) as csvfile:
                sudokureader = csv.reader(
                    csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
                return [row for row in sudokureader]
        else:
            raise Exception(
                "{file} doesn't exists".format(file=filePathString))

    @staticmethod
    def writeToFile(solution, filePathString):
        with open(filePathString, 'w', newline='') as csvfile:
            sudokuwriter = csv.writer(csvfile, delimiter=',')
            for i in range(Sudoku.dimensions):
                sudokuwriter.writerow(solution[i].tolist())


class InvalidSudokuPuzzleError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Sudoku:

    dimensions = 9

    def __init__(self, sudokuPuzzle):
        """
        """
        self.checkValidPuzzle(sudokuPuzzle)

        self.puzzle = np.array(sudokuPuzzle, dtype=np.uint8)
        self.subgroups = self.getSubGroups()
        self.decisionTree = self.buidDecisionTree()

    def checkValidPuzzle(self, puzzle):
        """
        Checks if a puzzle is 9x9. Raises Exception if condition is not met
        """
        if np.array(puzzle).shape != (Sudoku.dimensions, Sudoku.dimensions):
            raise InvalidSudokuPuzzleError(
                'A valid Sudoku puzzle is a 9x9 matrix. 9 rows, 9 columns')

    def isSolved(self):
        """
        Determines whether the sudoku puzzle is solved by checking

        Returns
        ------
        bool
            True if the sudokuPuzzle is solved False otherwise
        """
        return len([i for i in self.puzzle.flatten() if i == 0]) == 0

    def buidDecisionTree(self):
        """
        Returns
        -------
        decisionTree -> dict
            A dictionary where the keys denote the row of an empty element and
            the inner dictionary keys denote the index of the blank element
            with a list of [1,2,...9] denoting the initial possibilities for
            the blank element
        """
        decisionTree = {row: {rowElement: np.arange(1, 10) for rowElement in np.where(
            i == 0)[0]} for i, row in zip(self.puzzle, np.arange(self.puzzle.shape[0]))}
        return decisionTree

    def group(self, row, element):
        """
        Returns the 3x3 subgroup that the matrix[row][element] belongs to

        Parameters
        ----------
        row -> int
            The row of the missing element
        element -> int
            The index of the element within the row

        Returns
        -------
        groups -> ndarray
            An array that represents the 3x3 group that [row][element] belongs to
        """
        for rowRange, groups in self.subgroups.items():
            if row in rowRange[0] and element in rowRange[1]:
                return rowRange, groups.flatten()

    def getSubGroups(self):
        """
        Builds the different 3x3 subgroups of the sudoku puzzle.
        Useful to reduce possible elements
        Returns
        -------
        """
        subgroups = {}
        for startingRow, endingRow in zip(range(0, 10, 3), range(3, 10, 3)):
            for startingCol, endingCol in zip(range(0, 10, 3), range(3, 10, 3)):
                subgroups[(range(startingRow, endingRow), range(startingCol, endingCol))] = self.puzzle[
                    startingRow:endingRow, startingCol:endingCol]
        return subgroups

    def reducePossibilities(self, row, rowElement):
        """
        Reduces the possibilities of a blank sudoku cell.
        Parameters
        ----------
        row -> int
            The row where the blank element presides
        rowElement -> int
            The index of the blank element
        """
        groupRange, groupArray = self.group(row, rowElement)

        possibilities = itertools.chain(
            self.puzzle[row], self.puzzle[:, rowElement], groupArray)
        self.decisionTree[row][rowElement] = np.setdiff1d(
            self.decisionTree[row][rowElement], possibilities)
        if len(self.decisionTree[row][rowElement]) == 1:
            self.puzzle[row][rowElement] = self.decisionTree[row][rowElement]
            self.decisionTree[row].pop(rowElement)
        if len(self.decisionTree[row]) == 0:
            self.decisionTree.pop(row)

    def solve(self):
        """
        Solves the Sudoku puzzle
        """
        if not self.isSolved():
            while len(self.decisionTree) != 0:
                decisionTree = copy.deepcopy(self.decisionTree)
                for row, emptyRowElements in decisionTree.items():
                    for emptyRowElement, possibilities in emptyRowElements.items():
                        self.reducePossibilities(row, emptyRowElement)
