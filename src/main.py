#!/usr/bin/env python3

from Sudoku import Sudoku, SudokuIO
import optparse

if __name__ == '__main__':
    usage = "Usage: main.py [options] arg1"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option(
        '-i', '--input-file', action="store", type="string",
        dest="inputFile",
        help="Specify file where sudoku puzzle is stored")
    parser.add_option('-o', '--output-file', action='store', type="string",
                      dest="outputFile",
                      help="Specify a file to store the solved sudoku")
    parser.add_option('-v', '--verbose', action="store_true", dest="verbose",
                      help="For a verbose output of the solving process")
    (options, args) = parser.parse_args()
    if options.inputFile is None and options.outputFile is None:
        parser.print_help()
    else:
        # Open the csv
        sudokuIO = SudokuIO()
        # Get file contents
        sudokuPuzzle = sudokuIO.readFromFile(options.inputFile)
        # Initialize Sudoku solver
        sudoku = Sudoku(sudokuPuzzle)
        #Verbose output
        if options.verbose:
            print("Initial Puzzle")
            print(sudoku.puzzle)
        # Call to solve method
        sudoku.solve()
        # Verbose output
        if options.verbose:
            print("Solved puzzle")
            print(sudoku.puzzle)
        # if -o option selected
        if options.outputFile:
            sudokuIO.writeToFile(sudoku.puzzle, options.outputFile)
