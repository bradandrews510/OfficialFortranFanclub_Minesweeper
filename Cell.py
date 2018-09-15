"""@package docstring
   Cell class?
"""

class Cell:
    def __init__(self):
        # The default cell is completely blank
        self.isMined     = False
        self.isFlagged   = False
        self.isRevealed  = False

        self.numAdjacent = 0

        # This is the text representation of what's in the cell
        # M: Mine
        # n: The number of adjacent mines. Can only occurs when isMined == False
        self.textRep = '-'

        # The default image will be a regular cell
        self.image = "default..."

    ''' GET FUNCTIONS '''

    def get_cell_textRep(self):
        return self.textRep


    ''' SET FUNCTIONS '''
    def set_mine(self):
        self.isMined = True
        self.textRep = 'M'

    # Toggle the isFlagged flag
    """ @post   Toggles the isFlagged state
        @return 0 indicates nothing was done, -1 means the cell was unflagged,
                and 1 means that the cell was flaggeds
    """
    def set_flag(self):
        if self.isRevealed == True:
            return 0

        if self.isFlagged == False:
            self.isFlagged = True
            return -1 # This is supposed to subtract one flag from the player's
            # available flags

        elif self.isFlagged == True:
            self.isFlagged = False
            return 1 # Return +1 flags to player

        else:
            print("Error, we should not have reached this point")

    # Once revealed, a mine cannot be unrevealed
    def set_revealed(self):
        self.isRevealed = True

    # Set the number of adjacent mines to nMines
    def set_num_adj_mines(self, nMines):
        # We convert the number of mines to a string in order to keep all text
        # representations as the same data type
        self.numAdjacent = str(nMines)





''' Their stuff ***

#cell and flag images 20x20

cell_size = 20
cell_contents = {
    '1' : one_image,
    '2' : two_image,
    '3' : three_image,
    '4' : four_image,
    '5' : five_image,
    '6' : six_image,
    '7' : seven_image,
    '8' : eight_image,
    'M' : mine_image,
    '-' : revealed_image
}
'''
