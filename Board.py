"""@package docstring
   Game Board... this file or the class needs to be renamed
"""

# Imports
import random

from Cell import *


# GameBoard class
class Board:

    # Initialize a game board
    def __init__(self, width, height):

        # Store the height, width, and number of mines
        self.width  = width
        self.height = height

        # Go through the process of generating the board
        self.generate_board()
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

# # TESTING CODE
# print("2x2 with 2 mines")
# tB = GameBoard(2, 2, 2)
# board_create(tB)
# tB.print_board()
# recReveal(tB, 0, 0)
#
# print("\n\n")
#
# print("3x7 with 4 mines")
# aB = GameBoard(3, 7, 4)
# board_create(aB)
# aB.print_board()
# recReveal(aB, 0, 0)
#
#
# print("\n\n")
#
# print("4x4 with 6 mines")
# bB = GameBoard(4, 4, 6)
# board_create(bB)
# bB.print_board()
# recReveal(bB, 0, 0)
#
#
# print("\n\n")
#
# print("6x4 with 1 mine")
# cB = GameBoard(6, 4, 1)
# board_create(cB)
# cB.print_board()
# recReveal(cB, 0, 0)
#
#
# print("\n\n")
#
# print("4x5 with 7 mines")
# dB = GameBoard(4, 5, 7)
# board_create(dB)
# dB.print_board()
# recReveal(dB, 0, 0)
#
#
# print("\n\n")
#
# print("5x5 with 3 mines")
# eB = GameBoard(5, 5, 3)
# board_create(eB)
# eB.print_board()
# recReveal(eB, 0, 0)

def mark_adj(board):
    for i in range(0, board.get_height()):
        for j in range(0, board.get_width()):
            if board.board[i][j].isMined == False:
                # Work cell
                wCell = board.board[i][j]
                accessible = board.get_acces_by_cell(i, j)

                for t in accessible:
                    if t.isMined:
                        wCell.set_num_adj_mines(wCell.get_num_adj() + 1)
                        wCell.set_cell_textRep(str(wCell.get_num_adj()))


'''
                for t in accessible:
                    if t.isMined:
                        board.board[i][j].numAdjacent = board.board[i][j].numAdjacent + 1
                    board.board[i][j].textRep = str(board.board[i][j].numAdjacent)
'''
'''
# TESTING CODE
print("2x2 with 2 mines")
tB = GameBoard(2, 2, 2)
mark_adj(tB)
tB.print_board()

print("\n\n")

print("3x7 with 4 mines")
aB = GameBoard(3, 7, 4)
mark_adj(aB)
aB.print_board()

print("\n\n")

print("4x4 with 6 mines")
bB = GameBoard(4, 4, 6)
mark_adj(bB)
bB.print_board()

print("\n\n")

print("6x4 with 1 mine")
cB = GameBoard(6, 4, 1)
mark_adj(cB)
cB.print_board()

print("\n\n")

print("4x5 with 7 mines")
dB = GameBoard(4, 5, 7)
mark_adj(dB)
dB.print_board()

print("\n\n")

print("5x5 with 3 mines")
eB = GameBoard(5, 5, 3)
mark_adj(eB)
eB.print_board()
'''
