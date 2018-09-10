"""@package docstring
Testing out Doxygen
"""

# Imports

# GameBoard class
class GameBoard()

    # Initialize a game board
    def __init__(self, height, width, numOfMines):

        # Store the height, width, and number of mines
        self.height = height
        self.width  = width
        self.numOfMines = numOfMines

        # Go through the process of generating the board
        self.generate_board()
        self.generate_mines()

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
    # FOR TESTING PURPOSES ONLY
    def print_board(self):
        print("In print_board")
