"""@package docstring
Testing out Doxygen
"""

# Imports

# GameBoard class
#class GameBoard()

    # Initialize a game board
    def __init__(self):

        # Ask the user for the board dimensions
        self.set_dimensions()

        # Ask the user for the number of mines
        self.set_num_of_mines()

    '''
        FUNCTIONS TO SET OR GET BOARD PROPERTIES
    '''

    # Get dimensions
    # TODO: Add input error checking
    def set_dimensions(self):
        """ Trying to write comments that work with Doxygen
        """
        print("In set_dimensions")

    # Set the number of mines
    # TODO: Add input error checking
    def set_num_of_mines(self):
        print("In set_num_of_mines")

    # Generate the board
    # TODO: Create an mxn array containing all of the game cells
    def generate_board(self):
        print("In generate_board")


    # Find and mark all the of the empty cells adjacent to a mine
    def mark_adjacent(self):
        print("In mark_adjacent")


    '''
        MISC. FUNCTIONS
    '''

    # Traverse the board
    def traverse_board(self):
        print("In traverse_board")

    # Place mines
    def place_mines(self):
        print("In place_mines")

    # Print the board
    # The function prints each row individually
    def print_board(self):
        print("In print_board")
