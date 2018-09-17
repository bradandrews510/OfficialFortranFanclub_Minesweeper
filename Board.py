"""@package docstring
   Board.py contains the board class that will be used throughout the game. It
   only includes getter functions since the board is created when a Board object
   is instantiated using the given parameters
"""

# Imports
import random

#Our imports
from Cell import *

# GameBoard class
class Board:

    # Initialize a game board
    def __init__(self, width, height):
        """ @pre    width and height have been verified externally and so
        the Board class assumes we have proper values
            @post   Once width and height have been assigned, a call is made to
        generate_board() which will then create an array to represent the board
        """

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
        """ @pre    Assume height is a valid and returnable value
            @post   No changes are made anywhere
            @return Board height
        """
        return self.height

    def get_width(self):
        """ @pre    Assumes width is a valid and returnable value
            @post   No changes are made anywhere
            @return Board width
        """
        return self.width


    '''
        BOARD GENERATION FUNCTIONS
    '''
    # Generate the board
    # This is its own function so that the ability to extend the function for
    # different types of games with different rule sets does not impact
    # anything but this function. In retrospect, maybe we should have done
    # the same for the other parameters as well...
    def generate_board(self):
        """ @pre    Assumes a width and height have been assigned
            @post   Generates the game board using a simple list comprehension
        """

        # Generate a blank board
        self.board = [[Cell() for j in range(0, self.width)] for i in range(0, self.height)]

    '''
    MISC. FUNCTIONS
    '''

    # Return a dictionary with the accessible directions for some specific cell
    # This is a terrible name that needs to be updated
    def get_acces_by_cell(self, i, j):
        """ @pre    Assumes a valid i and j value have been passed. It does not
        attempt to verify if i and j are integers or do any sort of sanity
        check
            @post   If a cell in some direction d is within 1 unit of distance
        to the cell at [i][j], update the dictionary with a 'pointer' to the
        accessible cell... Needs to be reworded...
            @return A dictionary containing all the accessible directions for
        the specific cell located at [i][j]
        """
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
