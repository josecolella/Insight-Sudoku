Insight Sodoku
==============

A commandline sodoku solver for the Insight Data Engineering Fellows Program

Coding Deadline: November 3rd at 11pm

Command line program
--------------------

!["Command line program"](http://cl.ly/image/3X1C0F3M3E1H/program.png)

The command line program allows the user two options:
    - To input the sudoku puzzle from a csv file and output the results to a csv file
    - To input the sudoku puzzle from a csv file and output to the standard output

For the first option, interacting with the command line can be as follows:

```python3
python3 main.py -i sudoku.csv -o solution.csv -v
```

!["Result of fileoutput"](http://cl.ly/image/2K021I2I1X0S/fileoutput.png)

A *solution.csv* file is created in the directory containing the solution


For the second option, interacting with the command line can be as follows:

```python3
python3 main.py -i sudoku.csv -v
```

!["Result of stdout"](http://cl.ly/image/2G2k0q3K1q16/stdoutput.png)



Execute tests
--------------

Test cases have been created for three different sudoku puzzles. These
cases can be found in the test directory

```sh
cd test
```

To execute tests

```sh
python3 test.py
```
