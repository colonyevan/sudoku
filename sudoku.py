"""A program that solves a puzzle using backtracking"""

from random import choice
import re

exp = re.compile('\d*')

puzzles = [
     '9.2.5..8.9..21..35753.869.....3.....3...7...1.....4.....719.45626..45..9.4..3.1.8']


class Puzzle:
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
                'You didn\'t enter a valid string. please enter 81 integers: ')

        counter = 0

        for i in data:
            self.grid[counter / 9][counter % 9] = i
            counter += 1

        return

    def printGrid(self):
        """Prints the sudoku grid"""
        for i in self.i:
            for j in self.i[j]:
                print(f'{self.grid[i][j]} f')
            print('\n')

    def getRandom(self):
        """Get a random Sudoku string"""
        return choice(puzzles)


def runner():
    obj = Puzzle()
    obj.printGrid()


runner()
