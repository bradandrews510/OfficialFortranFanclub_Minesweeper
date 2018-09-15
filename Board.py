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

    ''' GET FUNCTIONS '''

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


    ''' BOARD GENERATION FUNCTIONS '''
    # Generate the board
    def generate_board(self):
        """ @pre    None
            @post   Generates the game board...
            @return None
        """

        # Generate a blank board
        self.board = [[Cell() for j in range(0, self.width)] for i in range(0, self.height)]


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
