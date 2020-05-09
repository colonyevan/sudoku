"""A program that solves a puzzle using backtracking"""
from random import choice
import re
import os
import pygame
import sys
from pygame.locals import *

# Setting the game FPS
FPS = 10

# Global Window Size Vars
WINDOWMULTIPLIER = 5 
WINDOWSIZE = 81
WINDOWWIDTH = WINDOWSIZE * WINDOWMULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * WINDOWMULTIPLIER
SQUARESIZE = int((WINDOWSIZE * WINDOWMULTIPLIER) / 3)
CELLSIZE = int(SQUARESIZE / 3)

# Font Setting
global BASICFONT, BASICFONTSIZE
BASICFONTSIZE = 15
BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

# Colors
WHITE = (255, 255, 255)
LIGHTGRAY = (200, 200, 200)
BLACK = (0, 0, 0)

exp = re.compile('([0-9]*\.*)*')

puzzles = [
     '53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79']

class Solved(Exception):
    pass

class Puzzle(object):
    grid = [[] for i in range(9)]

    def __init__(self) -> None:
        """Initalizes the grid to a proper string"""
        self.readPuzzle()

    def readPuzzle(self) -> None:
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

    def printGrid(self) -> None:
        """Prints the sudoku grid"""
        for row, i in enumerate(self.grid):
            for col, j in enumerate(i):
                print(j, end = " ")
                if ((col + 1) % 3 == 0 and col != 8):
                    print('|', end=" ")
            print('\n', end = "")
            if (row + 1) % 3 == 0 and row != 8:
                print('------+-------+-------')

    def getRandom(self) -> str:
        """Gets a random Sudoku string"""
        return choice(puzzles)

    def backtrack(self, row, col) -> None:
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
    
    def valid(self) -> bool:
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

def drawGrid() -> None:
    # Draw Minor Lines
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, LIGHTGRAY, (0,y), (WINDOWWIDTH, y))
    
    # Draw Major Lines
    for x in range(0, WINDOWWIDTH, SQUARESIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, BLACK, (x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT, SQUARESIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, BLACK, (0,y), (WINDOWWIDTH, y))
    return None

def runner() -> bool:
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    # Mouse variables
    mouseClicked = False
    mousex = 0
    mousey = 0

    # Setting up the grid
    pygame.display.set_caption('Sudoku Solver')
    DISPLAYSURF.fill(WHITE)
    drawGrid()

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        
        if mouseClicked:
            drawBox(mousex, mousey)

        pygame.display.update()    
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    runner()
