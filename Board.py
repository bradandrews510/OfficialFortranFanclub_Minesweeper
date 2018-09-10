"""@package docstring
Testing out Doxygen
"""

# Imports

# GameBoard class
class GameBoard()

    # Initialize a game board
    def __init__(self, width, height, numOfMines):
        self.generate_board()
        self.generate_mines()

    '''
        FUNCTIONS TO SET OR GET BOARD PROPERTIES
    '''

    # Get dimensions

    def set_dimensions(self):
        """ @pre    The dimensions passed are valid
            @post   An
            @return None
        """
        print("In set_dimensions")

    # Generate the board
    # TODO: Create an mxn array containing all of the game cells
    def generate_board(self):
        """ @pre    None
            @post   Generates the game board...
            @return None
        """
        print("In generate_board")


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

    # Traverse the board
    def traverse_board(self):
        print("In traverse_board")

    # Place mines
    def place_mines(self):
        """ @pre    The number of mines n is valid
            @post   Populates the game board with n mines
            @return None
        """
        print("In place_mines")

    # Print the board
    def print_board(self):
        print("In print_board")
