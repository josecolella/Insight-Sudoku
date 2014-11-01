# For array manipulation
import numpy as np
# For chain method that creates a generator for multiple arrays
import itertools
# In order to use deepcopy
import copy

class Sudoku:
    """
    """

    def __init__(self, sudokuPuzzle):
        """
        """
        self.sudokuPuzzle = np.array(sudokuPuzzle)
        self.subgroups = self.getSubGroups()
        self.decisionTree = self.buidDecisionTree()

    def buidDecisionTree(self):
        """
        """
        return {row: {rowElement: np.arange(1,10) for rowElement in np.where(i == 0)[0]} for i, row in zip(self.sudokuPuzzle, np.arange(self.sudokuPuzzle.shape[0]))}

    def group(self, row, element):
        """

        """
        for rowRange, groups in self.subgroups.items():
            if row in rowRange[0] and element in rowRange[1]:
                return groups

    def getSubGroups(self):
        """
        """
        subgroups = {}
        for i, k in zip(range(0, 10, 3), range(3, 10, 3)):
            for j, h in zip(range(0, 10, 3), range(3, 10, 3)):
                subgroups[(range(i, k), range(j, h))] = np.reshape(
                    self.sudokuPuzzle[i:k, j:h], self.sudokuPuzzle[i:k, j:h].size)
        return subgroups

    def reducePossibilities(self, row, rowElement):
        """
        """
        possibilities = itertools.chain(self.sudokuPuzzle[row], self.sudokuPuzzle[
                                        :, rowElement], self.group(row, rowElement))
        self.decisionTree[row][rowElement] = np.setdiff1d(
            self.decisionTree[row][rowElement], possibilities)
        if len(self.decisionTree[row][rowElement]) == 1:
            self.sudokuPuzzle[row][
                rowElement] = self.decisionTree[row][rowElement]
            self.decisionTree[row].pop(rowElement)
        if len(self.decisionTree[row]) == 0:
            self.decisionTree.pop(row)
        self.subgroups = self.getSubGroups()

    def solve(self):
        """
        """
        while len(self.decisionTree) != 0:
            decisionTree = copy.deepcopy(self.decisionTree)
            for row, emptyRowElements in decisionTree.items():
                for emptyRowElement, possibilities in emptyRowElements.items():
                    self.reducePossibilities(row, emptyRowElement)
