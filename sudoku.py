"""A program that solves a puzzle using backtracking"""

import re

exp = re.compile('[0-9]*')


class Puzzle:
    """A class representing a puzzle"""

    def __init__(self):
        self.i = readPuzzle()

    def readPuzzle():
        temp = input('Please enter a Sudoku puzzle string: ')

        while len(temp) != 81 or exp.fullmatch(temp) is None:
            temp = input(
                'You didn\'t enter a valid string. please enter 81 integers: ')
        
        retObj
        counter = 0

        for i in temp:
            retObj[counter / 9][ counter % 9]
            counter += 1

        return retObj


def runner():
    obj = Puzzle

runner()