# This script shows the bases for the algorithm

import numpy as np
import itertools

a = [
    [0, 3, 5, 2, 9, 0, 8, 6, 4],
    [0, 8, 2, 4, 1, 0, 7, 0, 3],
    [7, 6, 4, 3, 8, 0, 0, 9, 0],
    [2, 1, 8, 7, 3, 9, 0, 4, 0],
    [0, 0, 0, 8, 0, 4, 2, 3, 0],
    [0, 4, 3, 0, 5, 2, 9, 7, 0],
    [4, 0, 6, 5, 7, 1, 0, 0, 9],
    [3, 5, 9, 0, 2, 8, 4, 1, 7],
    [8, 0, 0, 9, 0, 0, 5, 2, 6],
]


npArray = np.array(a)


# Get all the indices where the zeros are present
b = {j: {k: np.arange(9) for k in np.where(i == 0)[0].tolist()} for i, j in zip(
    npArray, np.arange(npArray.shape[0]))}

# To get elements from row
# Remove duplicates

# you need to add the 3x3 groups
d = {}
for i, k in zip(range(0, 10, 3), range(3, 10, 3)):
    for j, h in zip(range(0, 10, 3), range(3, 10, 3)):
        d[(range(i, k), range(j, h))] = np.reshape(
            npArray[i:k, j:h], npArray[i:k, j:h].size)


def group(row, element):
    for i, j in d.items():
        if row in i[0] and element in i[1]:
            return j

# finds element that Return the sorted, unique values in ar1 that are not
# in ar2.
    np.setdiff1d(
        b[0][0], npArray([itertools.chain(npArray[0], npArray[:, 0]), group(0, 0)]))
    np.setdiff1d(b[7][3], itertools.chain(npArray[7], npArray[:,3], group(7,3)))
# This creates the structure that will be needed to find the results

# print(a)
# print(npArray)

# The problem with this algorithm is that when a medium or hard sudoku
# puzzle is given an infinite loop is started.
#   tree copy and self.decisionTree are the same as no more
#   possibilities can be reduced
#
# # Returns the index and the number of missing elements in the row for all the rows
# b = [(index,len(elements)) for index, elements in a.items()]
#
# (i[0] for i in sorted(b,key=operator.itemgetter(1)))


# Also take into consideration the 3 columns and rows
# for i,j in a.items():
#   a[i]   q[]
#
#
#   >>> np.setdiff1d(a.decisionTree[1][8],itertools.chain(a.decisionTree[0][6], a.decisionTree[0][8],a.decisionTree[1][7],a.decisionTree[2][7]))
#array([2])
