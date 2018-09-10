"""@package docstring
   Game Board... this file or the class needs to be renamed
"""

# Imports

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
        FUNCTIONS TO SET OR GET BOARD PROPERTIES
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


    # Generate the board
    def generate_board(self):
        """ @pre    None
            @post   Generates the game board...
            @return None
        """
        print("In generate_board")

        # Generate a blank board
        self.board = [['-' for j in range(0, self.width)] for i in range(0, self.height)]


    # Find and mark all the of the empty cells adjacent to a mine
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

    # Place mines
    def place_mines(self):
        """ @pre    The number of mines n is valid
            @post   Populates the game board with n mines
            @return None
        """
        print("In place_mines")

    # Print the board
    # FOR TESTING PURPOSES ONLY
    def print_board(self):
        for i in self.board:
            print(i)




# TESTING CODE
tB = GameBoard(5, 2, 1)
tB.print_board()

aB = GameBoard(3, 7, 1)
aB.print_board()

bB = GameBoard(4, 4, 1)
bB.print_board()

cB = GameBoard(6, 4, 1)
cB.print_board()

dB = GameBoard(4, 5, 1)
dB.print_board()

eB = GameBoard(5, 5, 1)
eB.print_board()
