"""@package docstring
   Game Board... this file or the class needs to be renamed
"""

# Imports
import random

from Cell import *



'''
    CELL STRING CONVENTION

    An generated but uninitialized will be labelled as 'M-0-F-H'
'''

# GameBoard class
class GameBoard:

    # Initialize a game board
    def __init__(self, width, height, numOfMines):

        # Store the height, width, and number of mines
        self.width  = width
        self.height = height
        self.numOfMines = numOfMines

        # Go through the process of generating the board
        self.generate_board()
        self.place_mines()

    '''
        GET FUNCTIONS
    '''

    # Get dimensions
    # I'm keeping these as two different functions because it seems
    # weird to suddenly return this data as a tuple or list when
    # they don't ever seem to be used or passed as such
    def get_height(self):
        """ @pre    None
            @post   None
            @return The board height
        """
        return self.height

    def get_width(self):
        """ @pre    None
            @post   None
            @return The board width
        """
        return self.width


    '''
        BOARD GENERATION FUNCTIONS
    '''
    # Generate the board
    def generate_board(self):
        """ @pre    None
            @post   Generates the game board...
            @return None
        """
        #print("In generate_board")

        # Generate a blank board
        self.board = [[Cell() for j in range(0, self.width)] for i in range(0, self.height)]

    # Place mines
    def place_mines(self):
        """ @pre    The number of mines n is valid
            @post   Populates the game board with n mines
            @return None
        """
        #print("In place_mines")

        mCounter = self.numOfMines
        while mCounter > 0:
            i = random.randint(0, self.height - 1)
            j = random.randint(0, self.width  - 1)

            if self.board[i][j].isMined == False:
                self.board[i][j].set_mine()
                mCounter = mCounter - 1

    # Find and mark all the of the empty cells adjacent to a mine
    # Should be renamed
    def mark_adjacent(self):
        """ @pre    None
            @post   None
            @return None
        """
        print("In mark_adjacent")


    '''
        MISC. FUNCTIONS
    '''

    # Return a dictionary with the accessible directions for some specific cell
    # This is a terrible name that needs to be updated
    def get_acces_by_cell(self, i, j):
        accessibleDirections = {'U' : False, 'U_L' : False, 'U_R' : False,
                      'D' : False, 'D_L' : False, 'D_R' : False,
                      'L' : False, 'R'   : False}

        # Up
        if ((i - 1) >= 0):
            accessibleDirections['U'] = self.board[i-1][j]

        # Up Left
        if ((i - 1) >= 0) and ((j - 1) >= 0):
            accessibleDirections['U_L'] = self.board[i-1][j-1]

        # Up Right
        if ((i - 1) >= 0) and ((j + 1) < self.size):
            accessibleDirections['U_R'] = self.board[i-1][j+1]

        # Down
        if (i + 1) < self.size:
            accessibleDirections['D'] = self.board[i+1][j]

        # Down Left
        if ((i + 1) < self.size) and ((j - 1) >= 0):
            accessibleDirections['D_L'] = self.board[i+1][j-1]

        # Down Right
        if ((i + 1) < self.size) and ((j + 1) < self.size):
            accessibleDirections['D_R'] = self.board[i+1][j+1]

        # Left
        if (j - 1) >= 0:
            accessibleDirections['L'] = self.board[i][j-1]

        # Right
        if (j + 1) < self.size:
            accessibleDirections['R'] = self.board[i][j+1]

        return(accessibleDirections)

    # Print the board
    # FOR TESTING PURPOSES ONLY
    def print_board(self):
        # For every row in the board, create a new (temporary) local array
        # that will be filled with the text representation of the cell
        # self.board[i][j]
        for i in self.board:
            row = []
            for j in i:
                row.append(j.get_cell_textRep())
            print(row)

            row = []




# TESTING CODE
print("2x2 with 2 mines")
tB = GameBoard(2, 2, 2)
tB.print_board()

print("\n\n")

print("3x7 with 4 mines")
aB = GameBoard(3, 7, 4)
aB.print_board()

print("\n\n")

print("4x4 with 6 mines")
bB = GameBoard(4, 4, 6)
bB.print_board()

print("\n\n")

print("6x4 with 1 mine")
cB = GameBoard(6, 4, 1)
cB.print_board()

print("\n\n")

print("4x5 with 7 mines")
dB = GameBoard(4, 5, 7)
dB.print_board()

print("\n\n")

print("5x5 with 3 mines")
eB = GameBoard(5, 5, 3)
eB.print_board()
