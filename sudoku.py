"""A program that solves a puzzle using backtracking"""

from random import choice
import re

exp = re.compile('([0-9]*\.*)*')

puzzles = [
     '53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79']

class Solved(Exception):
    pass

class Puzzle:
    grid = [[] for i in range(9)]

    def __init__(self):
        """Initalizes the grid to a proper string"""
        self.readPuzzle()

    def readPuzzle(self):
        """Asks user for Sudoku string if none specified"""
        userInput = input('Generated (G) grid or User (U) specified? ')

        data = ''

        while userInput not in ['G', 'U']:
            userInput = input('Please enter a valid choice: ')

        if userInput == 'G':
            data = self.getRandom()

        if len(data) != 81:
            data = input('Please enter a Sudoku puzzle string: ')

        while len(data) != 81 or exp.fullmatch(data) is None:
            data = input(
                'You didn\'t enter a valid string. please enter 81 integers or deciamls: ')

        counter = 0

        for num in data:
            self.grid[int(counter / 9)].append(num)
            counter += 1

        print('\n')
        return

    def printGrid(self):
        """Prints the sudoku grid"""
        for row, i in enumerate(self.grid):
            for col, j in enumerate(i):
                print(j, end = " ")
                if ((col + 1) % 3 == 0 and col is not 8):
                    print('|', end=" ")
            print('\n', end = "")
            if (row + 1) % 3 == 0 and row is not 8:
                print('------+-------+-------')

    def getRandom(self):
        """Gets a random Sudoku string"""
        return choice(puzzles)

    def backtrack(self, row, col):
        """Uses backtracking to figure out the answer to a puzzle"""
        # If it is already filled, means it was given, skip
        if row == 9 and self.valid():
            print("Solved!")
            self.printGrid()
            raise Solved
        # Else, start the loop here
        elif self.grid[row][col].isdigit():
            if col == 8:
                self.backtrack(row + 1, 0)
            else:
                self.backtrack(row, col + 1)
        else:
            for num in range(1, 10):
                self.grid[row][col] = str(num)
                if self.valid():
                    if col == 8:
                        self.backtrack(row + 1, 0)
                    else:
                        self.backtrack(row, col + 1)
                self.grid[row][col] = '.'
        return
    
    def valid(self):
        """Figures out if the current board is valid"""
        col_items = [set() for i in range(9)]
        box_items = [set() for i in range(9)]

        for row in range(9):
            row_items = set()
            for col in range(9):
                if self.grid[row][col].isdigit():
                    item = self.grid[row][col]
                    if item in row_items or item in col_items[col]:
                        return False
                    row_items.add(item)
                    col_items[col].add(item)

                    index = (row // 3) * 3 + col // 3
                    if item in box_items[index]:
                        return False
                    box_items[index].add(item)
        return True

def runner():
    """Runs the Puzzle Object"""
    obj = Puzzle()
    obj.printGrid()
    try:
        obj.backtrack(0, 0)
    except Solved:
        return True
    else:
        return False

runner()
